"""Flask application for Homomorphic Encryption-based Salary Prediction."""

import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import os
from cust import *
from servercalc import *
from os import path

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Render the home page.
    
    Returns:
        Rendered index.html template.
    """
    return render_template('index.html')

@app.route('/customerEncryption', methods=['GET', 'POST'])
def customerEncryption():
    """
    Handle customer encryption data submission.
    
    - Generates encryption keys if not present.
    - Encrypts customer data and saves it to data.json.
    - Renders the cust.html template with encryption keys.
    
    Returns:
        Rendered cust.html template with keys.
    """
    # Check if encryption keys exist; if not, generate and store them
    if not path.exists('custkeys.json'):
        storeKeys()
        
    # Retrieve existing encryption keys
    pub_key, priv_key = getKeys()
    
    # Extract features from the form and convert them to integers
    features = [int(x) for x in request.form.values()]
    # Serialize and encrypt the customer data
    datafileCustomer = serializeDataCustomer(pub_key, features)
    # Save encrypted data to data.json
    with open('data.json', 'w') as file: 
        json.dump(datafileCustomer, file)
    
    # Prepare keys to send to the frontend
    keys = {'public_key': pub_key, 'private_key': priv_key}
    # Render the customer details page with keys
    return render_template('cust.html', keys=keys)

@app.route('/company', methods=['GET', 'POST'])
def company():
    """
    Handle company data submission for salary prediction.
    
    - Serializes and computes encrypted data.
    - Saves the result to answer.json.
    - Renders the company.html template with encrypted data.
    
    Returns:
        Rendered company.html template with encrypted data.
    """
    # Serialize data for the company and compute encrypted results
    datafileCompany = serializeDataCompany()
    # Save encrypted company data to answer.json
    with open('answer.json', 'w') as file:
        json.dump(datafileCompany, file)
        
    # Render the company details page with encrypted data
    return render_template('company.html', datafileCompany=datafileCompany)
   
    # Optionally redirect to the result page
    # return redirect(url_for('result'))

@app.route('/result', methods=['GET', 'POST'])
def result():
    """
    Process the encrypted data to decrypt and display the predicted salary.
    
    Steps:
    - Load encrypted answer from answer.json.
    - Decrypt the result using customer's private key.
    - Round the final result to two decimal places.
    - Render the result.html template with the final result.
    
    Returns:
        Rendered result.html template with the final predicted salary.
    """
    # Load the encrypted answer data
    answer_file = loadAnswer()
    # Initialize the public key from the answer file
    answer_key = paillier.PaillierPublicKey(n=int(answer_file['pubkey']['n']))
    # Unpack the ciphertext and exponent
    ciphertext_str, exponent = answer_file['values']  # Changed from answer_file['values'][0]
    # Create an EncryptedNumber instance
    answer = paillier.EncryptedNumber(answer_key, int(ciphertext_str), exponent)
    # Retrieve customer's keys
    pub_key, priv_key = getKeys()
    if answer_key.n == pub_key.n:
        # Decrypt the answer using the private key
        final_result = priv_key.decrypt(answer)
        # Round the result to two decimal places
        final_result = round(final_result, 2)  # Rounded to 2 decimals
    else:
        final_result = "Keys do not match."
    
    # Render the result page with the final predicted salary
    return render_template('result.html', final_result=final_result)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8080)
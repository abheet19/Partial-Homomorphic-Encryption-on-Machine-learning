# ShieldAI: Privacy-Preserving Machine Learning with Homomorphic Encryption

**[➡️ Live Demo Link](https://private-user-images.githubusercontent.com/60404707/486456602-de17bc96-3278-46b3-94a6-780bd36bea53.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTcxODc3NDcsIm5iZiI6MTc1NzE4NzQ0NywicGF0aCI6Ii82MDQwNDcwNy80ODY0NTY2MDItZGUxN2JjOTYtMzI3OC00NmIzLTk0YTYtNzgwYmQzNmJlYTUzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA5MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwOTA2VDE5MzcyN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVkOWJhOTc1M2RiMjQzOTc0YjBkNWE5OGUzZDU0NjI5YzQ3MmFlOTY1NGNlMTc0NDg0NWQ1NWJlZjMwOWI1NzkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.d_mARPbtyo9Kvjm-NgBlN4gksMANIFuLfkArJ2-SZzY)**

ShieldAI is a web-based system that demonstrates privacy-preserving machine learning. It performs ML inference (Classification and Regression) on encrypted data using Partial Homomorphic Encryption (PHE). This allows for data analysis without ever exposing the raw, confidential data, ensuring the highest level of security and compliance.

---

### Screenshot
![ShieldAI](https://private-user-images.githubusercontent.com/60404707/486255816-16c5e422-85de-44f5-9389-88a9e61d906c.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTcxMDA0NjMsIm5iZiI6MTc1NzEwMDE2MywicGF0aCI6Ii82MDQwNDcwNy80ODYyNTU4MTYtMTZjNWU0MjItODVkZS00NGY1LTkzODktODhhOWU2MWQ5MDZjLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA5MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwOTA1VDE5MjI0M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWY0MzYxNzljZmM0NThlNGVhYmYyNWQyMDU1MDc3ZjQ4ZDcyN2RlYWE4MDlmNjBmZjIyM2ViZjE2ZGFkMTliZjkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.vo_XRrPfGkNH0nCkSn5Pe9hgMim2OFrui4Yvbf_HZWY)

---

### The Problem It Solves
Industries like finance, healthcare, and insurance need to analyze highly sensitive customer data to build predictive models. However, privacy regulations (like GDPR and HIPAA) and the risk of data breaches make it dangerous to process this data in its raw form. ShieldAI provides a solution by allowing ML models to make predictions on data while it remains fully encrypted.

---

### Key Features
- **Secure ML Inference:** Implements the Paillier cryptosystem, a form of Partial Homomorphic Encryption, which allows for mathematical operations (like addition and multiplication by a constant) to be performed on encrypted data.
- **Privacy-Preserving Pipeline:** Developed a complete, secure pipeline where a user can submit encrypted data and receive an encrypted prediction, which only they can decrypt.
- **Classification & Regression:** Supports both major types of supervised learning tasks, demonstrating broad applicability for various business use cases.
- **Cloud-Native Deployment:** Fully containerized with Docker and deployed on Google Cloud Run, showcasing a secure and scalable cloud architecture.
- **Automated CI/CD:** Features a robust CI/CD pipeline using GitHub Actions to automate the build and deployment process, enhancing reliability and security.

---

### Tech Stack

| Category              | Technologies                                                                          |
| --------------------- | ------------------------------------------------------------------------------------- |
| **ML & Security** | Python, Scikit-learn, Paillier Homomorphic Encryption Library, Pandas                 |
| **Backend** | Flask, JavaScript                                                                     |
| **Frontend** | Bootstrap, HTML/CSS                                                                   |
| **Cloud & DevOps** | Google Cloud Run, Google Container Registry, Docker, CI/CD with GitHub Actions, IaC   |

---

# Homomorphic Encryption
Homomorphic encryption is a form of encryption that permits users to perform computations on its encrypted data without first decrypting it. These resulting computations are left in an encrypted form which, when decrypted, result in an identical output to that produced had the operations been performed on the unencrypted data. Homomorphic encryption can be used for privacy-preserving outsourced storage and computation. This allows data to be encrypted and out-sourced to commercial cloud environments for processing, all while encrypted.

## A certain example to show usage of HE

Suppose there is a company **XYZ** which provides Machine learning services through encrypted means to user **ABC** which uses certain parameters to predict his salary through the company's portal such as `age` ,`healthy eating scale` , `active worklife scale` and `gender`. First of all we will use the 
```bash
storeKeys() and getKeys() methods
```  
to generate and load the public and private keys on the client side. After that the client's data will be encrypted using the
```bash
serializeDataCustomer() method
```  
Now company will load and compute on the data using their **Linear Regression** model using these methods
```bash
getData() and computeData()
```  
This is the power of HE , as the company now predicts the customer's salary without actually knowing the values  (as it is encrypted by the client's side ) using complex cryptographic operations .
Finally company sends the response back to user as json file which contains the encrypted result and public key using the method
```bash
serializeDataCompany()
``` 
![Architecture](./architecture.png)

### How to Run Locally

1. **Clone the Repository**
   
   ```bash
   git clone https://github.com/yourusername/Partial-Homomorphic-Encryption-on-Machine-learning.git
   cd Partial-Homomorphic-Encryption-on-Machine-learning
   ```

2. **Set Up a Conda Environment**
   
   ```bash
   conda create -n phe_ml_env python=3.8
   conda activate phe_ml_env
   ```

3. **Install Dependencies**
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the Machine Learning Model**
   
   Before running the application, train the model to generate the `improved_model.pkl` file.
   
   ```bash
   python train.py
   ```

5. **Generate Encryption Keys**
   
   ```python
   # ...existing code...
   python cust.py
   ```

6. **Start the Flask Application**
   
   ```bash
   python app.py
   ```

7. **Access the Application**
   
   Open your web browser and navigate to `http://localhost:8080/` to interact with the application.

## Usage

The main `app.py` (Flask file) contains the code for implementing all the above functions
```bash
@app.route('/customerEncryption', methods=['GET','POST']) 
def customerEncryption():    # Handles the encryption on client side

@app.route('/company', methods=['GET','POST'])
def company():               # Handles the encryption on company side

@app.route('/result', methods=['GET','POST'])
def result():                # Generates the final output on the client side
```

## Final Thoughts
* This is a high-level glimpse into the future of ML and cryptography but not yet production-ready.
* Partial Homomorphic Encryption is a great way to perform complex ML computations on encrypted samples.
* Evolving space with Fully-Homomorphic Encryption which is in research right now.
* This will likely be in demand in the next 5-7 years.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Thanks for reading this and if you like this content please give a **LIKE** to this repository.

## License
[MIT](https://choosealicense.com/licenses/mit/)

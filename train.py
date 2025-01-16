
import pandas as pd
from linmodel import trainImprovedModel

def main():
    # Load the employee data
    df = pd.read_csv('employee_data.csv')
    # Define features and target
    X = df[['age', 'healthy_eating', 'active_lifestyle', 'Gender']]
    y = df['salary']
    # Train and save the model
    trainImprovedModel(X, y)

if __name__ == "__main__":
    main()
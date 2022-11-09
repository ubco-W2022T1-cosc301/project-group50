import pandas as pd
import os

def processData(csv_file):
    df = pd.read_csv(csv_file)
    
    df1= (df.drop(['BMI', 'GenHlth', 'MentHlth', 'PhysHlth', 'Age', 'Education', 'Income', 'Fruits', 'Veggies', 'Sex', 'DiffWalk'], axis =1))
    
    return df1
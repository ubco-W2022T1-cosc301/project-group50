import pandas as pd
import os

def processData(csv_file):
    df = pd.read_csv(csv_file)
    
    df1 = ['BMI', 'GenHlth', 'MenHlth', 'PhysHlth', 'Age', 'Education', 'Income']
    
    dprocessed=(df.drop(df1, axis = 1).replace(["0.0"], "no"))
    
    return dprocessed
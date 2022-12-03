#import statements
import pandas as pd
import os


def readCsv(csv):
    df = pd.read_csv(csv)
    return df


def removeColumns(df):
    dfgh = df.copy().drop(columns = ['CholCheck', 'BMI', 'Smoker','PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare',
                               'NoDocbcCost', 'GenHlth', 'MentHlth', 'PhysHlth', 'Age', 'Education','Income'])
    return dfgh

def reorderColumns(df):
    dfgh = dfgh.iloc[:,[6,0,1,2,3,4,5]]
    return dfgh

def renameColumns(df):
    df.rename(columns = {'HighBP' : 'HighBloodPressure'}, inplace = True)
    df.rename(columns = {'HighChol' : 'HighCholesterol'}, inplace = True)
    df.rename(columns = {'DiffWalk' : 'DifficultyWalkingUpStairs'}, inplace = True)
    df.rename(columns = {'Sex' : 'Gender'}, inplace = True)
    return df
    
def replaceValues(df):
 
    df['Gender'] = df['Gender'].replace(to_replace=0, value='Woman')
    df['Gender'] = df['Gender'].replace(to_replace=1, value='Man')
    df['Diabetes'] = df['Diabetes'].replace(to_replace=1, value=0)
    df['Diabetes'] = df['Diabetes'].replace(to_replace=2, value=1)
    df = df.replace(to_replace=1, value='Yes')
    df = df.replace(to_replace=0, value='No')
    
    return df

def reorderColumns(df):
#re-order columns to present Gender at the beginning
    dfgh = df.iloc[:,[6,0,1,2,3,4,5]]
    return dfgh

def processingChain(csv):
    #read csv file
    df = readCsv(csv)
    
    #remove undesired columns
    df = removeColumns(df)
    
    #re-order columns to present Gender at the beginning
    df = reorderColumns(df)
    
    #rename columns to be more readable and precise
    df = renameColumns(df)
    
    # replace Gender values from 0 & 1 to Woman and Man aswell as replace values from 0 & 1 to Yes and No
    df = replaceValues(df)
    
    return df
    
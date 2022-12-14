import pandas as pd
def pipeline(path):
   
    HD = pd.read_csv(path)

    df = (
        HD.loc[:,['HighBP','BMI','HighChol','Diabetes','HeartDiseaseorAttack','Stroke']]
        .loc[(HD["BMI"] <60)]
    )
    return df
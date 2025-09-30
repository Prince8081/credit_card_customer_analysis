import pandas as pd 
import numpy as np 

df = pd.read_csv('Credit_Card_Dataset.csv')

# print(df.shape)
# print(df.describe())

df.drop_duplicates(inplace=True)


# Strip extra spaces in categorical columns

cat_cols = ['Gender','Marital_Status','Education_Level','Employment_Status']

for col in cat_cols:
    df[col]= df[col].str.strip()


# Risk_Level based on Credit_Score

def credit_risk(score):
    if score >= 750 :
        return "Low Risk"
    if score >= 600:
        return "Medium Risk"
    else:
        "High Risk"

df['Risk_level'] = df['Credit_Score'].apply(credit_risk)


# Customer_Segment based on Annual Income

bins = [0 , 40000 , 80000, 120000 ,np.inf ]
labels = ['Low Income' , 'Mid Income' , 'Upper Mid' , 'High Income']

df['Customer_Segment'] = pd.cut(df['Annual_Income'], bins=bins  , labels=labels)
  

# Late_Payment_Flag

df['Late_Payment_Flag'] = np.where(df['Number_of_Late_Payments'] > 0, "Yes", "No")


# Fraud_Risk_Flag

df['Fraud_Risk_Flag']  = np.where(df['Fraud_Transactions']> 0 , 'Yes' , 'No' )

# Credit_Utilization_Category

bins =[ 0.0 , 0.3 , 0.6 , 0.9 ,1]
labels = ['Low','Moderate','High','Very High']

df['Credit_Utilization_Category'] = pd.cut(df['Credit_Utilization_Ratio'] ,bins=bins, labels=labels )


for col in ['Risk_level','Customer_Segment','Credit_Utilization_Category',
            'Late_Payment_Flag','Fraud_Risk_Flag']:
    df[col] = df[col].astype('category')


# Spend to Income Ratio

df['Spend_to_Income_Ratio'] = ((df['Total_Spend_Last_Year']/df['Annual_Income'])*100).round(2)


# CLV Category

clv_p33, clv_p66 = df['CLV'].quantile([0.33, 0.66])

df['CLV_Category'] = pd.cut(
    df['CLV'],
    bins=[-float('inf'), clv_p33, clv_p66, float('inf')],
    labels=['Low CLV', 'Mid CLV', 'High CLV'])


# Create Transaction Frequency (per year)

df['Tenure_in_Years'] = df['Tenure_in_Years'].replace(0, np.nan)

df['Transaction_Frequency'] = (df['Total_Transactions_Last_Year'] / (df['Tenure_in_Years'])).round(2)

tf_p33, tf_p66 = df['Transaction_Frequency'].quantile([0.33, 0.66])

df['Transaction_Frequency_Category'] = pd.cut(
    df['Transaction_Frequency'],
    bins=[-float('inf'), tf_p33, tf_p66, float('inf')],
    labels=['Low Frequency', 'Medium Frequency', 'High Frequency'])


# Default Risk Flag

df['Default_Risk_Flag'] = np.where(
    (df['Credit_Utilization_Ratio'] > 0.8) & (df['Number_of_Late_Payments'] > 2),
    "High Default Risk", "Low Default Risk")


# Replace inf and -inf with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

print(df)

df.to_csv("Cleaned_Credit_Card_Data.csv", index=False)
print("SAVE")
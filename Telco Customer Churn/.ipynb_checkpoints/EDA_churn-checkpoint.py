import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

path = '/Users/macbookair/Documents/Projects/telco_customer_churn/'
filename = 'Telco-Customer-Churn.csv'

# check missing value (null/ na/ empty string)
df = pd.read_csv(path + filename)

print(df.head(10))
print()


check_missing = pd.concat([df.isna().sum(), df.isnull().sum(),df.eq(' ').sum()],keys=['NaN', 'Nulls','Empty'],axis=1)

df = df.drop(df[df['TotalCharges'] == ' '].index)
df['TotalCharges'] = df['TotalCharges'].astype('float')

categorical = []
numeric = []
for col in df.columns:
    if df[col].dtypes == 'object':
        categorical.append(col)
    else:
        numeric.append(col)

for category in categorical:
    print(df[category].value_counts())
    print()

# change the categorical value to numeric value
# No phone service / No internet service = 0, No = 1, Yes = 2
    
df_changes = df.copy()
for col in df_changes[categorical]:
    print('{} : {}'.format(col, df_changes[col].unique()))
    df_changes[col].replace({"No phone service" : 0}, inplace=True)
    df_changes[col].replace({"No internet service" : 0}, inplace=True)
    df_changes[col].replace({"No" :  1}, inplace=True)
    df_changes[col].replace({"Yes" : 2}, inplace=True)

print(df_changes.head(10))


plt.figure(figsize=(10,10))
sns.heatmap(df_changes.corr(numeric_only = True),cbar=True,annot=True,cmap='Blues')
plt.savefig(path + 'correlation.png')




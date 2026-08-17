import numpy as np
import pandas as pd
df = pd.read_csv('customers_messy_500.csv')
print(df.head(5),df.tail(5),sep='\n')
print(df.shape,df.columns,df.dtypes,sep='\n')
print(df.info())
print(df.describe(include='all'))
#float type data as strings
#null data in every column
#multiple data for same customer

print(df.isna().sum())
print(df.isna().sum()/df.shape[0]*100)
#higher percentage is in age column.So age is most incomplete.

print(df.loc[:9,['customer_id','age','city','score']])
print(df.iloc[:10,:4])

score_series = pd.Series(df.score)
age_score = pd.DataFrame({'age':df.age,'score':df.score})
print(score_series)
print(age_score)
#In loc we have to use labels as column indexing while iloc uses indexes as column indexing.

df.age = pd.to_numeric(df.age,errors='coerce')
df["score"] = df["score"].apply(
    lambda x: float(x.strip().replace("%", "")) / 100
    if isinstance(x, str) and "%" in x
    else pd.to_numeric(x, errors="coerce")
)
    
df["income"] = pd.to_numeric(df["income"].str.strip().str.replace("LKR", "").str.replace(',',''),errors="coerce")

print(df.dtypes)

df.city = df.city.str.strip().str.capitalize().str.replace('Colmbo','Colombo').str.replace('Gale','Galle').replace('',np.nan)
print(df.city.value_counts())

df.dropna(subset=['customer_id'],inplace=True)
df.dropna(thresh=4,inplace=True)

df.age = df.age.fillna(df.age.median())
df.score = df.score.fillna(df.score.median())
df.income = df.income.fillna(df.income.median())

df.city = df.city.fillna(df.city.mode()[0])
#If we drop NaN city rows we loose lot of important informations.

print(df.isna().sum())

before = len(df)
df = df[(df['age']>18) & (df['age']<80) & (df['score']<1) & (df['score']>0) & (df['purchases']>=0)]
print(f'No.of rows removed : {before-len(df)}')
print(df.shape)

df.purchased = df.purchased.apply(lambda x : 1 if x in ['Yes','YES','true','True','y','1']
                                  else 0 if x in ['No','NO','false','False','n','0']
                                  else pd.NA).dropna()

df.drop_duplicates(subset=['customer_id'],inplace=True,keep='first')
df.drop_duplicates(keep='first',inplace=True)

print(f'Final No.of rows : {df.shape[0]}')

df['score_pct'] = df.score*100
df['high_value'] = df['income']>df.income.median()

df.sort_values('score', ascending=False, inplace=True, ignore_index=True)
print(df.head(10))

filtered_customers = df[(df.city=='Colombo') & (df.score>=0.7) & (df.purchased==1)]
print(filtered_customers)
print(len(filtered_customers))

print(df.city.value_counts())

print(df.purchased.value_counts())

print(df.value_counts(subset=['city','purchased']))

print(df.groupby('city')['score'].mean())

print(df.groupby('city')[['income','purchases']].mean())

print(df.groupby('city').agg(
    row_count = ('customer_id','count'),
    mean_age = ('age','mean'),
    mean_score = ('score','mean'),
    purchase_rate = ('purchases','mean')))

# Age, income, score, and purchases can be used as numerical features.
# City can be encoded and used as a categorical feature.
# purchased and high_value can serve as potential prediction targets.
# Customer behavior differs across cities, especially in purchase rates.



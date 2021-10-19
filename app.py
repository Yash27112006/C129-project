import pandas as pd

df = pd.read_csv('star.csv')
#print(df.head())
#print(df.columns)
#print(df.dtypes)

df = df.dropna()
df['Radius'] = 0.102763*df['Radius']

df['Mass'] = df['Mass'].apply(lambda x:x.replace('$','').replace(',','')).astype('float') 
df['Mass'] = df['Mass'] * 0.000954588

print(df.head())
print(df.columns)
print(df.dtypes)

df.drop(['Unnamed: 0'], axis=1, inplace=True)

df.to_csv('Unit_Converter_Star.csv')

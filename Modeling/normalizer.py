import pandas as pd
dataset = pd.read_csv('FixDataBind.csv')
df = pd.DataFrame(dataset)

df['waktu'] = pd.factorize(df['waktu'])[0]
df['hari'] = pd.factorize(df['hari'])[0]
df['idrelay'] = pd.factorize(df['idrelay'])[0]
df['status'] = pd.factorize(df['status'])[0]

df.to_csv('file_name.csv', index=False)
print(df)

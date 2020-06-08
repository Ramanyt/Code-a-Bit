%matplotlib notebook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
plt.style.use('seaborn')


df = pd.read_csv('Dataset.csv')
df.drop(['Unnamed: 0'], 1, inplace=True)
df['Time Serie'] = pd.to_datetime(df['Time Serie'])
df = df.replace('ND', np.NaN)
df.dropna(inplace=True)

df[[ 'AUSTRALIA - AUSTRALIAN DOLLAR/US$','EURO AREA - EURO/US$', 'NEW ZEALAND - NEW ZELAND DOLLAR/US$','UNITED KINGDOM - UNITED KINGDOM POUND/US$', 'BRAZIL - REAL/US$','CANADA - CANADIAN DOLLAR/US$', 'CHINA - YUAN/US$','HONG KONG - HONG KONG DOLLAR/US$', 'INDIA - INDIAN RUPEE/US$','KOREA - WON/US$', 'MEXICO - MEXICAN PESO/US$','SOUTH AFRICA - RAND/US$', 'SINGAPORE - SINGAPORE DOLLAR/US$','DENMARK - DANISH KRONE/US$', 'JAPAN - YEN/US$','MALAYSIA - RINGGIT/US$', 'NORWAY - NORWEGIAN KRONE/US$','SWEDEN - KRONA/US$', 
	'SRI LANKA - SRI LANKAN RUPEE/US$','SWITZERLAND - FRANC/US$', 'TAIWAN - NEW TAIWAN DOLLAR/US$','THAILAND - BAHT/US$']] = (
	df[['AUSTRALIA - AUSTRALIAN DOLLAR/US$','EURO AREA - EURO/US$', 'NEW ZEALAND - NEW ZELAND DOLLAR/US$','UNITED KINGDOM - UNITED KINGDOM POUND/US$', 'BRAZIL - REAL/US$','CANADA - CANADIAN DOLLAR/US$', 'CHINA - YUAN/US$','HONG KONG - HONG KONG DOLLAR/US$', 'INDIA - INDIAN RUPEE/US$','KOREA - WON/US$', 'MEXICO - MEXICAN PESO/US$',
	'SOUTH AFRICA - RAND/US$', 'SINGAPORE - SINGAPORE DOLLAR/US$','DENMARK - DANISH KRONE/US$', 'JAPAN - YEN/US$','MALAYSIA - RINGGIT/US$', 'NORWAY - NORWEGIAN KRONE/US$','SWEDEN - KRONA/US$', 'SRI LANKA - SRI LANKAN RUPEE/US$','SWITZERLAND - FRANC/US$', 'TAIWAN - NEW TAIWAN DOLLAR/US$','THAILAND - BAHT/US$']]
	.apply(pd.to_numeric))

dollars = []
for d in df.columns:
    if ' - ' in d:
        dollars.append(d[((d.find(' - ')+3)):])
    else:
        dollars.append(d)
dollars = dollars[1:]
lst = []
for data in df.columns:
    lst.append(data[:(data.find(' - '))])
lst[0] = 'Time'
df.columns = lst
df = df.set_index(df['Time'])

print(df.head(3))


df_developed = df[['AUSTRALIA', 'NEW ZEALAND', 'UNITED KINGDOM', 'CANADA', 'HONG KONG', 'DENMARK' ,'JAPAN' ,'NORWAY', 'SWEDEN', 'SWITZERLAND', 'TAIWAN']]
# KOREA IS REMOVED
df_undeveloped = df[['EURO AREA', 'BRAZIL', 'CHINA', 'INDIA', 'MEXICO', 'SOUTH AFRICA', 'SINGAPORE', 'MALAYSIA', 'SRI LANKA', 'THAILAND']]

def korea(Include_Korea):
    if Include_Korea == True:
        df_developed = df[['AUSTRALIA', 'NEW ZEALAND', 'UNITED KINGDOM', 'CANADA','KOREA', 'HONG KONG', 'DENMARK' ,'JAPAN' ,'NORWAY', 'SWEDEN', 'SWITZERLAND', 'TAIWAN']]

        plt.figure()
        plt.plot(df.index, df_developed.mean(axis=1), label='Developed Countries')
        plt.plot(df.index, df_undeveloped.mean(axis=1), label='Developing Countries')
        plt.xlabel('Date')
        plt.ylabel('Mean Exchange Rate')
        plt.title('Difference Exchange Rate per US$ between Developed and Developing Countries')
        plt.legend();
        
    else:
        df_developed = df[['AUSTRALIA', 'NEW ZEALAND', 'UNITED KINGDOM', 'CANADA', 'HONG KONG', 'DENMARK' ,'JAPAN' ,'NORWAY', 'SWEDEN', 'SWITZERLAND', 'TAIWAN']]

        plt.figure()
        plt.plot(df.index, df_developed.mean(axis=1), label='Developed Countries')
        plt.plot(df.index, df_undeveloped.mean(axis=1), label='Developing Countries')
        plt.xlabel('Date')
        plt.ylabel('Mean Exchange Rate')
        plt.title('Difference in Exchange Rates per US$ between Developed and Developing Countries')
        plt.legend();

interact(korea, Include_Korea=False);



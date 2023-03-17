#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd
import string
import warnings
import requests
warnings.filterwarnings('ignore')


# In[20]:


#baixando dados do fundamentus
url = 'https://www.fundamentus.com.br/resultado.php'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"  
 }

r = requests.get(url, headers=header)
df = pd.read_html(r.text,  decimal=',', thousands='.')[0]


# In[31]:


for coluna in ['Div.Yield', 'Mrg Ebit', 'Mrg. Líq.', 'ROIC', 'ROE', 'Cresc. Rec.5a']:
    df [coluna] = df[coluna].replace('.' , '')
    df [coluna] = df[coluna].replace(',', '.')
    df [coluna] = df[coluna].astype(str).str.rstrip('%').astype('float') / 100
    
df


# In[35]:


df = df[df['Liq.2meses'] > 1000000]


# In[44]:


ranking = pd.DataFrame()
ranking['pos'] = range(1,151)
ranking['EV/EBITDA'] = df[ df['EV/EBITDA'] > 0 ].sort_values(by=['EV/EBITDA'])['Papel'][:150].values
ranking['ROIC'] = df.sort_values(by=['ROIC'], ascending=False)['Papel'][:150].values


# In[45]:


ranking


# In[47]:


a = ranking.pivot_table(columns='EV/EBITDA', values='pos')
b = ranking.pivot_table(columns='ROIC', values='pos')
t = pd.concat([a,b])
t


# In[48]:


rank = t.dropna(axis=1).sum()
rank


# In[49]:


rank.sort_values()[:15]


# In[ ]:





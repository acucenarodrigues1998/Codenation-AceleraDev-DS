#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


black_friday.head()


# In[37]:


black_friday.info()


# In[38]:


black_friday.describe()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[4]:


def q1():
    return black_friday.shape

q1()


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[83]:


def q2():
    aux = black_friday.loc[(black_friday.Gender == 'F') & (black_friday.Age == '26-35')]
    return int(aux.shape[0])

q2()


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[48]:


def q3():
    return int(black_friday.nunique()['User_ID'])

q3()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[31]:


def q4():
    return black_friday.dtypes.nunique()
    
q4()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[82]:


def q5():
    # Retorne aqui o resultado da questão 5.
    aux = black_friday.loc[(black_friday.Product_Category_2.isna()) | (black_friday.Product_Category_3.isna())]
    return float(aux.shape[0]/black_friday.shape[0])

q5()


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[52]:


def q6():
    return int(black_friday['Product_Category_3'].isna().sum())

q6()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[81]:


def q7():
    return float(black_friday['Product_Category_3'].mode()[0])

q7()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[66]:


def q8():
    purch = black_friday['Purchase']
    norm = (purch-purch.min())/(purch.max()-purch.min())
    return float(norm.mean())

q8()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[80]:


def q9():
    purch = black_friday['Purchase']
    avg = purch.mean()
    stdv = purch.std()
    stand = (purch - avg)/ stdv
    return int(stand.loc[(stand < 1) & (stand > -1)].count())

q9()


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[92]:


def q10():
    # Retorne aqui o resultado da questão 10.
    n_in_2 = black_friday['Product_Category_2'].isna().sum()
    qtd_nan_and = black_friday.loc[(black_friday['Product_Category_2'].isna()) & (black_friday['Product_Category_3'].isna())].shape[0]

    return bool(n_in_2 == qtd_nan_and)

q10()


# In[ ]:





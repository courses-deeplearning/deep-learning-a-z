# -*- coding: utf-8 -*-

# regresion logistica

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%
# importar el dataset
#dataset = pd.read_csv("Data.csv")
dataset = pd.read_csv("Social_Network_Ads.csv")
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values
#%%

print('hello')
#%%

def hla():
    print('hola')

#%%

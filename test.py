
#%%
import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats
from scipy.stats import kstest
from scipy.stats import bartlett
from scipy.stats import levene
data = pd.read_csv("Life Expectancy Data.csv")
data.head()
# %%
d1 = data["Country"]
d2 = data["Life_expect"]
data_cToe = pd.concat([d1,d2],axis=1)
print(kstest(data_m,'norm'))
print(kstest(data_w,'norm'))
#!/usr/bin/env python
# coding: utf-8

# In[1]:


# libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


# In[2]:


df= pd.read_excel(r'C:\Users\orlik\Downloads\tasks\score.xlsx')


# In[3]:


df. head (10)


# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA

# Load the data into a DataFrame
df= pd.read_excel(r'C:\Users\orlik\Downloads\tasks\score.xlsx')

# Select the columns of interest
columns = ["pos1", "pos2", "pos3", "pos4", "pos5", "pos6", "pos7", "pos8", "pos9", "pos10", "pos11", "pos12", "pos13", "neg1", "neg2", "neg3", "neg4", "neg5", "neg6", "neg7", "neg8", "neg9", "neg10", "neg11", "neg12", "neg13"]
df = df[columns]

# Impute the missing values with the mean of the column
imputer = SimpleImputer(strategy='mean')
df_imputed = imputer.fit_transform(df)

# Perform the PCA
pca = PCA()
pca.fit(df_imputed)


# Plot the explained variance ratio for each component
plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_)
plt.xlabel("Principal Component")
plt.ylabel("Explained Variance Ratio")
plt.show()



# In[3]:


pca.explained_variance_ratio_


# In[7]:





# In[ ]:





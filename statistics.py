#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats as st


# In[2]:


pip list


# In[3]:


data = [5, 10, 10, 9, 8]


# In[4]:


mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
mode = st.mode(data)[0]


# In[5]:


print(st.mode(data))
print(st.mode(data)[0])


# In[6]:


print(f"Media: {mean}, Mediana: {median}, Desviación estándar: {std_dev}, Moda: {mode}")


# In[7]:


import matplotlib.pyplot as plt


# In[28]:


data_uni = np.random.normal(10,2,1000)


# In[30]:


mean = np.mean(data_uni)
median = np.median(data_uni)
std_dev = np.std(data_uni)
mode = st.mode(data_uni)[0]


# In[31]:


print(f"Media: {mean}, Mediana: {median}, Desviación estándar: {std_dev}, Moda: {mode}")


# In[32]:


plt.hist(data_uni, bins=30, label='Unimode')


# In[33]:


data_bi = np.concatenate([np.random.normal(5,1,500), np.random.normal(15,1,500)])


# In[34]:


plt.hist(data_bi, bins=30, label='Bimode')


# In[35]:


plt.hist(data_uni, bins=30, label='Unimode')
plt.hist(data_bi, bins=30, label='Bimode')
plt.legend()
plt.show();


# In[59]:


random_data = np.random.randint(0,100,1000)


# In[46]:


random_data


# In[47]:


mean = np.mean(random_data)
median = np.median(random_data)
std_dev = np.std(random_data)
mode = st.mode(random_data)[0]


# In[48]:


print(f"Media: {mean}, Mediana: {median}, Desviación estándar: {std_dev}, Moda: {mode}")


# In[49]:


plt.hist(random_data, bins=100, label='Population')
plt.legend()
plt.show();


# In[50]:


np.mean(random_data)


# In[51]:


random_data


# In[58]:


for _ in random_data:
    print(_)


# In[68]:


np.mean(np.random.randint(0,100,10))


# In[69]:


sample_means = [np.mean(np.random.randint(0,100,100)) for _ in range(1000)]


# In[72]:


plt.hist(sample_means, bins=30, density=True)
plt.title("Teorema del Límite Central")
plt.show()


# # Operaciones Matriciales y Vectoriales

# In[89]:


A = np.array([[1,2],[3,4]])
B = np.array([[2,0],[1,2]])


# In[90]:


A


# In[91]:


B


# In[92]:


print(np.dot(3,4))


# In[93]:


suma = A + B
producto = np.dot(A,B)


# In[94]:


print(f'La suma de los vectores es: {suma}, y su producto punto es {producto}')


# In[95]:


producto


# In[96]:


pip list


# In[ ]:





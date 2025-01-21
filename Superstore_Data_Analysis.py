#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import librairies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


df = pd.read_csv(r"C:\Users\ElMehdi\Documents\Projects\Super-store-data-analysis\Sample - Superstore.csv", encoding='ISO-8859-1')


# In[9]:


df.head(5)


# In[20]:


df.info()


# ##### No null value found

# In[19]:


# cheking for duplicates

if df.duplicated().sum() > 0 :
    print("Duplicates exist")
else:
    print("No duplicates found")


# #### Customer Segmentation

# In[33]:


# Types of customer

types_of_customer = df['Segment'].unique()
print(types_of_customer)


# In[35]:


number_of_customers = df['Segment'].value_counts().reset_index()
number_of_customers = number_of_customers.rename(columns={'Segment':'Type of customer'})


# In[36]:


print(number_of_customers)


# In[45]:


plt.pie(
    number_of_customers['count'],
    labels=number_of_customers['Type of customer'],
    autopct = '%1.1f%%'
)
plt.title("Pie Chart of Customer Types")
plt.show()


# #### Customer Sales Insight

# In[56]:


sales_per_segment = df.groupby('Segment')['Sales'].sum().reset_index()
sales_per_segment = sales_per_segment.rename(columns={'Segment' : 'Types of Customer', 'Sales' : 'Total Sales'})

print(sales_per_segment)

plt.bar(sales_per_segment ['Types of Customer'], sales_per_segment['Total Sales'])
plt.xlabel('types of customer')
plt.ylabel('total sales')
plt.show()


# ### Exploring Customer loyalty

# In[54]:


# customer order frequency

customers_order_frequency = df.groupby(['Customer ID', 'Customer Name', 'Segment'])['Order ID'].count().reset_index()


# In[63]:


# renaming order id

customers_order_frequency.rename(columns={'Order ID' : 'Total Order'}, inplace=True)


# In[69]:


# sorting the total order desc

repeat_customers = customers_order_frequency[customers_order_frequency['Total Order'] >=1]

repeat_customers_sorted = repeat_customers.sort_values(by='Total Order', ascending = False)

print(repeat_customers_sorted.head(12).reset_index(drop = True))


# In[72]:


# Calculating customer sales

customer_sales = df.groupby(['Customer ID', 'Customer Name', 'Segment'])['Sales'].sum().reset_index()

# Sorting the customer sales

Top_spenders = customer_sales.sort_values(by = 'Sales', ascending=False)

print(Top_spenders)


# #### Exploring Shipping Strategies

# In[77]:


shipping_model = df['Ship Mode'].value_counts().reset_index()

shipping_model = shipping_model.rename(columns={'index':'Use Frequency','Ship Mode': 'Mode of Shipement'})

print(shipping_model)


# In[ ]:





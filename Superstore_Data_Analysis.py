#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import librairies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv(r"C:\Users\ElMehdi\Documents\Projects\Super-store-data-analysis\Sample - Superstore.csv", encoding='ISO-8859-1')


# In[3]:


df.head(5)


# In[4]:


df.info()


# ##### No null value found

# In[5]:


# cheking for duplicates

if df.duplicated().sum() > 0 :
    print("Duplicates exist")
else:
    print("No duplicates found")


# #### Customer Segmentation

# In[6]:


# Types of customer

types_of_customer = df['Segment'].unique()
print(types_of_customer)


# In[7]:


number_of_customers = df['Segment'].value_counts().reset_index()
number_of_customers = number_of_customers.rename(columns={'Segment':'Type of customer'})


# In[8]:


print(number_of_customers)


# In[9]:


plt.pie(
    number_of_customers['count'],
    labels=number_of_customers['Type of customer'],
    autopct = '%1.1f%%'
)
plt.title("Pie Chart of Customer Types")
plt.show()


# #### Customer Sales Insight

# In[10]:


sales_per_segment = df.groupby('Segment')['Sales'].sum().reset_index()
sales_per_segment = sales_per_segment.rename(columns={'Segment' : 'Types of Customer', 'Sales' : 'Total Sales'})

print(sales_per_segment)

plt.bar(sales_per_segment ['Types of Customer'], sales_per_segment['Total Sales'])
plt.xlabel('types of customer')
plt.ylabel('total sales')
plt.show()


# ### Exploring Customer loyalty

# In[11]:


# customer order frequency

customers_order_frequency = df.groupby(['Customer ID', 'Customer Name', 'Segment'])['Order ID'].count().reset_index()


# In[12]:


# renaming order id

customers_order_frequency.rename(columns={'Order ID' : 'Total Order'}, inplace=True)


# In[13]:


# sorting the total order desc

repeat_customers = customers_order_frequency[customers_order_frequency['Total Order'] >=1]

repeat_customers_sorted = repeat_customers.sort_values(by='Total Order', ascending = False)

print(repeat_customers_sorted.head(12).reset_index(drop = True))


# In[14]:


# Calculating customer sales

customer_sales = df.groupby(['Customer ID', 'Customer Name', 'Segment'])['Sales'].sum().reset_index()

# Sorting the customer sales

Top_spenders = customer_sales.sort_values(by = 'Sales', ascending=False)

print(Top_spenders)


# #### Exploring Shipping Strategies

# In[15]:


# Counting shipping model and renaming columns

shipping_model = df['Ship Mode'].value_counts().reset_index()

shipping_model = shipping_model.rename(columns={'index' : 'Use Frequency', 'Ship Mode' : 'Mode of Shipement'})

print(shipping_model)


# In[16]:


plt.figure(figsize=(8, 8))
plt.pie(
    shipping_model['count'],
    labels=shipping_model['Mode of Shipement'],
    autopct='%1.1f%%', 
    startangle=140,  
    colors=plt.cm.Paired.colors 
)
plt.title('Distribution of Shipment Modes') 
plt.show()


# In[17]:


# Exploring Sales by States and cities, counting and renaming the columns

state = df['State'].value_counts().reset_index()
state = state.rename(columns={'index' : 'State', 'State' : 'Number of Customers'})

print(state.head(20))


# In[18]:


city = df['City'].value_counts().reset_index()
print(city.head(10))


# In[19]:


# Calculating and sorting Sales by States

state_sales = df.groupby(['State'])['Sales'].sum().reset_index()

top_sales = state_sales.sort_values(by='Sales', ascending=False)

print(top_sales.head(10))


# In[20]:


# Calculating and sorting Sales by Cities

city_sales = df.groupby(['City'])['Sales'].sum().reset_index()

top_city_sales = city_sales.sort_values(by='Sales', ascending=False)

print(top_city_sales.head(10).reset_index(drop=True))


# In[21]:


# looking for the popular product

products = df['Category'].unique()

print(products)


# In[22]:


product_subcategory = df['Sub-Category'].unique()

print(product_subcategory)


# In[23]:


# Counting and sorting the subcategory

subcategory_count = df.groupby('Category')['Sub-Category'].nunique().reset_index()

subcategory_count = subcategory_count.sort_values(by ='Sub-Category', ascending = False)

print(subcategory_count)


# In[24]:


# Calculating the sales by subcategory

subcategory_count_sales = df.groupby(['Category', 'Sub-Category'])['Sales'].sum().reset_index()

subcategory_count_sales = subcategory_count_sales.sort_values(by='Sales', ascending = False)

print(subcategory_count_sales)


# In[25]:


product_category = df.groupby(['Category'])['Sales'].sum().reset_index()

top_product_category = product_category.sort_values(by='Sales', ascending = False)

print(top_product_category.reset_index(drop=True))


# In[26]:


plt.figure(figsize=(8, 8))
plt.pie(
    top_product_category['Sales'],
    labels=top_product_category['Category'],
    autopct='%1.1f%%', 
    startangle=140,  
    colors=plt.cm.Paired.colors 
)
plt.title('Distribution of sales by category') 
plt.show()


# In[27]:


# Sorting the subcategory sales

subcategory_count_sales = subcategory_count_sales.sort_values(by='Sales', ascending=True)

plt.figure(figsize=(10, 8))

plt.barh(
    subcategory_count_sales['Sub-Category'],  # y-axis labels
    subcategory_count_sales['Sales'],  # x-axis values
    color='#004B87',  # Optional: Bar color
    edgecolor='black'  # Optional: Add edges to bars
)


plt.title('Sales by Sub-Category', fontsize=16, fontweight='bold')
plt.xlabel('Sales', fontsize=14)
plt.ylabel('Sub-Category', fontsize=14)

plt.grid(axis='x', linestyle='--', alpha=0.7)

for index, value in enumerate(subcategory_count_sales['Sales']):
    plt.text(value, index, f'{value:,.2f}', va='center')

plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





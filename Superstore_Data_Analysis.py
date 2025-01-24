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


# In[28]:


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


# #### Trend sales analysis

# In[32]:


# Converting 'Order Date' to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')

# Group by year and calculating the sum of sales
yearly_sales = df.groupby(df['Order Date'].dt.year)['Sales'].sum()

# Reset index to convert from Series to DataFrame
yearly_sales = yearly_sales.reset_index()

# Rename columns order date and sales
yearly_sales = yearly_sales.rename(columns={'Order Date': 'Year', 'Sales': 'Total Sales'})

print(yearly_sales)


# In[42]:


# converting the year column to integer type
yearly_sales['Year'] = yearly_sales['Year'].astype(int)

# Create the bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(yearly_sales['Year'], yearly_sales['Total Sales'], color='#1f4e78', edgecolor='black')

# Set x-ticks to show only integer years
plt.xticks(yearly_sales['Year'])

# Add labels and title
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.title('Yearly Sales Performance', fontsize=14)

# Show the chart
plt.tight_layout()
plt.show()


# In[47]:


plt.plot(yearly_sales['Year'], yearly_sales['Total Sales'],marker='o', linestyle='-')


# In[50]:


# Create the line chart
plt.figure(figsize=(8, 5))
plt.plot(yearly_sales['Year'], yearly_sales['Total Sales'], 
         marker='o', linestyle='-', color='#1f4e78', linewidth=2, markersize=8, label='Total Sales')

# Add title and labels
plt.title('Yearly Sales Trend', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)

# Add gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Add legend
plt.legend(loc='upper left', fontsize=10)

# Enhance x-axis ticks for clarity
plt.xticks(yearly_sales['Year'], fontsize=10)

# Tight layout for better spacing
plt.tight_layout()

# Display the chart
plt.show()


# In[52]:


df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
year_sales = df[df['Order Date'].dt.year == 2017]
quarterly_sales = year_sales.resample('Q', on='Order Date')['Sales'].sum()
quarterly_sales = quarterly_sales.reset_index()
quarterly_sales = quarterly_sales.rename(columns = {'Order Date': 'Quarter', 'Sales' : 'Total Sales'})
print(quarterly_sales)


# In[53]:


plt.plot(quarterly_sales['Quarter'], quarterly_sales['Total Sales'], marker = 'o', linestyle = '--')

plt.tight_layout()
plt.xticks(rotation=75)
plt.show()


# In[55]:


df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst = True)
yearly_sales = df[df['Order Date'].dt.year == 2017]
monthly_sales = yearly_sales.resample('M', on = 'Order Date')['Sales'].sum()
monthly_sales = monthly_sales.reset_index()
monthly_sales = monthly_sales.rename(columns={'Order Date':'Month', 'Sales' : 'Total Monthly Sales'})

print (monthly_sales)


# In[56]:


plt.plot(monthly_sales['Month'], monthly_sales['Total Monthly Sales'], marker = 'o', linestyle = '--')


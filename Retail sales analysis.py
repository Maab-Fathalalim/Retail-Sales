
# Retail Sales Dataset✨
# 
# Dataset Overview:
# 
# This dataset is a snapshot of a fictional retail landscape, capturing essential attributes that drive retail operations and customer interactions. It includes key details such as Transaction ID, Date, Customer ID, Gender, Age, Product Category, Quantity, Price per Unit, and Total Amount.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[2]:


data = pd.read_csv("C:/Users/Oooba/Desktop/Analysis with pyhton/Retail sales/retail_sales_dataset.csv")
data.head()


# # Data cleaning and Manipulation

# In[3]:


data.info()


# In[44]:


import datetime as dt
data['Date'] = pd.to_datetime(data['Date'], errors='coerce', infer_datetime_format=True)
data["Year_Month"]=data["Date"].dt.to_period("M")
data=data.sort_values(by="Date")


# In[5]:


data.isnull().sum()


# In[6]:


data.duplicated().sum()


# In[7]:


data.describe()


# In[28]:


data =data.drop("Transaction ID", axis=1)


# In[11]:


Gender_cou=data["Gender"].value_counts()
Gender_cou


# In[47]:


revenue_Trend =data.groupby("Year_Month")["Total Amount"].sum().sort_values(ascending=False)
revenue_Trend


# In[16]:


Product_revenue =data.groupby("Product Category")["Total Amount"].sum().sort_values(ascending=False)
Product_revenue


# In[24]:


Gender_revenue =data.groupby("Gender")["Total Amount"].sum().sort_values(ascending=False)
Gender_revenue


# In[25]:


Gender_order =data.groupby("Gender")["Quantity"].sum().sort_values(ascending=False)
Gender_order


# In[45]:


Age_categ=[(15,25),(26,35),(36,45),(46,55),(56,65)]
data["Age_categ"] =pd.cut(data["Age"],bins=[x[0] for x in Age_categ]+ [Age_careg[-1][1]],labels=[f"{x[0]}-{x[1]}" for x in Age_categ])
data


# In[31]:


Age_revenue =data.groupby("Age_categ")["Total Amount"].sum().sort_values(ascending=False)
Age_revenue


# In[32]:


Total_quantity = data["Quantity"].sum()
Total_quantity


# In[33]:


Total_revenue = data["Total Amount"].sum()
Total_revenue


# # Data Visualization
# 

# In[63]:


from matplotlib import style
style.use("bmh")
plt.figure (facecolor="white")
revenue_Trend.plot(kind="bar", color="lightgreen")
plt.title(" Revenue Trend")
plt.xlabel("Date")
plt. ylabel("Revenue")
plt.grid(True)
plt.show()


# In[64]:


colors=["lightgreen","lightcoral"]
plt.pie(Gender_cou ,labels=['Male', 'Female'], autopct='%1.1f%%',colors=colors, explode=[0,0.1],shadow=True)
plt.legend()
plt.show()


# In[65]:


Product_revenue.plot(kind="bar", color="lightgreen")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt. ylabel("Revenue")
plt.grid(True)
plt.show()


# In[68]:


Gender_revenue.plot(kind="bar", color="lightgreen")
plt.title("Revenue by Gender")
plt.xlabel("Gender")
plt. ylabel("Revenue")
plt.grid(True)
plt.show()


# In[71]:


colors=["lightgreen","lightcoral"]
plt.pie(Gender_order ,labels=['Male', 'Female'], autopct='%1.1f%%',colors=colors, explode=[0,0.1],shadow=True)
plt.title("Quantity by Gender")
plt.legend()
plt.show()


# In[72]:


Age_revenue.plot(kind="bar", color="lightgreen")
plt.title("Revenue by Age")
plt.xlabel("Age")
plt. ylabel("Revenue")
plt.grid(True)
plt.show()


# In[ ]:





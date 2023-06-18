#!/usr/bin/env python
# coding: utf-8

# 
# # What month has the best Sales?
# 
#                 
#             
# 
#     
#     
#     
# 

# # First i will merge the csv files of All months

# In[ ]:


import pandas as pd
df = pd.read_csv("data\Sales_September_2019.csv")
months = ['January', 'February', 'March',
          'April', 'May', 'June', 'July', 'August', 'September', 'October'
          , 'November', 'December']



for month in months:
    name = "data\Sales_" + month+ "_2019.csv"
    with open(name, "r") as inFile, open("outF.csv" , "a") as out:
             file1_contents = inFile.read()
             out.write(file1_contents)
                


# ##  I will create a month column

# In[2]:


import pandas as pd
import numpy as np
df = pd.read_csv("outF.csv")



dic = {
    "01" : "January",
    "02" : "February",
    "03" : "March",
    "04" : "April",
    "05" : "May",
    "06" : "June",
    "07" : "July",
    "08" : "August",
    "09" : "September",
    "10": "Octorber",
    "11" : "Novmber",
    "12": "December"
    
}
month = lambda sub : dic[sub] if sub in dic else ""

df["Month"] = df["Order Date"].str[0:2].dropna().apply(month)
df


# In[3]:


months = df["Month"].unique()
import numpy as np

m = np.delete(months,[0,1,2])


value = pd.to_numeric(df[df["Month"] == "January"]["Price Each"]   ) 
value2=  pd.to_numeric(df[df["Month"] == "January"]["Quantity Ordered"]   )



values = [(value * value2).sum()]
for month in m:
    
    value = pd.to_numeric(df[df["Month"] == month]["Price Each"]   )
    value2=  pd.to_numeric(df[df["Month"] == month]["Quantity Ordered"]   )
    
    nd = (value * value2).sum()
    values.append(nd)
    
   

    
    
    
    


# In[4]:


import matplotlib.pyplot as plt

months = range(1,13)
plt.bar(months, pd.Series(values))

plt.xticks(months)
plt.show()


# ## Task2 
# 

#  #### Finding the city with highes sales

# In[ ]:





# ###  1 - I will create a city column based on the adress column
# ### 2- For each city multiply the price column by the quanity column 

# In[5]:


df["City"]  =df["Purchase Address"].str.split(",").dropna().apply(lambda x : x[1] if (len(x) >1 ) else x[0])


cities = df["City"].unique() 
cities  = np.delete(cities, [cities.size -1 ]  ) 
salesL =[]
for city in cities:
    
    price = pd.to_numeric(df[df["City"] == city]["Price Each"] )
  
    quant = pd.to_numeric(df[df["City"] == city]["Quantity Ordered"] )
    sales = (price * quant).sum()
    salesL.append(sales)
    print("For ", city , " Sales:" , sales)
    




# In[ ]:





# In[ ]:





# In[ ]:





# ###  Task 3 

# #### Generate a column of the prodcuts sold  togther
# 

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:





# In[6]:





# In[ ]:


#df[df["Order ID"].duplicated(keep = False)].groupby('Order ID')["Product"].head()


# In[8]:


products = df[df["Order ID"].duplicated(keep = False)].groupby("Order ID")["Product"].agg(lambda x: ', '.join(x)  ).reset_index()

products


# ## Task3 

# ### What product has been sold the most?

# In[ ]:





# In[11]:


df["Quantity Ordered"] = df["Quantity Ordered"].apply(lambda x: x if(str(x).isdigit())else 0)

df["Price Each"] = df["Price Each"].apply(lambda x: x if(str(x).isdigit() or "." in str(x) )else 0)
df["Sales"] = pd.to_numeric(df["Price Each"])  * pd.to_numeric(df["Quantity Ordered"])


# In[12]:


df2 = df.sort_values(by='Sales', ascending=False)


lst1 = df2["Product"].unique()
lst2 = df2["Sales"].unique()
for i in range(len(df2["Product"].unique())):
    product = lst1[i]
    sale= lst2[i]
    print("Product= " , product, ", Sale: " , sale)
    
            


# In[ ]:





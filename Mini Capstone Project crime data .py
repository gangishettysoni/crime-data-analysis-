#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pymysql')


# # 2.Database Connection:

# In[2]:


import pymysql
conn=pymysql.connect(host='localhost',
                 user='root',
                  password='soni',
                   database='minicapcrimedata')
conn


# In[3]:


import warnings
warnings.filterwarnings("ignore")


# In[4]:


import pandas as pd
query="select * from crime_data"
df=pd.read_sql(query,conn)


# In[5]:


print(type(df))


# In[6]:


#our dataframe is ready with crime data to analyze
df


# # 3.Data Exploration:

# Retrieve basic statistics on the dataset, such as the total number of records and unique values in specific columns --- Identify the distinct crime codes and their descriptions.

# In[9]:


## perform the pandas operation to know more about data
df.info


# In[10]:


## total no of  records in crime_data 
df.shape


# In[11]:


df.dtypes


# In[12]:


#get statistical information about data 
df.describe(include="all")


# In[13]:


cols=df.columns
cols


# In[14]:


##unique value in specific colums


# In[15]:


df["AREA_NAME"].unique()


# In[16]:


df["Location"].unique()


# identify the distrinct crime codes and their descriptions

# In[17]:


df["Crm_Cd"].unique()


# In[18]:


df["Crm_Cd_Desc"].unique()


# # 4.Temporal Analysis:

# analyze the temporal aspects of data 

# In[19]:


df[['Date_Rptd','DATE_OCC']]


# In[20]:


#convert data type object to datetime
df['Date_Rptd']=pd.to_datetime(df['Date_Rptd'])
df['DATE_OCC']=pd.to_datetime(df['DATE_OCC'])
df.info()


# In[21]:


#how many days after crime occured 
delta=df['Date_Rptd']-df['DATE_OCC']
delta


# determine trends in crime occurrence overtime.

# In[22]:


df['month Occured']=df['DATE_OCC'].dt.month_name()
df.head()


# In[23]:


df['month Occured'].unique()


# In[31]:


df['AREA_NAME'].unique()


# In[39]:


grp_gen=df.groupby(by="AREA_NAME")
grp_gen


# In[36]:


df       


# In[40]:


grp_gen.count()


# In[29]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[33]:


month_order=['January','February','March','April','May','June', 'July',  'August','September','October','November','December']


# In[46]:


plt.figure(figsize=(10,2))#width,height
plt.title("Understanding of scatter plot using AREA_NAME and month Occured ")
AREA_NAME=['Southwest', 'Central', 'N Hollywood', 'Mission', 'Van Nuys',]
monthOccured=['January','February','March','April','May']
plt.scatter(AREA_NAME,monthOccured)
plt.xlabel("Area names of crime")
plt.ylabel("month")
plt.show()


# ## scatter plot --- relationship between 2 numerical variables

# In[54]:


plt.figure(figsize=(10,8))
plt.scatter(df['Vict_Age'],df['Status'])
plt.show()


# # 6.Victim Demographics:

# Investigate the distribution of victim ages and genders.
# 
#    - Identify common premises descriptions where crimes occur.

# In[55]:


plt.figure(figsize=(10,2))
sns.lineplot(x=df['Vict_Age'],y=df['Status'])
plt.show()


# In[56]:


plt.figure(figsize=(10,2))#width,height
AREA_NAME=['Southwest', 'Central', 'N Hollywood', 'Mission', 'Van Nuys']
monthOccured=['January','February','March','April','May']
plt.plot(AREA_NAME,monthOccured)
plt.show()


# In[72]:


plt.bar(df['Status'],df['Vict_Age'])
plt.show()


# In[79]:


# pie chart -- categorical -- univarient   plt.
plt.pie(df['Status'].value_counts().values,labels=df['Status'].value_counts().index)
plt.show()


# In[83]:


plt.figure(dpi=100) #dots per inch
plt.pie(df['Status'].value_counts().values,labels=df['Status'].value_counts().index,autopct="%0.4f%%",colors=["green","pink","yellow","blue"])
plt.show()


# In[84]:


## univarient -- numerical   ,
plt.hist(df['Vict_Age'])
plt.show()


# In[85]:


plt.hist(df['Vict_Age'],edgecolor="black",bins=4)
plt.show()


# In[88]:


sns.distplot(df['Vict_Age'],bins=5) #distribution
plt.show()



# In[89]:


sns.distplot(df['Vict_Age'],bins=5,hist=False)  #bell curve , kde curve , normal distributed curve
plt.show()


# # 7.Status Analysis

#  Examine the status of reported crimes.
# 
#    - Classify crimes based on their current status

# In[20]:


plt.figure(figsize=(10,2))#width,height
Crm_Cd=['624', '745', '740', '442', '510']
monthOccured =['January','February','March','April','May']
plt.plot(Crm_Cd,monthOccured)
plt.show()                    


# # questions

# Spatial Analysis:

# Where are the geographical hotspots for reported crimes?

# ans:geographical hotspots for reported crimes the places where the crimes occurred most and its in california,los,angeles

# victim Demographics:

# what is the distribution of victim ages in reported crimes?

# Ans: more crimes took place for ages 0 which might be an outlier,apart from that,maxmium of the crimes are observed under age 10.

# Is there a significant difference in crime rates between male and female victims?

# Ans: yes, there a significant difference in crime rates between male and female as crime count of male is as much double as female crime count.

# Location Analysis:

# Where do most crimes occur based on the "Location" column?

# Ans:As Location column unique values almost near to length of Dataframe i.e all location present in the dataset are different,we cannot make any more inferences or conclude just basis on the location.

# Crime Code Analysis:

# What is the distribution of reported crimes based on Crime Code?

# Ans: the crime code 330 and 624 stood on the top with more crimes of 82 and 74.

# In[ ]:





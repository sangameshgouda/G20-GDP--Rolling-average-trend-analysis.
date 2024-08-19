#!/usr/bin/env python
# coding: utf-8

# ### Importing the neccessary libraries

# In[214]:


import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np


# ### Loading the dataset 

# In[247]:


df=pd.read_excel("/Users/sangameshgoudahorapeti/Downloads/G20 GDP Dataset.xlsx")
df.head()


# ### Head of the dataset 

# In[248]:


df.head()


# ###  Tail of the dataset

# In[249]:


df.tail()


# ### Set Country name as the index 

# In[250]:


# Set 'Country Name' as the index
df.set_index('Country Name', inplace=True)


# In[251]:


df.head()
#here we can see that the country name columns become index column


# ### Checking the null values 

# In[252]:


# checking missing values
missing_data = pd.DataFrame(df.T.isnull().sum(), columns = ["Count"])
missing_data["Percentage"] = missing_data["Count"]/len(df) *100
missing_data


# In[ ]:





# From the above dataframe we can see that missing values in country wise rows

# ### Statistical Discription of the dataset 

# In[270]:


df_new=df.transpose()
df_new.describe()


# ### 1 - Visualize data for all the listed countries over time in a single plot, using various colors for each country. Make sure to add a legend. 
# 
#  

# In[253]:


df.head()


# In[254]:


df.columns[1:]


# In[255]:


df.loc["Belgium"][1:]


# In[259]:


# Create a figure and axis object
plt.figure(figsize=(20,15))

# Iterate through each country in the DataFrame
for country in df.index:
    if country !='Country Name':
        # Plot the GDP values over time for each country, excluding the 'Country Name' column
        plt.plot(df.columns[1:], df.loc[country][1:], label=country)

# Add labels and title
plt.title("G20 GDP Over Time")
plt.xlabel("Year")
plt.ylabel("GDP (current US$)")

# Add legend with adjusted parameters
plt.legend()
plt.tight_layout()
plt.show()


# The graph shows the GDP growth over time of several G20 nations
# 
# China shows an exponential development trend, especially from the early 2000s onward, which is consistent with its fast growth in GDP and major rise in global financial power during this period.The other countries' more linear development patterns are indicative of the steady, moderate expansion that describes developed, mature economies.
# Germany, France, and the European Union all show similar growth rates, which could mean that European policy and economic conditions are coordinated.But being not as rapid as China's, India's growth trend during the past three decades shows significant economic improvement.The comparatively flat line from the 1990s represents Japan's economic stagnation during the "Lost Decade," nevertheless there has been a small increase in the years that followed. Russia's GDP varies due to shifts in world oil prices, international developments, and economic shocks and recoveries.

# In[188]:





# ### 2 - Trend analysis over the period provided for the US, China, India, UK, France, Germany, Japan.  Brief interpretation of your results.

# In[260]:


df.head()


# In[261]:


x = df.columns.astype(int)
x


# In[262]:


y = df.loc[country]
y


# In[263]:


# Plotting
plt.figure(figsize=(12, 8))

for country in countries_of_interest:
    x = df.columns.astype(int)
    y = df.loc[country]
    plt.plot(x, y, label=country)

    # Fit a polynomial trend line
    degree = 1  # Degree of the polynomial (1 for linear)
    coeffs = np.polyfit(x, y, degree)
    trend_line = np.polyval(coeffs, x)
    plt.plot(x, trend_line, linestyle='--', color='black')

plt.title('GDP Trend Analysis')
plt.xlabel('Year')
plt.ylabel('GDP (in billions)')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# A few G20 countries' GDP patterns are shown in this graph.
# 
# China's spectacular growth is gaining prominence. China's GDP began in 1960 at around the same point as the other countries and remained similar to them until the 2000s, when it grew more swiftly and surpassed all of the other countries by a considerable margin by 2020.The United States economy is still the strongest in the world, and it is still showing indications of improvement.As a result, Japan's growth rate seems to be decreasing in the 1990s.
# Similar growth trends may be seen in the GDP lines of Japan, France, Germany, and the UK.India's GDP has been increasing, particularly throughout the 2000s. This implies a rapid expansion of the economy, signifying the emergence of an emerging market. In comparing the more dynamic and rapid increases of China and India with the steady growth lines of the United States and Europe, mature economies may be easily identified from rapidly expanding ones.
# 

# ### 3 - 5-year rolling average for the countries listed in part 2. Brief interpretation of your results. Which country has the highest potential for growth over the next 5 years?

# In[264]:


import seaborn as sns
plt.figure(figsize=(30,20))
countries_of_interest = ['United States', 'China', 'India', 'United Kingdom', 'France', 'Germany', 'Japan']
 
# Calculate 5-year rolling average for the selected countries
rolling_avg_df = df.loc[countries_of_interest].rolling(window=5, axis=1).mean()

# Plotting
plt.figure(figsize=(12, 8))

# Plot the GDP data for each country
sns.lineplot(data=df.loc[countries_of_interest].T, palette='tab10')

# Plot the 5-year rolling average for each country
sns.lineplot(data=rolling_avg_df.T, palette='tab10', linestyle='--')

plt.title('GDP Trend Analysis with 5-Year Rolling Average')
plt.xlabel('Year')
plt.ylabel('GDP (in billions)')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', labels=[f'{country}' for country in countries_of_interest] + [f'{country} (5-Year Rolling Avg)' for country in countries_of_interest])
plt.show()


# Looking at the 5-year rolling average GDP trends, China has shown amazing economic momentum, indicating that it has the greatest potential for expansion in the upcoming five years. Its average growth trajectory is not just steep but also rapidly accelerates, in contrast to the more developed economies of the United States, Japan, and Europe, which have steadier, more linear trends. While  China in terms of magnitude, India's rise is also encouraging. If historical trends may indicate potential, they fail to prepare for potential changes in policy, market conditions, or the state of the world economy that could impact these paths. Forecasting has to be done carefully because of this.
# 

# ### 4 - Concluding remarks and inferential analysis based on rolling average trend analysis.  A brief paragraph summarizing your observations.

# Understanding the G20 countries' economic growth and development trends can be gained by looking at their GDP performance over the previous 20 years. Based on their GDP trends, the following is a brief overview of how these nations have been operating:
# 
# United States: Historically, the U.S. has been a major economic powerhouse within the G20. Its GDP growth has been driven by a diverse economy, innovation, technological advancements, and strong consumer spending.
# 
# China: China has experienced remarkable GDP growth over the past two decades, driven by its transition to a more market-oriented economy, massive infrastructure investments, and export-led growth strategies.
# 
# Japan: Japan's GDP growth has been more moderate compared to China and the U.S. Factors such as an aging population, deflationary pressures, and sluggish domestic demand have contributed to its economic challenges.
# 
# Germany: Germany has been a key player in the G20, with a strong emphasis on exports, particularly in automobiles and machinery. Its robust manufacturing sector has been a significant driver of economic growth.
# 
# India: India has emerged as one of the fastest-growing economies within the G20, inspired by a large and youthful population, economic reforms, and a expanding service sector, including IT and outsourcing.
# 
# The 5-year rolling average GDP graph for selected G20 countries depicts long-term trends: China's rapid economic development stabilizes after significant growth, while the US maintains dominance, and France, Germany, and the UK show steady progress. India's economy accelerates since the late 20th century, while Japan experienced a plateau due to economic difficulties but shows signs of improvement. European nations display modest growth with occasional fluctuations linked to regional policies and economic cycles.

# In[ ]:





# In[ ]:





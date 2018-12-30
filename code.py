# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace = True)
print(data.head(10))


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer',
np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both'))

better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)



# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]

top_countries.drop(axis = 0, index = top_countries.tail(1).index, inplace =True)

def top_ten(top_countries,column_name):
    country_list=[]
    top_ten_complete_df = top_countries.nlargest(10,column_name)
    country_list = list(top_ten_complete_df['Country_Name'])
    return(country_list)

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df= data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot(kind = 'bar',x='Country_Name',y='Total_Summer')
winter_df.plot(kind = 'bar',x='Country_Name',y="Total_Winter")
top_df.plot(kind = 'bar',x='Country_Name',y = 'Total_Medals')


# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df[summer_df['Golden_Ratio']==summer_df['Golden_Ratio'].max()]['Country_Name'].values[0]
print(summer_country_gold)


winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df[winter_df['Golden_Ratio']==winter_df['Golden_Ratio'].max()]['Country_Name'].values[0]
print(winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df[top_df['Golden_Ratio']==top_df['Golden_Ratio'].max()]['Country_Name'].values[0]
print(top_country_gold)




# --------------
#Code starts here
data_1 = data.drop(axis=0, index = data.tail(1).index)

data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2+data_1['Bronze_Total']*1

most_points = data_1['Total_Points'].max()
best_country = data_1[data_1['Total_Points']==most_points]['Country_Name'].values[0]


# --------------
#Code starts here

best = data[data['Country_Name']==best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked = True)
plt.xlabel("United States")
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)



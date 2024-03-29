# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)

data.rename(columns={'Total':'Total_Medals'},inplace=True)

data.head(10)


# --------------
#Code starts here

data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',(np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')) )  

better_event=data['Better_Event'].value_counts().idxmax()






# --------------
#Code starts here

top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries.drop(top_countries.index[-1],inplace=True)


def top_ten(variable1,variable2):
    country_list=[]
    country_list=variable1.nlargest(10,variable2).iloc[:,0]
    return country_list


top_10_summer=list(top_ten(top_countries,'Total_Summer'))

top_10_winter=list(top_ten(top_countries,'Total_Winter'))

top_10=list(top_ten(top_countries,'Total_Medals'))


common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))


# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]

winter_df=data[data['Country_Name'].isin(top_10_winter)]
print(winter_df)
top_df=data[data['Country_Name'].isin(top_10)]
print(top_df)

fig, (ax_1,ax_2,ax_3)=plt.subplots(3,1)
summer_df.plot(x='Country_Name',y='Total_Medals',kind='bar',ax=ax_1)
winter_df.plot(x='Country_Name',y='Total_Medals',kind='bar',ax=ax_2)
top_df.plot(x='Country_Name',y='Total_Medals',kind='bar',ax=ax_3)


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer'] / summer_df['Total_Summer']

summer_max_ratio =summer_df['Golden_Ratio'].max()

summer_country_gold=summer_df.loc[summer_df['Golden_Ratio']==summer_max_ratio,'Country_Name'].iloc[0]

winter_df['Golden_Ratio']=winter_df['Gold_Winter'] / winter_df['Total_Winter']

winter_max_ratio =winter_df['Golden_Ratio'].max()

winter_country_gold=winter_df.loc[winter_df['Golden_Ratio']==winter_max_ratio,'Country_Name'].iloc[0]
top_df['Golden_Ratio']=top_df['Gold_Total'] / top_df['Total_Medals']

top_max_ratio =top_df['Golden_Ratio'].max()

top_country_gold=top_df.loc[top_df['Golden_Ratio']==top_max_ratio,'Country_Name'].iloc[0]




# --------------
#Code starts here
data_1=data.drop(data.index[-1])

data_1['Total_Points']=(data_1['Gold_Total']*3) + (data_1['Silver_Total']*2)+data_1['Bronze_Total']

most_points=data_1['Total_Points'].max()


best_country=data_1.loc[data_1['Total_Points']==most_points,'Country_Name'].iloc[0]




# --------------
#Code starts here
best=data[data['Country_Name']==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)



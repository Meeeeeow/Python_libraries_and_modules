# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:22:51 2021

@author: User
"""

import matplotlib.pyplot as plt;
import pandas as pd;

print(plt.style.available);#available styles

plt.style.use('bmh');

# =============================================================================
# plt.xkcd(); #comic like
# =============================================================================
gas = pd.read_csv('gas_prices.csv');
print(gas);
plt.figure(figsize=(11,8),dpi=300);

plt.plot(gas.Year,gas.USA,'bo-',markersize=7,label='USA');

plt.plot(gas.Year,gas.Canada,'ro-',markersize=7,label='Canada');
plt.plot(gas.Year,gas.Japan,color='#9467bd',marker='o',linestyle='solid',markersize=7,label='Japan');
overall_median=3.2
plt.fill_between(gas.Year,gas.Japan,gas['South Korea'],
                 where=(gas.Japan >= gas['South Korea']),interpolate=True,alpha=0.25,label='Higher Price(JPN vs SK)');

plt.fill_between(gas.Year,gas.Japan,gas['South Korea'],
                 where=(gas.Japan<= gas['South Korea']),
                 interpolate=True,color='red',alpha=0.25,label='Cheaper price(JPN vs SK)');
# =============================================================================
# for country in gas:
#     if country != 'Year':
#         plt.plot(gas.Year,gas[country],marker='o',linestyle='solid',markersize=7,label=country);
# =============================================================================

plt.plot(gas.Year,gas['South Korea'],'go-',markersize=7,label='South Korea');

plt.title('Gas Price Plot (in USD)',fontdict={'fontname':'Comic Sans MS','fontsize':20,'fontweight':'bold'});
plt.xlabel('Year',fontdict={'fontname':'Comic Sans MS','fontsize':20});
plt.ylabel('Price (in USD)',fontdict={'fontname':'Comic Sans MS','fontsize':20});
plt.xticks(gas.Year[::3]);
plt.yticks(list(range(1,9)));
plt.legend();
plt.grid(True); #create a grid layout
plt.tight_layout(); #creates a perfect padding style
plt.savefig('Gas Prices over world.png',dpi=300);
plt.show();



#fifa histogram
plt.style.use('bmh');
plt.figure(dpi=300, figsize=(10,7))
fifa = pd.read_csv('fifa_data.csv');
fifa_values = fifa.describe();
print(fifa_values['Overall']);
mean_performance = 66.238699;
bins = list(range(40,101));
print(bins[::10]);
print(plt.hist(fifa.Overall,bins=bins[::10], edgecolor='black' ,log=True, color='violet',label='Player Data'));
plt.xticks(bins[::10]);
plt.axvline(mean_performance,color='#fc4f30',label='Skill Median',linewidth=2);
plt.title('Player Skills in FIFA 2018',fontdict={'fontname':'Comic Sans MS','fontweight':'bold','fontsize':15});
plt.savefig('fifa_performance.png', dpi=300);
plt.legend();
plt.grid(True);
plt.tight_layout();
plt.show();

print(fifa['Preferred Foot']);

left=fifa.loc[fifa['Preferred Foot']== 'Left'].count()[1];
print(left);

right=fifa.loc[fifa['Preferred Foot']=='Right'].count()[3];
print(right);
explode=(0,0.1);
labels='Left','Right';
plt.pie([left,right],explode =explode,labels=labels,shadow=True,autopct='%0.2f %%');
plt.title('Preferred foot FIFA 2018',fontdict={'fontname':'Comic Sans MS','fontsize':15});
plt.show();

# =============================================================================
# fig,ax = plt.subplots();
# print(fig,ax);
# fig,axs=plt.subplots(2,1)
# print(fig,axs);
# =============================================================================
print(fifa.Weight);
fifa.Weight=[int(x.strip('lbs'))*.453592 if type(x)== str else x  for x in fifa.Weight];
print(fifa.Weight);
print(max(fifa.Weight));
print(min(fifa.Weight));

plt.figure(figsize=(8,6),dpi=200);
light_players = fifa.loc[fifa.Weight < 65];
print(light_players.Weight);
light_players_csv = light_players[:];
print(light_players_csv);
light_players_csv=light_players_csv.reset_index(drop=True);
light_players_csv.to_csv('Less than 65kg players data.csv');
light_players = fifa.loc[fifa.Weight<65].count()[0];
print(light_players);
light_medium = fifa.loc[(fifa.Weight>=65) & (fifa.Weight <=80)];
print(light_medium.Weight);
light_medium_weight_csv = light_medium[:];
light_medium_weight_csv = light_medium_weight_csv.reset_index(drop=True);
light_medium_weight_csv.to_csv('65 to 80 kg players.csv');
light_medium=light_medium.count()[0];
print(light_medium);
overweight=fifa.loc[fifa.Weight>80];
overweight_csv=overweight[:];
overweight_csv=overweight_csv.reset_index(drop=True);
overweight_csv.to_csv('More than 80kg players.csv');
overweight=overweight.count()[0];
print(overweight);
weights=[light_players,light_medium,overweight];
labels='Under 65','65-80','Over 80';
explode=(0.1,0.1,0.1);
#change color of pie
plt.style.use('bmh');#use styles
plt.pie(weights,labels=labels,explode=explode,shadow=True,autopct='%0.2f %%',pctdistance=0.7,textprops=dict(color="w",size=14),wedgeprops=dict(edgecolor='black'));
plt.title('Player Weights(Kg) FIFA 2018',fontdict={'fontname':'Comic Sans MS','fontsize':15});
plt.legend(title='Weights',loc='center left',bbox_to_anchor=(0.8, 0.37, 0.5, 1));
plt.show();

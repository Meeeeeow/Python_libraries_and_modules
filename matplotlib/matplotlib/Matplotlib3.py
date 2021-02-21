# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 21:07:07 2021

@author: User
"""

import matplotlib.pyplot as plt;
import pandas as pd;
import numpy as np;
from collections import Counter;
plt.figure(figsize=(10,7),dpi=300);
print(plt.style.available);
plt.style.use('ggplot');
# =============================================================================
# plt.rcdefaults();
# =============================================================================
ages_x=[25,26,27,28,29,30,31,32,33,34,35];
x_indexes = np.arange(len(ages_x));
print(x_indexes);
bar_width=0.25;
dev_y=[30000,35500,40000,45000,50000,55000,60000,65000,70000,75000,80000];
python_devs_y=[50000,55000,60000,65000,70000,75000,60000,70000,80000,40000,60000];
js_devs_y=[37000,43000,45000,46000,60000,50000,70000,65000,70000,80000,76000];
plt.title('Software Devs Median Salary(USD)',fontdict={'fontname':'Comic Sans MS','fontsize':15});

plt.bar(x_indexes-bar_width,dev_y,label='All devs',width=bar_width);
plt.bar(x_indexes,python_devs_y,label='Python devs',width=bar_width);
plt.bar(x_indexes+bar_width,js_devs_y,label='Javascript devs',width=bar_width,color="#444444");
plt.xlabel('Age',fontdict={'fontname':'Comic Sans MS','fontsize':15});
plt.ylabel('Median Salary',fontdict={'fontname':'Comic Sans MS','fontsize':15});
plt.xticks(ticks=x_indexes,labels=ages_x);
plt.legend();
plt.show();

fifa =pd.read_csv('fifa_data.csv');
print(Counter(fifa['Overall']));

Overall_performance = Counter(fifa['Overall']);
plt.figure(figsize=(12,10),dpi=300);
print(Overall_performance.most_common(25));
performance=[];
num_people=[];
for item in Overall_performance.most_common(25):
    num_people.append(item[1]);
    performance.append(item[0]);
print(num_people);
print(performance); 

x2=np.arange(len(performance));
plt.barh(x2,num_people,label='Player performance',color='m');
plt.yticks(ticks=x2,labels=performance);
plt.title('Overall Performance Rating Fifa 2018',fontdict={'fontname':'Comic Sans MS','fontsize':15});
plt.ylabel('Perfrmance Ratings',fontdict={'fontname':'Comic Sans MS','fontsize':15});
plt.xlabel('Number of People',fontdict={'fontname':'Comic Sans MS','fontsize':15});
plt.tight_layout();
plt.legend();
plt.show();   

slices=[59219,55466,47544,36443,35917];
languages=['Javascript','HTML/CSS','SQL','Python','Java'];
plt.figure(figsize=(10,8),dpi=300);
explode=(0,0,0,0,0);
plt.style.use('fivethirtyeight');
plt.pie(slices,labels=languages,explode=explode,startangle=90,shadow=True,autopct='%0.2f %%',wedgeprops=dict(edgecolor='black'),textprops=dict(color="k",size=14));
plt.title('Most popular languages',fontdict={'fontname':'Comic Sans MS','fontsize':15});
plt.tight_layout();
plt.legend(title='languages');
plt.savefig('Popular known languages',dpi=300);
plt.show();

#stackplot

plt.figure(figsize=(7,5),dpi=300);
minutes=[1,2,3,4,5,6,7,8,9];
player1=[1,2,2,2,2,2,3,4,5];
player2=[1,1,1,1,2,2,2,3,3];
player3=[1,1,1,1,1,2,2,2,2];
labels=['player1','player2','player3'];
plt.stackplot(minutes,player1,player2,player3,labels=labels, baseline='zero');
plt.title('Player Performance',fontdict={'fontname':'Comic Sans MS','fontsize':15});
plt.xlabel('Minutes',fontdict={'fontname':'Comic Sans MS','fontsize':15});
plt.ylabel('Scores',fontdict={'fontname':'Comic Sans MS','fontsize':15});
plt.xticks(list(range(1,10)));
plt.legend(loc='upper left');
plt.tight_layout();
plt.show();

#histogram



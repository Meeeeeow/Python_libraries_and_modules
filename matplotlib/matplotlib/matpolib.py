# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 12:27:34 2021

@author: User
"""

import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;


#resize graph
plt.figure(figsize=(3,4),dpi=300); #dpi should be around 300 dpi
#basic graph

x=[1,2,3,4];
y=[2,4,6,8];

# =============================================================================
# print(plt.plot(x,y))
# print(plt.plot(x,y,'bo'));
# =============================================================================
print(plt.plot(y));
print(plt.plot(y,'r+'));
print(plt.plot(x,y,'bo--',linewidth=2,markersize=10,label='2x'));
plt.title('Basic Graphs' ,fontdict={'fontname':'Comic Sans MS','fontsize':20,'color':'red','fontweight' :1000},loc='center');
plt.xlabel('X Axis',fontdict={'fontname':'Comic Sans MS','fontsize':15,'color':'red'});
plt.ylabel('Y Axis',fontdict={'fontname':'Comic Sans MS','fontsize':15,'color':'red'});

#line number 2
x2 = np.arange(1,4.5,0.5);
plt.plot(x2,x2**2,'ro-',markersize=10,linewidth=4,label='x^2');
print(x2);
#graph plotting of x and y (scale of graph)
plt.xticks([0,1,2,3,4,5]);
# =============================================================================
# plt.yticks([0,2,4,6,8,10]);
# =============================================================================

plt.legend(); #shows definition of graph


#save graph
plt.savefig('mygraph.png' , dpi=300);
plt.show();

#bar chart
plt.figure(figsize=(6,4),dpi=200);
labels=['A','B','C'];
values=[10,20,15];
bars = plt.bar(labels,values);
print(bars);
plt.title('Basic Bar Chart',fontdict={'fontname':'Comic Sans MS','fontsize':15,'color':'red'});
plt.xlabel('X Axis',fontdict={'fontname':'Comic Sans MS','color':'red','fontsize':15});
plt.ylabel('Y Axis',fontdict={'fontname':'Comic Sans MS','color':'red','fontsize':15});
# =============================================================================
# 
# =============================================================================
patterns = ('-', '+', 'x');
for bar,pattern in zip(bars,patterns):
    bar.set_hatch(pattern);

# =============================================================================
# patterns = ['-', '+', 'x'];
# for bar in bars:
#     bar.set_hatch(patterns.pop(0));   
# =============================================================================
plt.savefig('barchart.png');
plt.show();

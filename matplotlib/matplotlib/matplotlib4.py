# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 02:17:48 2021

@author: User
"""
#scatter plotting

import pandas as pd;
import matplotlib.pyplot as plt;
from datetime import datetime,timedelta;
from matplotlib import dates as mpl_dates;
from itertools import count;
import random;
import psutil;
import time;
plt.figure(figsize=(10,8),dpi=300);
plt.style.use('seaborn');

i=0;
x,y=[],[];
while True:
    x.append(i);
    y.append(psutil.cpu_percent());
    plt.plot(x,y,color='m');
    time.sleep(0.1);
    i+=1;
    plt.xlim(left=max(0,i-50),right=i+50);
    plt.title('Cpu Usage Over Time',fontdict={'fontname':'Comic Sans MS','fontsize':15});
    plt.xlabel('Time Axis',fontdict={'fontname':'Comic Sans MS','fontsize':15});
    plt.ylabel('Cpu Usage',fontdict={'fontname':'Comic Sans MS','fontsize':15});
    plt.show();
#real time plots




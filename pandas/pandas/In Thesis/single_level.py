# -*- coding: utf-8 -*-
"""
Created on Mon May 10 00:39:57 2021

@author: User
"""

import pandas as pd;

# creating a blank series
Activities = pd.Series([]);

# reading csv file
df = pd.read_csv("user1.csv");

# print(df.head(5));

#name of cols
cols = list(df.columns);
# print(cols);

#number of cols
num_cols = len(df.axes[1]);
# print(num_cols);

# print(len(df));


#conditions if met value added to series
for i in range(len(df)):
    if df['label:LYING_DOWN'][i] == 1 or df['label:SITTING'][i]  == 1 or df['label:SLEEPING'][i] == 1:
        Activities[i]='Inactive';
    elif df['label:FIX_walking'][i] == 1 or df['label:STROLLING'][i] == 1:
        Activities[i]='Walking';
    elif df['label:BICYCLING'][i] == 1 or df['label:OR_exercise'][i] == 1 or df['label:FIX_running'][i] == 1 or df['label:AT_THE_GYM'][i] == 1 or df['label:STAIRS_-_GOING_UP'][i] ==  1 or df['label:STAIRS_-_GOING_DOWN'][i] == 1:
        Activities[i]='Active';
    elif df['label:IN_A_CAR'][i] == 1 or df['label:ON_A_BUS'][i] == 1 or df['label:DRIVE_-_I_M_THE_DRIVER'][i] == 1 or df['label:DRIVE_-_I_M_A_PASSENGER'][i] == 1:
        Activities[i]='Driving';
    else:
         Activities[i]='None';
        

#insert new column at last position
df.insert(num_cols  , "Activity Class", Activities);

#delete rows with no activity class
df = df.loc[(df["Activity Class"] != 'None')];
# print(df.head(5));

#save csv
df.to_csv('Activity Class(00EABED2-271D-49D8-B599-1D4A09240601).csv');
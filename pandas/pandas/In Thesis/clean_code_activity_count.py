# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:37:53 2021

@author: User
"""

import pandas as pd;
import numpy as np;
import datetime;
from collections import Counter;

df = pd.read_csv('user7.csv');
counter = 0;
activity_count = 0;
day_count = 0;


cols = list(df.columns);
modified_df = df[cols[0:3] +[cols[-1]]]; #csv to fill out day state of  a date



date_list = [];
full_activity_list=modified_df['activity'];
activity_list=[];
activity_list1=[];
activity_list2=[];
activity_list3=[];previous_date='';
final_list=dict();
day_state =['Midnight','Morning','Noon','Night'];

def allocate_day_state(hour,activity,date):
        global previous_date,counter,day_count,activity_list,activity_list1,activity_list2,activity_list3;
        
        # one day has passed
        if previous_date != date and previous_date != '':
            #date as key and activities as  values 
            final_list[previous_date] = Counter(activity_list),Counter(activity_list1),Counter(activity_list2),Counter(activity_list3);
            previous_date = date; #mm/dd/yy
            activity_list=[];
            activity_list1=[];
            activity_list2=[];
            activity_list3=[];
            
            
        
        if int(hour) in list(range(0,6)) and date_list[counter] == date:  #midnight
            activity_list3.append(activity);
            previous_date = date;
            counter+=1;   
            return 0;
        
        elif int(hour) in list(range(6,12))  and date_list[counter] == date: #morning
            activity_list2.append(activity);
            previous_date = date;
            counter+=1;
            return 1;
    
        elif int(hour) in list(range(12,18))  and date_list[counter] == date:  #noon
            activity_list1.append(activity);
            previous_date = date;
            counter+=1;
            return 2;

        elif int(hour) in list(range(18,24))  and date_list[counter] == date:  #night
            activity_list.append(activity);
            previous_date = date;
            counter+=1;
            return 3;



for time in df['timestamp']:
    date_list.append(datetime.datetime.fromtimestamp(time).strftime("%D"));
    

# to print out the day state modified csv necessary complonents

for time in df['timestamp']:
    hour = datetime.datetime.fromtimestamp(time).strftime("%H");
    date = datetime.datetime.fromtimestamp(time).strftime("%D");
    activity = df.iloc[activity_count]['activity'];
    time_state = allocate_day_state(hour,activity,date);
    activity_count += 1;
    
# to print out final user csv

final_list = list(final_list.items());
data=[];
segment = ['6pm - 12am','12pm - 6pm','6am - 12pm','12am - 6am']

# list of all activity counts counter  in  each day 
for i in range(len(final_list)):
    activity=[];
    date = datetime.datetime.strptime(final_list[i][0],"%m/%d/%y");
    timestamp = datetime.datetime.timestamp(date)


    day = int(datetime.datetime.fromtimestamp(timestamp).strftime("%w"));
    
    
    #date object from str date
    date_obj = datetime.datetime.strptime(final_list[i][0],"%m/%d/%y").date();
    
    
    #distinct activities in the dataset
    full_activity_list = list(set(full_activity_list));
    
    # to get the counters in a list 
    for item in final_list[i][1]:
            activity.append(item); 
            
    #distribute activity count  over a day in 4  segments        
    walking=[0,0,0,0];
    driving=[0,0,0,0];
    inactive=[0,0,0,0];
    active=[0,0,0,0];
    
    
    # get activity count  matrix  for all activities
    for i in range(len(full_activity_list)):
       
        for k,v in activity[i].items():         
            if i == 0:              #i =0->night ,1->noon , 2 -> mornining ,3->midnight
                if k == 'Walking':
                    walking[i] = v;
                if k == 'Driving':
                    driving[i]= v;
                if k == 'Inactive':
                    inactive[i] = v;
                if k == 'Active':
                    active[i] = v;
            if i == 1:
                if k == 'Walking':
                    walking[i] = v;
                if k == 'Driving':
                    driving[i]= v;
                if k == 'Inactive':
                    inactive[i] = v;
                if k == 'Active':
                    active[i] = v;
            if i == 2:
                if k == 'Walking':
                    walking[i] = v;
                if k == 'Driving':
                    driving[i]= v;
                if k == 'Inactive':
                    inactive[i] = v;
                if k == 'Active':
                    active[i] = v;
            if i == 3:
                if k == 'Walking':
                    walking[i] = v;
                if k == 'Driving':
                    driving[i]= v;
                if k == 'Inactive':
                    inactive[i] = v;
                if k == 'Active':
                    active[i] = v;
   
    
    # print(walking);
    # print(driving);
    # print(active);
    # print(inactive);
    
    ###  i =0->night ,1->noon , 2 -> mornining ,3->midnight
    ###  walking -> 0, driving -> 1, inactive -> 2, active -> 3;
    ### sunday -> 0,monday -> 1 ,tuesday -> 2,wedneday->3,thutsday->4,friday->5,saturday->6;
    
    #append  the data fro csv
    for activity in full_activity_list:
         if activity == 'Walking':
            a,b,c,d = walking;
            i = 0;
            for seg in segment:
                if day == 0:
                    data.append([int(timestamp),date_obj,day,0,0,i,walking[i]]);
                else:
                    data.append([int(timestamp),date_obj,day,1,0,i,walking[i]]);
                i+= 1;
         if activity == 'Driving':
            a,b,c,d = driving;
            i = 0;
            for seg in segment:  
                if day == 0:
                    data.append([int(timestamp),date_obj,day,0,1,i,driving[i]]);
                else:
                    data.append([int(timestamp),date_obj,day,1,1,i,driving[i]]);
                i+= 1;
         if activity == 'Inactive':
            a,b,c,d = inactive;
            i = 0;
            for seg in segment:
                if day == 0:
                    data.append([int(timestamp),date_obj,day,0,2,i,inactive[i]]);
                else:
                    data.append([int(timestamp),date_obj,day,1,2,i,inactive[i]]);
                i+= 1;
         if activity == 'Active':
            a,b,c,d = active;
            i = 0;
            for seg in segment:
                if day == 0:
                    data.append([int(timestamp),date_obj,day,0,3,i,active[i]]);
                else:
                    data.append([int(timestamp),date_obj,day,1,3,i,active[i]]);
                i+= 1;
        
    
    new_df = pd.DataFrame(data, columns=['timestamp', 'date', 'day','day type','activity name','segment','activity count'])
            
        
#to csv
new_df.to_csv('final_user_cleaned_version_0.02.csv');                  
    
            
            
        
        
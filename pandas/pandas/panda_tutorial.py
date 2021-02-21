# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 01:36:03 2020

@author: User
"""

import pandas as pa;

#data load
#csv
poke = pa.read_csv('pokemon_data.csv');
print(poke);
#xcel
poke_xlsx = pa.read_excel('pokemon_data.xlsx');
print(poke_xlsx);

poke_txt = pa.read_csv('pokemon_data.txt',delimiter='\t');
print(poke_txt);
 #load data as wish
print(poke.head(5)); # from top
print(poke.tail(4)); # from bottom

#reading data in pandas
print(poke.columns); #to read cols
#specify a column

print(poke['Name']);
print(poke['Name'][0:5]);
print(poke['Name'][::-1]);#reverse

#read each row
print(poke.head(4));
print(poke.tail(4));
print(f"pokemon is {poke.iloc[0]['Name']}");
print(poke.iloc[0:5]['Type 1']);

# =============================================================================
# for index,row in poke.iterrows():
#     print(index,row);
#     print(index,row['Name']);
# =============================================================================

print(poke.iloc[799][3]);    

print(poke.loc[poke['Type 1'] == 'Fire']);

#sorting
print(poke.describe()); #gives mean,count,min,max etc

print(poke.sort_values('Name', ascending=True));
print(poke.sort_values('Name', ascending=False));

print(poke.sort_values([ 'Generation' , 'Name'] , ascending=[0,1]))

#making changes to data
poke['Total'] = poke['HP'] +poke['Attack'] + poke['Defense']+ poke['Sp. Atk'] + poke['Sp. Def'] + poke['Speed'];
print(poke.head(3));
#drop a column
#method 1
poke = poke.drop(columns=['Total']);
print(poke.head(3));

#method 2
poke['Total'] = poke.iloc[:,4:10].sum(axis=1)#1 for row wise , 0 for column wise
print(poke.head(3));

#get all columns
cols = list(poke.columns);
print(cols);
poke = poke[cols[0:4] + [cols[-1]]+cols[4:12]];
cols = list(poke.columns);
print(cols);
print(poke.head(3));

#save data
poke.to_csv('modified_poke.csv'); #will show with index
poke.to_csv('modified_poke_without_index.csv',index=False);

poke.to_excel('Modified_poke_excel.xlsx',index=False);

poke.to_csv('Modified_poke_text.txt',index=False,sep='\t');

#filter data
filtered_data = poke.loc[(poke['Type 1']== 'Fire') & (poke['Speed'] > 75) & (poke['Legendary'] == True)];
filtered_data.to_csv('filtered_poke_data.csv');
#reset index with previos index being saved
filtered_data.reset_index(drop =True,inplace=True) #drop = True removes previos index,inplace=True makes the changes in the same moment no return type;
print(filtered_data.head(3));
filtered_data.reset_index(drop =True)
filtered_data.to_csv('filtered_poke_data.csv');
poke.to_csv('check_poke_data.csv');

#regex
poke_name_mega = poke.loc[poke['Name'].str.contains('Mega')];
poke_name_mega.reset_index(drop =True)
poke_name_mega.to_csv('poke_name_mega_csv.csv');
print(poke.loc[~poke['Name'].str.contains('Mega')])#~ means not in pandas

import re;
print(poke.loc[poke['Type 1'].str.contains('fire|Grass',flags=re.I,regex=True)]);
poke_regex = poke.loc[(poke['Name'].str.contains('^pi[a-z]*',flags=re.I,regex=True)) & (poke['Speed'] > 50)];
poke_regex_csv = poke_regex.reset_index(drop =True);
poke_regex_csv.to_excel('poke_regex_excel.xlsx');

#conditional changes
poke.loc[poke['Type 1'] == 'Flamer','Type 1'] ='Fire'; 
print(poke);#can be used to set another condition too
#poke.loc[poke['Total']>500 ,['Generation','Legendary']]=['x','y']; multiple conditions

#aggregate using groupby
print(poke.groupby(['Type 1']).mean().sort_values('Speed',ascending=False));
print(poke.groupby(['Type 1']).sum()); # just for use not useful in this case
poke['count'] = 1;

print(poke.groupby('Type 1').count()['count']);
print(poke.groupby('Type 1').sum()['HP']);
print(poke.groupby(['Type 1','Type 2']).count()['count']);
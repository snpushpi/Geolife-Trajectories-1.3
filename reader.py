
import read_geolife
import pandas as pd
import numpy as np
import pptk
def make_list(frame):
    mod_df0 = frame.loc[:,'modified_lat':'modified_lon']
    new_list0lat = mod_df0['modified_lat'].to_list()
    new_list0lon = mod_df0['modified_lon'].to_list()
    l =[]
    length = len(new_list0lat)
    for i in range(length):
        l.append((new_list0lat[i],new_list0lon[i]))
    return l
def sublists(list1, list2):
    subs = []
    for i in range(len(list1)-1):
        for j in range(len(list2)-1):
            if list1[i]==list2[j] and list1[i+1]==list2[j+1]:
                m = i+2
                n = j+2
                while m<len(list1) and n<len(list2) and list1[m]==list2[n]:
                    m += 1
                    n += 1
                subs.append((i,m,j,n,list1[i:m]))
    return subs
def ordered_intersection(list1, list2):
    subls = sublists(list1, list2)
    if len(subls)==0:
        return []
    else:
        max_len = max(len(subl[4]) for subl in subls)
        return [subl for subl in subls if len(subl[4])==max_len]
def ordered_intersection1(list1, list2):
    set_2 = frozenset(list2)
    intersection = [x for x in list1 if x in set_2]
    return intersection
def modifier(a):
    return float(int(a)+float(str(a-int(a))[1:6]))
df = pd.read_pickle('geolife.pkl')
print('joa')
df['modified_lat']=df.lat.apply(modifier)
df['modified_lon']=df.lon.apply(modifier)
print('koa')
df.to_pickle('modified_geolife.pkl')
new_df = []
for i in range(182):
    new_df.append(df[df.user==i])
list_of_coors = []
for elt in new_df:
    list_of_coors.append(make_list(elt))
big_dict = {}
length = len(list_of_coors)
new_check_list = [list_of_coors[i][:2000] for i in range(length)]
new_df_list = []
for j in range(2000):
    new_df_list.append((new_check_list[57][j][0], new_check_list[57][j][1], 5*j, 57, 'Querier himself'))
print(len(new_check_list[47]))
for i in range(length):
    if i!=57:
        for j in range(len(new_check_list[i])):
            if (new_check_list[57][j][0], new_check_list[57][j][1])==(new_check_list[i][j][0], new_check_list[i][j][1]): 
                new_df_list.append((new_check_list[i][j][0], new_check_list[i][j][1], 5*j, i, 'Intersection Happened with Querier'))
            else:
                new_df_list.append((new_check_list[i][j][0], new_check_list[i][j][1], 5*j, i, 'No Intersection happened'))
column_name = ['Latitude', 'Longitude', 'Timestamp', 'User_ID', 'Intersection determiner']
df = pd.DataFrame(columns=column_name, data=new_df_list)
df.to_csv('Main_dataset.csv')

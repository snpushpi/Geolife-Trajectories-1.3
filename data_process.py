import pandas as pd 
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
df['modified_lat']=df.lat.apply(modifier)
df['modified_lon']=df.lon.apply(modifier)
new_df = []
for i in range(182):
    new_df.append(df[df.user==i])
list_of_coors = []
for elt in new_df:
    list_of_coors.append(make_list(elt))
big_dict = {}
length = len(list_of_coors)
new_check_list = [list_of_coors[i][:2000] for i in range(length)]
maximum = 0
border = 0
for i in range(182):
    sum=0
    for j in range(i+1, length):
        inter = ordered_intersection(new_check_list[i], new_check_list[j])
        if len(inter)!=0:
            big_dict[(i,j)]=inter[0]
            sum+=len(big_dict[(i,j)][4])
    if sum>maximum:
        maximum=sum
        border=i
working_dict = {}
for elt in big_dict:
    if elt[0]==border:
        working_dict[elt]=big_dict[elt]
print(big_dict)
print(working_dict)
check_dict={e:len(big_dict[e][4]) for e in big_dict}
print(check_dict)
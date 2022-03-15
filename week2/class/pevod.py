list1=[1,3,8,12,24,1,2,15,16,21]
list2=[1,8,9,21,2,16]
list1.insert(0,[])
list2.insert(0,[])
def pevod(list):
    for i in range(1,len(list)-1):
            if list[i]<list[i+1]: 
                list[0].append(list[i])
            else:
                list[0].append(list[i])
                list.append(list[i+1:])
                del list[2:i]
                del list[1:-1]
                break
    return list
print(pevod(list1))
print(pevod(list2))
Subscription_list1=list(filter(lambda x: x in list1[0],list2[0]))
Subscription_list2=list(filter(lambda x: x in list1[1],list2[1]))
print(Subscription_list1,Subscription_list2)


   






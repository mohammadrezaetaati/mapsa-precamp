from functools import reduce


from functools import reduce
def b_m_m(input1,input2):
    list1=[1]
    list2=[1]
    for i in range(1,input1):
        a=input1/i
        list1.append(a)
    for i in range(1,input2):
        a=input2/i
        list2.append(a)
    set_1=set(list1)& set(list2)
    return max(set_l)

     

print(b_m_m(12,40))

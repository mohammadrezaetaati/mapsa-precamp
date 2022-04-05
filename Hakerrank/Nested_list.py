
from collections import defaultdict
number_student=int(input())
students=[ [input(),float(input())] for s in range(number_student)]
students.sort(key=lambda x:x[1])
second_score=[]
sort_name=[]
for i in range(len(students)-1):
    if students[i][1]<students[i+1][1]:
        second_score.append(students[i+1][0]) 
        second_score.append(students[i+1][1]) 
        break
for l in students:
    if l[1]==second_score[1]:
        sort_name.append(l[0])
sort_name.sort()
print('\n'.join(sort_name))

# for j in range(len(students)-2):
#     i+=1
#     print(students[i])
#     if students[i][1]==students[i+1][1]:
#         second_score.append(students[i+1][0]) 
    
# print(students)      
# # second_score.reverse()
# print('\n'.join(second_score))   
# for i in range():
#     pass
# print(student_sort)

# print(students)
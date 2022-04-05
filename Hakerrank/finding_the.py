number_student=int(input())
dict_student={}
for _ in range(number_student):
    input_user=input().split()
    dict_student[input_user[0]]=input_user[1:]
nam_student_serch=input()
for name,score in dict_student.items():
    if name==nam_student_serch:
        sum_score=list(map(float,score))
        average=sum(sum_score)/len(sum_score)
        print('{:.2f}'.format(average))
   



number_student=int(input('Enter Number Student:'))
dict_student={}
for _ in range(number_student):
    input_user=input('Enter Name and Score :').split()
    dict_student[input_user[0]]=input_user[1:]
nam_student_serch=input('Enter nam Student:')
for name,score in dict_student.items():
    if name==nam_student_serch:
        sum_score=list(map(int,score))
        print(sum(sum_score)/len(sum_score))
    else:
        print(' not is this studen ')




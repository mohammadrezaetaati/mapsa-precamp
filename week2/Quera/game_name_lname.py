
import csv
bank={'esm':[],'famil':[],'keshvar':[],'rang':[],'ashia':[],'ghaza':[]}
name={}
namlist=[]

def ready_up():
    global data
    source=open('esm_famil_data.csv')
    data=csv.reader(source)
    
def add_participant(participant:str,**answers):
    name.update({participant:[]})
    namlist.append(participant)
    for val in answers.values():
        for key,val11 in val.items():
            if val11.isspace() or val11=='':
                bank[key].append(None)
            else:
                bank[key].append(val11)  

def calculate_all():
    c_data=0
    lists=[]
    for key,val in bank.items():
        c=0
        c_data+=1
        for d in data:
            lists.append(d[c_data])
            print(lists)
        for i in val:
            if None  not in val: 
                for r in range(len(val)):
                    if i in lists:
                        if  val.count(i)>1:
                            name[namlist[c]].append(5)
                            
                        elif val.count(i)==1:
                            name[namlist[c]].append(10)       
                    else:
                        name[namlist[c]].append(0)
                c+=1       
        
      
            
   
add_participant(participant = 'salib', answers = {'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
add_participant(participant = 'kianoush', answers = {'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل', 'rang': 'بلوطی', 'ashia': 'بیل', 'ghaza': 'به   پلو'})
add_participant(participant = 'sajjad', answers = {'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما', 'rang': 'بژ', 'ashia': '        ', 'ghaza': 'برنج خورشت'})
add_participant(participant = 'farhad', answers = {'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب', 'rang': 'بژ', 'ashia': 'بیل', 'ghaza': 'باقلوا'})

ready_up()
calculate_all()
print(name)
print(bank)

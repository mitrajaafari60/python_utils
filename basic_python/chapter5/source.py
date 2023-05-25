import csv
from statistics import mean
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name, newline='') as csvfile:
            
            reader = csv.reader(csvfile)
            data = list(reader)

            # Task 1: Calculate and store individual averages
            averages = OrderedDict()
            for row in data:
                name = row[0]
                grades = list(map(int, row[1:]))
                avg = mean(grades)
                averages[name] = avg
            with open(output_file_name, 'a') as file:
                for key, value in averages.items():
                    num= float(value)
                    i_part = int(num)
                    f_part = num - i_part
                    str1= str(f_part)
                    str2=str(i_part)
                    if len(str1)>=2:
                        if len(str1)>=17:
                            str2=str2+"."+str1[2:17]
                        else:
                            str2=str2+"."+str1[2:]
                    file.write(key+","+str2+"\n")
                file.write("\n")
            
def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            averages = OrderedDict()
            for row in data:
                name = row[0]
                grades = list(map(int, row[1:]))
                avg = mean(grades)
                averages[name] = avg
            sorted_averages = OrderedDict(sorted(averages.items(), key=lambda x: x[1]))
            with open(output_file_name, 'a') as file:
                for key, value in sorted_averages.items():
                    num= float(value)
                    i_part = int(num)
                    f_part = num - i_part
                    str1= str(f_part)
                    str2=str(i_part) 
                    if len(str1)>=2:
                        if len(str1)>=17:
                            str2=str2+"."+str1[2:17]
                        else:
                            str2=str2+"."+str1[2:]
                    file.write(key+","+str2+"\n")                   


def calculate_three_best(input_file_name, output_file_name):
     with open(input_file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            averages = OrderedDict()
            for row in data:
                name = row[0]
                grades = list(map(int, row[1:]))
                avg = mean(grades)
                averages[name] = avg
            
            sorted_averages= OrderedDict(sorted(averages.items(), key=lambda x: x[1],reverse=True))
            top_3=OrderedDict()
            count=0
            for key, value in sorted_averages.items():
                if count < 3:
                    top_3[key]=value
                else:
                     break
                count +=1

            with open(output_file_name, 'a') as file:
                for key, value in top_3.items():
                        num= float(value)
                        i_part = int(num)
                        f_part = num - i_part
                        str1= str(f_part)
                        str2=str(i_part)
                        if len(str1)>=2:
                            if len(str1)>=17:
                                str2=str2+"."+str1[2:17]
                            else:
                                str2=str2+"."+str1[2:]
                        file.write(key+","+str2+"\n")
                 


def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            averages = OrderedDict()
            for row in data:
                name = row[0]
                grades = list(map(int, row[1:]))
                avg = mean(grades)
                averages[name] = avg
            sorted_averages = OrderedDict(sorted(averages.items(), key=lambda x: x[1]))
            with open(output_file_name, 'a') as file:
                count=0
                for key, value in sorted_averages.items():
                    if count>=3:
                         break
                    count +=1
                    num= float(value)
                    i_part = int(num)
                    f_part = num - i_part
                    str1= str(f_part)
                    str2=str(i_part)
                    if len(str1)>=2:
                        if len(str1)>=17:
                            str2=str2+"."+str1[2:17]
                        else:
                            str2=str2+"."+str1[2:]
                    
                    file.write(str2+"\n")  


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            averages = OrderedDict()
            for row in data:
                name = row[0]
                grades = list(map(int, row[1:]))
                avg = mean(grades)
                averages[name] = avg
            sorted_averages = OrderedDict(sorted(averages.items(), key=lambda x: x[1]))
            avg_of_averages = mean(sorted_averages.values())
            with open(output_file_name, 'a') as file:
                file.write(str(avg_of_averages)+"\n") 
                

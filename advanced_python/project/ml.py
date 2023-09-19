import sqlite3
from sklearn import tree
import numpy as np

conn = sqlite3.connect('car_data.db')
cursor = conn.cursor()

# Execute a query to fetch data
cursor.execute('SELECT * FROM car_data')
data = cursor.fetchall()

x=[]
y=[]
cars_name_to_number = {} 
# fill data
i=0
for row in data:
    index=0
    if row[0]in cars_name_to_number:
        index= cars_name_to_number[row[0]]
    else:
        i+=1
        cars_name_to_number[row[0]]=i
        index=i


    if row[3] != 'توافقی':
        data=[index,row[1],row[2]]
        #print(row[0],data)
        x.append(data)
        y.append(int(row[3]))
conn.close()

#print(cars_name_to_number)
#print(x,y)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

new_data =['پژو 206 تیپ ۵',1396,166000]
if new_data[0] in cars_name_to_number :
    car_index = cars_name_to_number[new_data[0]]
    check_this = np.array([car_index, new_data[1], new_data[2]]).reshape(1, -1)  # Reshape to 2D array with 3 features
    answer = clf.predict(check_this)
    if len(answer) >=1:
        print(answer[0])
    else:
        print('توافقی')
else:
    print('توافقی')

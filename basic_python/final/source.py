import hashlib
from collections import OrderedDict
import csv

def hash_password_hack(input_file_name, output_file_name):
    hashes = OrderedDict()
    for i in range(1000,9999):
        num= str(i)
        hashed_string = hashlib.sha256(num.encode('utf-8')).hexdigest()
        hashes[hashed_string]=num
    with open(input_file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            results = OrderedDict()
            for row in data:
                name = row[0]
                pass_hash = row[1:]
                results[name] = hashes[pass_hash[0]] 
            
            with open(output_file_name, 'a') as file:
                for key, value in results.items():
                     print(key+","+value)
                     file.write(key+","+value+"\n")
                file.write("\n")


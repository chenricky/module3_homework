# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

count_Jefferson_Charles_Casper_Stockham = 0
count_Jefferson_Diana_DeGette  = 0
county = set()
candidate = set()

# Add a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
file_to_load = os.path.join("election_results.csv")


with open(file_to_load) as csv_file:
   csv_reader = csv.reader(csv_file)

   for line in csv_reader:
       if line[1] == "Jefferson" and line[2] == "Charles Casper Stockham":
           count_Jefferson_Charles_Casper_Stockham =  count_Jefferson_Charles_Casper_Stockham + 1
       elif line[1] == "Jefferson" and line[2] == "Diana DeGette":
           count_Jefferson_Diana_DeGette =  count_Jefferson_Diana_DeGette + 1
    
print("Total votes in Jefferson county voted Chalres is " + str(count_Jefferson_Charles_Casper_Stockham))
print("Total votes in Jefferson county voted Diana is " + str(count_Jefferson_Diana_DeGette))

f = open("result.txt", "a")
f.write("Total votes in Jefferson county voted Chalres is " + str(count_Jefferson_Charles_Casper_Stockham))
f.write("\n")
f.write("Total votes in Jefferson county voted Diana is " + str(count_Jefferson_Diana_DeGette))
f.write("\n")
f.close()

with open(file_to_load) as csv_file:
   csv_reader = csv.reader(csv_file)
   next(csv_reader, None)
   
   for line in csv_reader:
        # if line[1] not in county:
        #     county.append(line[0])
        # if line[2] not in candidate:
        #     candidate.append(line[1])    
        county.add(line[1])
        candidate.add(line[2])

print(county)
print(candidate)   

print("Below the list of county")
for i in county:
    print(i)
    f = open("result.txt", "a")
    f.write(i)
    f.write("\n")
    f.close()
print("\n")
print("Below the list of candidates")
for i in candidate:
    print(i)
    f = open("result.txt", "a")
    f.write(i)
    f.write("\n")
    f.close()


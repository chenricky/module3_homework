# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os


count_Jefferson_Charles_Casper_Stockham = 0
count_Jefferson_Diana_DeGette  = 0
count_Jefferson_Raymon = 0
count_Arapahoe_Raymon = 0
count_Arapahoe_Diana_DeGette = 0
count_Arapahoe_Charles_Casper_Stockham = 0
count_Denver_Charles_Casper_Stockham = 0
count_Denver_Diana_DeGette = 0
count_Denver_Raymon = 0
totalVotes = 0



county = set()
candidate = set()

# Add a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_election_resultss.csv")
file_to_load = os.path.join("election_results.csv")




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

print("\n")
print("the list of county is:")
print(county)
print("\n")
print("the list of candidate is:")
print(candidate) 
  

f = open("election_results.txt", "a")
f.write("\n")
f.write(" ")
f.write("\n")
f.write("Below the list of county:")
f.write("\n")
f.close()
for i in county:
    # print(i)
    f = open("election_results.txt", "a")
    f.write(i)
    f.write("\n")
    f.close()


f = open("election_results.txt", "a")
f.write("\n")
f.write(" ")
f.write("\n")
f.write("Below the list of candidate:")
f.write("\n")
f.close()
for i in candidate:
    # print(i)
    f = open("election_results.txt", "a")
    f.write(i)
    f.write("\n")
    f.close()

with open(file_to_load) as csv_file:
   csv_reader = csv.reader(csv_file)

   for line in csv_reader:
    #    if line[1] == "Jefferson" and line[2] == "Charles Casper Stockham":
       if line[1] == "Jefferson" and "Charles" in line[2]:
           count_Jefferson_Charles_Casper_Stockham =  count_Jefferson_Charles_Casper_Stockham + 1
       elif line[1] == "Jefferson" and line[2] == "Diana DeGette":
           count_Jefferson_Diana_DeGette =  count_Jefferson_Diana_DeGette + 1
       elif line[1] == "Jefferson" and "Raymon" in line[2]:
           count_Jefferson_Raymon =  count_Jefferson_Raymon + 1

       elif line[1] == "Arapahoe" and "Charles" in line[2]:
            count_Arapahoe_Charles_Casper_Stockham =  count_Arapahoe_Charles_Casper_Stockham + 1
       elif line[1] == "Arapahoe" and line[2] == "Diana DeGette":
           count_Arapahoe_Diana_DeGette =  count_Arapahoe_Diana_DeGette + 1
       elif line[1] == "Arapahoe" and "Raymon" in line[2]:
           count_Arapahoen_Raymon =  count_Arapahoe_Raymon + 1
                  
       elif line[1] == "Denver" and "Charles" in line[2]:
            count_Denver_Charles_Casper_Stockham =  count_Denver_Charles_Casper_Stockham + 1
       elif line[1] == "Denver" and line[2] == "Diana DeGette":
           count_Denver_Diana_DeGette =  count_Denver_Diana_DeGette + 1
       elif line[1] == "Denver" and "Raymon" in line[2]:
           count_Denver_Raymon =  count_Denver_Raymon + 1
print("\n")
print("the final election_results for Arapahoe county is:")
print("\n")
print("Total votes in Arapahoe county voted Chalres is " + str(count_Arapahoe_Charles_Casper_Stockham))
print("Total votes in Arapahoe county voted Diana is " + str(count_Arapahoe_Diana_DeGette))
print("Total votes in Arapahoe county voted Raymon is " + str(count_Arapahoe_Raymon))

print("\n")
print("the final election_results for Jefferson county is:")
print("\n")
print("Total votes in Jefferson county voted Chalres is " + str(count_Jefferson_Charles_Casper_Stockham))
print("Total votes in Jefferson county voted Diana is " + str(count_Jefferson_Diana_DeGette))
print("Total votes in Jefferson county voted Raymon is " + str(count_Jefferson_Raymon))

print("\n")
print("the final election_results for Denver county is:")
print("\n")
print("Total votes in Denver county voted Chalres is " + str(count_Denver_Charles_Casper_Stockham))
print("Total votes in Denver county voted Diana is " + str(count_Denver_Diana_DeGette))
print("Total votes in Denver county voted Raymon is " + str(count_Denver_Raymon))

f = open("election_results.txt", "a")
f.write("\n")
f.write(" ")
f.write("\n")
f.write("Total votes in Jefferson county voted Chalres is " + str(count_Jefferson_Charles_Casper_Stockham))
f.write("\n")
f.write("Total votes in Jefferson county voted Diana is " + str(count_Jefferson_Diana_DeGette))
f.write("\n")
f.write("Total votes in Jefferson county voted Raymon is " + str(count_Jefferson_Raymon))
f.write("\n")
f.write(" ")
f.write("\n")
f.write("Total votes in Arapahoe county voted Chalres is " + str(count_Arapahoe_Charles_Casper_Stockham))
f.write("\n")
f.write("Total votes in Arapahoe county voted Diana is " + str(count_Arapahoe_Diana_DeGette))
f.write("\n")
f.write("Total votes in Arapahoe county voted Raymon is " + str(count_Arapahoe_Raymon))
f.write("\n")
f.write(" ")
f.write("\n")
f.write("Total votes in Denver county voted Chalres is " + str(count_Denver_Charles_Casper_Stockham))
f.write("\n")
f.write("Total votes in Denver county voted Diana is " + str(count_Denver_Diana_DeGette))
f.write("\n")
f.write("Total votes in Denver county voted Raymon is " + str(count_Denver_Raymon))
f.write("\n")
f.close()

print("\n")
raymonTotal = count_Denver_Raymon + count_Arapahoe_Raymon + count_Jefferson_Raymon
print("total votes for Raymon are: " + str(raymonTotal))
print("\n")

charlesTotal = count_Denver_Charles_Casper_Stockham + count_Arapahoe_Charles_Casper_Stockham + count_Jefferson_Charles_Casper_Stockham
print("total votes for Charles are: " + str(charlesTotal))
print("\n")

dianaTotal = count_Denver_Diana_DeGette + count_Arapahoe_Diana_DeGette + count_Jefferson_Diana_DeGette
print("total votes for Diana are: " + str(dianaTotal))
print("\n")


totalVotes =  raymonTotal + dianaTotal + charlesTotal


f = open("election_results.txt", "a")
f.write(" ")
f.write("\n")
f.write("total votes for Raymon are: " + str(raymonTotal))
f.write("\n")
f.write("Raymon won: " + "{0:.0%}".format(raymonTotal/totalVotes) )
f.write("\n")

f.write(" ")
f.write("\n")
f.write("total votes for Diana are: " + str(dianaTotal))
f.write("\n")
f.write("Diana won: " + "{0:.0%}".format(dianaTotal/totalVotes) )
f.write("\n")
f.write(" ")
f.write("\n")
f.write("total votes for Charles are: " + str(charlesTotal))
f.write("\n")
f.write("Charles won: " + "{0:.0%}".format( charlesTotal/totalVotes ) )
f.write("\n")

f.close()
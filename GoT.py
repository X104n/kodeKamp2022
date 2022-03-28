import csv
from encodings import utf_8

lst = ["You know nothing", "Winter is coming", "A lannister always pays her debt", "A lannister always pays his debt"]

def read_file(t):
   with open("Game_of_Thrones_Script.csv", "r", encoding="utf8") as f:
    csv_reader = csv.reader(f, delimiter=',')
    print(t+":")
    for line in csv_reader:
        if t.lower() in line[5].lower():
            print( [line[4], line[2], line[1]] )
    print()

f = input("sentence: ")
read_file(f)
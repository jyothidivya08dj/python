import csv
with open("filebook.csv","w",newline="")as file:
    writer=csv.writer(file)

    writer.writerow(["name","age","city"])#header
    writer.writerow(["divya",20,"hyderabad"])
    writer.writerow(["seetha",22,"chennai"])

import csv
with open('./data/currencyrates.csv','r') as file:
    lines = csv.reader(file)
    for line in lines:
        if 'BDT' in line:
            print(line)
            print(f"1 taka = {line[2]} dollar")
            print(f"1 dollar = {line[3]} taka")
            
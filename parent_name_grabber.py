unique = []

with open("companies.txt", "r", encoding="utf-8") as companies:
    for each in companies:
        if "-" not in each:
            unique.append(each)
output = open("parents.txt", "w")

for company in unique:
    output.write(company)
output.close()

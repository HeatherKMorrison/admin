unique = []

with open("raw.txt", "r", encoding="utf-8") as companies:
    for each in companies:
        if each not in unique:
            unique.append(each)
output = open("companies.txt", "w")

alphabetical = sorted(unique)

for company in alphabetical:
    output.write(company)
output.close()

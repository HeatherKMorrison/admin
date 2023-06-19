unique = []
final = []
with open("raw.txt", "r", encoding="utf-8") as companies:
    for each in companies:
        if each not in unique:
            unique.append(each)
output = open("companies.txt", "w")


with open("final.txt", "r", encoding="utf-8") as batch:
    for comp in batch:
        if comp not in unique:
            final.append(comp)

alphabetical = sorted(final)

for company in alphabetical:
    output.write(company)
output.close()

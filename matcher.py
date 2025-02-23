import pandas

def load_column(file_path, column_name):
    
    reader = pandas.read_csv(file_path)
    return set(reader[column_name])

def load_columns(file_path, column_0, column_01):
    reader = pandas.read_csv(file_path)
    return set(reader[[column_0, column_01]])
lead = load_column("leads.csv", "0")
low_lead = {place.lower() for place in lead}
licensed = load_column("thinned.csv", "0") 

low_lic = {name.lower() for name in licensed}

licensed_lead = []

for company in low_lead:
    if(any(lic_company in company for lic_company in low_lic)):
        print(company)

keyset = {" ai ", " ml ", "software"}

for each in keyset:
    for comp in low_lic:
        if each in comp:
            print(comp)
        
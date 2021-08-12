# Add your code here
medical_costs = {}
# Populating medical_costs
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0
medical_costs.update({"Connie":8886.0, "Isaac":16444.0, "Valentina":6420.0})
print(medical_costs)
# Over-write cost for Vinay
medical_costs["Vinay"] = 3325.04
#Calculate the average medical cost of each patient
total_cost = 0
for values in medical_costs.values():
  total_cost += values

average_cost = total_cost/len(medical_costs)
print("Average Insurance Cost: " + str(average_cost))

#List Comprehension to Dictionary
print("-------------------------------------------")
names = list(medical_costs.keys())
ages = [27,24,43,35,52]
#zipped list pair between names and ages
zipped_ages= zip(names, ages)
names_to_ages= {key:value for key,value in zipped_ages}
print(names_to_ages)
# Get Marina's age
marina_age = names_to_ages["Marina"]
print("Marina's age is " + str(marina_age))
print("-------------------------------------------")

# New dictionary for medical records
medical_records = {}
medical_records["Marina"] = {"Age": 27, "Sex":"Female", "BMI":31.1, "Children":2, "Smoker":"Non-smoker", "Insurance_cost":6607.0}

medical_records["Vinay"] = {"Age": 24, "Sex":"Male", "BMI":26.9, "Children":0, "Smoker":"Non-smoker", "Insurance_cost":3225.0}

medical_records["Connie"] = {"Age": 43, "Sex":"Female", "BMI":25.3, "Children":3, "Smoker":"Non-smoker", "Insurance_cost":8886.0}

medical_records["Isaac"] = {"Age": 35, "Sex":"Male", "BMI":20.6, "Children":4, "Smoker":"Smoker", "Insurance_cost":16444.0}

medical_records["Valentina"] = {"Age": 52, "Sex":"Female", "BMI":18.7, "Children":1, "Smoker":"Non-smoker", "Insurance_cost":6420.0}

print(medical_records)
print("-----------------------------------------")

# Print out Connie's records
print("Connie's insurance cost is "+ str(medical_records["Connie"].get("Insurance_cost"))+" dollars.")
print("-----------------------------------------")
# Remove Vinay from medical_records
medical_records.pop("Vinay")

# Iterate through to print value for each record
for name, record in medical_records.items():
  print(name + " is a " + str(record["Age"])+ " year old " + record["Sex"]+" "+ record["Smoker"]+" with a BMI of "+ str(record["BMI"])+ " and insurance cost of "+ str(record["Insurance_cost"]))

#Extra
def update_medical_records(name, age,sex, BMI,children, smoker,insurance):
  new_record = {}
  new_record[name] = {"Age":age,"Sex":sex,"BMI":BMI,"Children":children,"Smoker":smoker,"Insurance_cost":insurance}
  medical_records.update(new_record)
  return medical_records

print(update_medical_records("Steve",19,"male",20.5,1,"Non-smoker",541))
#proof
print(medical_records)







import json
#  load the json file.
with open('file_name.json') as file_json:
  data = json.load(file_json)
#  take the input of weight & height.
count_of_over_weight_people = []
#print(len(data))
for iteam in range(len(data)):
    #data[iteam]['HeightCm']
    #data[iteam]['WeightKg']
    BMI = data[iteam]['WeightKg'] / (data[iteam]['HeightCm'] / 100) 
    # print(BMI)
    if BMI <= 18.5:
        print(f' {BMI:.2f} Malnutrition risk & Underweight')

    elif 18.5 < BMI < 25:
        print(f' {BMI:.2f} Low risk & Normal weight')
    elif 25 < BMI < 30:
        print(f' {BMI:.2f} Enhanced risk & Overweight')
        count_of_over_weight_people.append(BMI)
    elif 30 < BMI < 35:
        print(f' {BMI:.2f} Moderately obese')
        count_of_over_weight_people.append(BMI)
    elif 35 < BMI < 40:
        print(f' {BMI:.2f} Severely obese')
        count_of_over_weight_people.append(BMI)
    elif BMI > 40:
        print(f' {BMI:.2f} Very severely obese')
        count_of_over_weight_people.append(BMI)


print(f'{len(count_of_over_weight_people)} people are over weight.')


# calculate BMI with the formula, BMI(kg/m2) = mass(kg) / height(m)2

# add them in the 3 new columns 

# Count the total number of overweight people using ranges in the column BMI
# Category of Table 1, check this is consistent programmatically and add any
# other observations in the documentation



# Create build, tests to make sure the code is working as expected and this
# can be added to an automation build / test / deployment pipeline
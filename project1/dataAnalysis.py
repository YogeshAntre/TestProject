import csv

def calculate_average_salary(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        
        total_salary = 0
        num_rows = 0
        for row in reader:
            total_salary += int(row['Salary'])
            num_rows += 1
    return total_salary / num_rows if num_rows > 0 else 0

def find_min_max_age(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        ages = [int(row['Age']) for row in reader]
    if len(ages) > 0:
        return min(ages), max(ages)
    else:
        return None, None

def count_rows_with_condition(file_name, age, gender):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        count = sum(1 for row in reader if row['Age'] == str(age) and row['Gender'].lower() == gender.lower())
    return count

data_file = 'data.csv'

# 1. Calculate the average value of salary
average_salary = calculate_average_salary(data_file)
print(f"Average Salary: {average_salary}")

# 2. Find the minimum and maximum values of Age
min_age, max_age = find_min_max_age(data_file)
print(f"Minimum Age: {min_age}")
print(f"Maximum Age: {max_age}")

# 3. Count the number of rows that satisfy the condition
age_condition = 28
gender_condition = 'female'
count = count_rows_with_condition(data_file, age_condition, gender_condition)
print(f"Number of rows with Age {age_condition} and Gender {gender_condition}: {count}")

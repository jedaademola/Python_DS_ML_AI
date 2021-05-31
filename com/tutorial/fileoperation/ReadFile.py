from csv import reader

opened_file = open('sample.csv')
sum_age = 0
read_file = reader(opened_file)
apps_data = list(read_file)
header = apps_data[0]
apps_data = apps_data[1:]

for row in apps_data:
    age = row[1]
    sum_age = sum_age + int(age)


print(apps_data[:5])  # we only print the first 5 rows
print('No of Rows:', len(apps_data))
print('sum of age:', sum_age)

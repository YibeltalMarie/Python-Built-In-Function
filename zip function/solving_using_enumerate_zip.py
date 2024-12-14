#question1:
#Given two lists: one with the names of planets and another withtheir diameters
# and distances from the sun (as tuples of diameter and distance),
# write a script to print each planet with
# its diameter and distance from the sun, along with an index starting from 1.


planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planet_details = [
    (4879, 57.9),    # Mercury: Diameter in km, Distance from Sun in million km
    (12104, 108.2),  # Venus
    (12742, 149.6),  # Earth
    (6779, 227.9),   # Mars
    (139820, 778.5), # Jupiter
    (116460, 1434),  # Saturn
    (50724, 2871),   # Uranus
    (49244, 4495)    # Neptune
]

#solution

for index , (planet,(diameter,distance)) in enumerate(zip(planets,planet_details),start=1):
    print(f"{index}.{planet}: {diameter}km diameter,{distance} million km from sum.")

#Question 2:
#You have three lists: one with the names of employees,another with
#their respective, department names, and a third with their salaries.
# Write a Python script to print each
#employee's name, department, and salary, along with an index starting from 1.

employee_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
departments = ["HR", "Engineering", "Marketing", "Finance", "Sales"]
salaries = [55000, 75000, 60000, 58000, 62000]

combiled_info = zip(employee_names,departments,salaries)

for index,(employee_name,department,salary) in enumerate(combiled_info,start=1):
    print(f"{index}.{employee_name},department:{department},salary:{salary}")



#Question 3:

#Given two lists: one with product names and another with their prices
#at two different stores (as tuples of two prices),
# write a script to calculate the average price for each product and print the product
#names with the calculated average price, including an index starting from 1.

product_names = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch"]
prices_store1 = [1000, 700, 400, 150, 200]
prices_store2 = [950, 680, 390, 160, 210]

combiled_zip = zip(product_names,prices_store1,prices_store2)

for index,(product_name,price1,price2) in enumerate(combiled_zip,start=1):
    average = (price1 + price2)/2
    print(f"{index}:{product_name}, its average price:{average}.")


#Question 4:
# You have two lists: one with the names of sports teams and
# another with their respective scores in a tournament.
# a script to rank the teams based on their scores in descending order
# and print the team names with their scores and ranks

team_names = ["Tigers", "Eagles", "Sharks", "Lions", "Panthers"]
team_scores = [85, 92, 88, 75, 90]


combiled = list(zip(team_names,team_scores))

for i in range (len(combiled)):
    for j in range(i+1,len(combiled)):
        if combiled[i][1] < combiled[j][1]:
            combiled[i], combiled[j] = combiled[j], combiled[i]

for index, (team_name,team_score) in enumerate (combiled,start=1):
    print(f"{index}.{team_name},their score:{team_score}")


#Question 5:


#You have two lists: one with the names of software applications and
# another with their respective version numbers and release dates
# (as tuples of version number and release date).
# Write a script to print each software application with its version number and release date,
# including an index starting from 1


software_names = ["Photoshop", "Excel", "VS Code", "Zoom", "Slack"]
version_numbers = ["2023.1", "16.0", "1.74", "5.8.6", "4.22"]
release_dates = ["2023-02-15", "2023-01-10", "2023-03-05", "2023-04-11", "2023-05-20"]

combiled_sources = zip(software_names,version_numbers,release_dates)

for index, (name,number,date) in enumerate(combiled_sources,start=1):
    print(f"{index}.{name},its version number:{number},its release date:{date}.")
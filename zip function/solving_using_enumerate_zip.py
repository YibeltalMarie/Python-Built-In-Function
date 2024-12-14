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
numbers = [2, -1, 79, 33, -45]
doubled = []

for number in numbers:
    doubled.append(number * 2)
    print(doubled)

#Exercise
grades = [90, 50, 70, 58, 89, 72]

scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)

#Excercise 2
pares = [2, -1, 79, 33, -45]
pares_for_pare = [pare * 2 if pare < 0 else pare * 3 for pare in pares]
print(pares_for_pare)

#Excercise 3
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [riders for riders in heights if riders > 161]
print(can_ride_coaster)

#List comprehension example
#list = [elemnt <opereted on in some way> for elemnt in old_list]
#cubes = [cube**3 for cube in heights]

#Excercise 4
single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
for digits in single_digits: print(digits)
squares.append(digits**2)
print(squares)

cubes = [cube**3 for cube in single_digits]
print(cubes)

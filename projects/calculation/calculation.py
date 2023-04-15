import geometry

radius = float(input("Enter the radius: "))
circle_area = geometry.circle_area(radius)
print(f'The area of a circle with radius {radius} is {circle_area:.2f}')

side = float(input("Enter the side value: "))
square_area = geometry.square_area(side)
print(f'The area of a square with side length {side} is {square_area}')

length = float(input("Enter the value of length: "))
width = float(input("Enter the value of width: "))
rectangle_area = geometry.rectangle_area(length, width)
print(f'The area of a rectangle with length {length} and width {width} is {rectangle_area}')


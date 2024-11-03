#Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3
def cube(side):
    return side*side*side
def divisibility(side):
    if side%3==0:
        return cube(side)
    else:
        return False
side=int(input("Enter side"))
print(divisibility(side))
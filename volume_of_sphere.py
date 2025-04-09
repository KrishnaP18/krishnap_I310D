def calculate_volume_of_sphere(radius):
    constant = 4 / 3
    pi = 3.14
    return constant * pi * pow(radius, 3)

print(int(calculate_volume_of_sphere(30)))
print(int(calculate_volume_of_sphere(40)))

def tempeture_converter(tempeture_list):
    return list(map(lambda t: round(t + 273.15, 2), tempeture_list))

temperatures = [-23, 0, 34, 22, -30, 23]

print(f"temperatures = {temperatures}")
print(f"temperatures = {tempeture_converter(temperatures)}")

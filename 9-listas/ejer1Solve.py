rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
auxMonth=rainfall_mi.split(",")
print(auxMonth)
num_rainy_months=0
for month in auxMonth:
    if float(month)>3.0:
        print(month)
        num_rainy_months+=1
print(num_rainy_months)

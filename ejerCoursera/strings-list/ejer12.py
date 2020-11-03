inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for item in inventory:
    #print(item.split(", "))
    print("The store has {1} {0}, each for {2} USD.".format(*item.split(", ")))

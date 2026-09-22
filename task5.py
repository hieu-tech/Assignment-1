talent = float(input("Enter talents: "))
pound = float(input("Enter pounds: "))
lot = float(input("Enter lots: "))

# convert everything down to lots first
pounds_total = talent * 20 + pound
lots_total = pounds_total * 32 + lot

# now convert lots to grams
grams_total = lots_total * 13.3

kg = int(grams_total // 1000)
g = grams_total - kg * 1000
g = round(g, 2)

print("The weight in modern units:")
print(kg, "kilograms and", g, "grams.")
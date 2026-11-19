bread_weight = float(input("Bread Weight: "))
serving_size = float(input("Serving Size: "))
num_guests = int(input("No. of Guests: "))

breadweight_needed = num_guests * serving_size
loaves_needed = breadweight_needed / bread_weight
print("For", num_guests, "people, you will need", loaves_needed, "loaves of bread;")

yeast = loaves_needed * (1 * (1/2))
salt = loaves_needed * (1 * (1/2))
sugar = loaves_needed * (1 * (1/2))
flour = loaves_needed * (2 * (1/2))
sourdough_starter = loaves_needed * 2
lukewarm_water = loaves_needed * (1/2)

print("")
print("  ", yeast, "teaspoons instant yeast")
print("  ", salt, "teaspoons salt")
print("  ", sugar, "teaspoons sugar")
print("  ", flour, "cups all-purpose flour")
print("  ", sourdough_starter, "cups sourdough starter")
print("  ", lukewarm_water, "cups lukewarm water")
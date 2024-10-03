#CTI110
#P1LAB2 - Receipt
#Norris
#10/1/24

print ("PILAB2")
#PILAB2
num_burgers = 0
num_fries = 0
burger_cost = 4.99
fry_cost = 0.99

print ("Can I take your order?")


num_burgers = int(input("How many burgers?"))

print ("You ordered", num_burgers, "burgers")

num_fries = int(input("How many fries?"))
print ("Okay, that's", num_fries, "french fries.")

burger_total = num_burgers * burger_cost
fry_total = num_fries * fry_cost
meal_total = burger_total + fry_total

print ("-" * 20)
print (num_burgers, "burger\t$", format(burger_total,".2f"))
print (num_burgers, "fry\t$", format(fry_total, ".2f"))
meal_total = burger_total + fry_total

print ("-" * 20)
print ("-" * 20)
print ("Total\t\t$", format(meal_total, ".2f"))

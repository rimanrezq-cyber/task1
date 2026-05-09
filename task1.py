coffee_price = 25
cake_price = 40
water_price = 10
total = (2 * coffee_price) + \
       (1* cake_price) + \
       (3* water_price)

print ("total bill =  ",total)
print("Is total greater than 100?", total > 100)
is_total_greater_than_120 = total > 120
print("Is total greater than 120?", is_total_greater_than_120)
coffee_price += 5
print("New coffee price:", coffee_price)


points = 40
points += 20
points -= 10
points *= 2
print("Final points:", points)
is_customer_VIP = points >= 100
print("Is customer a VIP?", is_customer_VIP)
is_customer_get_free_delivary = total > 150 or is_customer_VIP
print("Does customer get free delivery?", is_customer_get_free_delivary)


result = 10 + 5 * 2
print("Result:", result) # In this case, multiplication is performed before addition, so the result is 10 + (5 * 2) = 10 + 10 = 20.
result = (10 + 5) * 2
print("Result with parentheses:", result) # Parentheses change the order of operations, ensuring that addition is performed before multiplication.


print(True or False and False) # In this case, the expression is evaluated from left to right. The 'or' operator has lower precedence than 'and', so the expression is evaluated as (True or False) and False. The result of (True or False) is True, and then True and False evaluates to False.
print((True or False) and False) # In this case, the expression inside the parentheses is evaluated first, resulting in True. Then, the expression becomes True and False, which evaluates to False.


total_bill = 120
points = 20
premium_member = True
print(total_bill > 150 and points > 50 or premium_member) # In this case, the 'and' operator has higher precedence than 'or', so the expression is evaluated as (total_bill > 150 and points > 50) or premium_member. The result of (total_bill > 150 and points > 50) is False, and then False or premium_member evaluates to True.
print(total_bill > 150 and (points > 50 or premium_member)) # In this case, the expression inside the parentheses is evaluated first. The result of (points > 50 or premium_member) is True, and then the expression becomes total_bill > 150 and True, which evaluates to False.
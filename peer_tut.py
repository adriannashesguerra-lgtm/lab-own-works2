#print statement
print ("my name is nash")

name = "nash"
print ("my name is", name)
print ("my name is" + name)

#input function

#escape sequences
# \n, \t, \\, \
print ("\tHello world")
print ("\nHello world")
print ("\\Hello world")
print ("\"Hello world\"")

#type conversion
#int
var = 2
print (type(var))
#str
var = 2
var = str (var)
print (type(var))
#float
var2 = 5
var2 = float (var2)
print (type(var2))
#float to int
var = 5.94
var = int (var)
print (var)

x = 5
x += 3 #originally x = x+3
y = 3
y -=1

print (x)
print (y)

#Nash - my program is for computing how much and how many tickets did you buy, and if you are eligible for a discount
print ("Welcome to the ticket website")
age = int(input("How old are you? "))
amount = int(input("Enter how many would you like to purchase [price = 150]? "))
price = amount * 150
#calculate
if age <= 12 or age >= 60:
    dsic = 0.20
    fprice = price - (price * dsic)
    discount = "Yes"
else:
    fprice = price
    discount = "No"

#display the receipt
print ("\n===Cinema Ticket Checkout===")
print (f"Age: {age}")
print (f"Tickets: {amount}")
print (f"\n---Receipt---")
print (f"Initial price: {price}")
print (f"Discount applied: {discount}")
print (f"Final price: {fprice}")

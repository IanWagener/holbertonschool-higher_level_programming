'''This program was made by Ian Wagener, 
its purpose is to calculate the price of 
a meal before and after tax'''

#the following line will print "Welcome to the taxes and tip calculator!"
print "Welcome to the taxes and tip calculator!"

print "What is the price before tax?" 
pricebeforetax = float(raw_input(''))

print "What are the taxes? (in %)" 
tax = float(raw_input(''))

print "What do you want to tip? (in %)" 
tip = float(raw_input(''))

total = (pricebeforetax) + (pricebeforetax * tax /100) + (tip/100 * ((pricebeforetax) + (pricebeforetax * tax /100)))
 
print "The price you need to pay is: %f" % (total)
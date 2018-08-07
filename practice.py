#prints out the outcome regardless of users input 
pictures = input("Do you like taking pictures? ")
if pictures[0].casefold() == 'y':
	print('Me too!')
else: 
	print('why not? ')

#asked question waits for result and gives respond 
ice_cream = input('would you like ice-cream? ')
if ice_cream[0].casefold() != 'y':
	print('Then what would you like? ')
else:
	i = input('okay, how namy scoops? ')
	if int(i) <= 2:
		print('Are you sure?')
	else:
  		print('That is to much')

#define function 
def like_chocolate():
	chocolate = int(input('Guess around what age I started eating chocolate: '))
	number = 6
	if chocolate <= int(number) :
		print ('Correct, You guessed it!!')
	else:
		print('Guess again')
like_chocolate()

#for loop
for i in range(5):
	print('yes')

#gives the year the user will be 100 years old with the input they present
def character_input():
	name = input('What is your name? ')
	age = int(input('How old are you? ' ))
	years = int((2018 - age) + 100)
	print (name + ' will be 100 years old on ' + str(years))
character_input()

#evaluates input even or odd
class odd_or_even:
	number = int(input('pick a number: '))
	if(number % 2) == 0 :
		print(str(number) + ' is an even number')
	else:
		print(str(number) + ' is an odd number')

#evaluates divisibility by 2 inputs or number 4
class extra_oddandeven:
	num = int(input('Pick first number: ')) 
	check =int(input('Pick second number: '))
	if num % 4 == 0 and num % 2 == 0:
		print(str(num) + ' is a multiple of four and is an even number')
	elif num % 2 == 0:
		print(str(num) + ' is an even number')
	else:
		print(str(num) + ' is an odd number')
	if num % check == 0:
		print(str(num) + ' is divisible by ' + str(check)) 
	else: 
		print(str(num) + ' is not divisable by ' + str(check))

#outputs all numbers less than 5 the list s provides
class list_less_than_ten:
	m = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	for element in m:
		if element < 5:
			print(element)

#give all the divisors of the input the user provides 
class divisor:
	divisor = int(input('insert a number: '))
	for i in range(1, divisor + 1):
		if divisor % i == 0:
			print(i)
#binary numbers
class bitwise_operations:
	a = 60
	b = 13		
	c = 0
	c = a & b;
	print ("Line 1 - value of c is " , c)

#Repeating string
s = " this is amazing" * 3
print(s)


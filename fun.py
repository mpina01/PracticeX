with open("color.txt", "r+") as f:
     colors = f.readlines()
colors = [x.strip() for x in colors]

print(colors)

number = int(input("number: "))
print (number* 2)

movie = int(input("How many movies: "))
if movie > 5:
 print('stop watching')
else:
 print('keep watching')

for i in range(4):
   print('Grapes')


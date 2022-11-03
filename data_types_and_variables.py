little_mermaid = 3
brother_bear = 5
hercules = 1
x = 3 #dollars
y  = (little_mermaid * x) + (brother_bear * x) + (hercules * x)
print(y) #total sum
# You rented some movies for your kids

h = [10, 6, 4]
google = 400 * h[1]
amazon = 380 * h[-1]
facebook = 350 * h[0]
payment = google + amazon + facebook
print(payment)
#You're working as a contractor for 3 companies

def product_offer(x):
    offer_discount = 0.25
    purchase_total = x * offer_discount
    premimum_membership = True
    if x > 2 or premimum_membership:
        print(purchase_total)
    else:
        return False
assert product_offer(1)
# product offer application
purchase_more_than_two = True
product_not_expired = True
premium_membership = False
discount_eli = product_not_expired and (purchase_more_than_two or premium_membership)
discount_eli
#Review
username = 'codeup'
password = 'notastrongpassword'
password = 'p'

len(password) >= 5
# the password must be at least 5 characters
len(username) <= 20
#the username must be no more than 20 characters
username != password
# the password must not be the same as the username
username.strip()
password.strip()
#bonus neither the username or password can start or end with whitespace
no_whitespace_username = not(username.startswith(' ') or username [-1] == '')
no_whitespace_password = not(password.startswith(' ') or password [-1] == '')
user_and_pass_valid = no_whitespace_username and no_whitespace_password
user_and_pass_valid
#reviewww

#Bonus
#17 exercises
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
output = []
for x in fruits:
    output.append(x.upper())
print(output)

# Exercise 2
output = []
for x in fruits:
    output.append(x.title())
print(output)
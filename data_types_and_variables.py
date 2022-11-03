little_mermaid = 3
brother_bear = 5
hercules = 1
x = 3 #dollars
y  = (little_mermaid * x) + (brother_bear * x) + (hercules * x)
print(y) #total sum
# You rented some movies for your kids

h = [10, 6, 4]
google = 300 * h[0]
amazon = 380 * h[1]
facebook = 350 * h[2]
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

username = 'codeup'
password = 'notastrongpassword'

len(password) >= 5
# the password must be at least 5 characters
len(username) <= 20
#the username must be no more than 20 characters
username == password
# the username must be no more than 20 characters
username.strip()
password.strip()
#bonus neither the username or password can start or end with whitespace
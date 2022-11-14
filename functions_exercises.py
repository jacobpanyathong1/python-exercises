def is_two(x):
    if x == 2 or x == '2':
        return True
    else: 
        return False
#is_two(3)
#is_two(2)
def is_vowel(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        if x == vowel in vowels:
            return True
    else:
        return False
#is_vowel('a')
#is_vowel('z')
def is_consonant(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        if x == vowel in vowels:
            return False
    else:
        return True
#is_consonant('z')
#is_consonant('a')



def acc_str(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in x:
        if i in x[0] != i in vowels:
            return x.capitalize()
    else:
        return x.lower()
                
#acc_str('reagan')
#acc_str('Aagan')

def calculate_tip():
    wild_wings = float(input("Enter total bill: "))
    tip = float(input('Enter tip amount: '))
    total_bill = wild_wings + (wild_wings * tip) 
    return total_bill
#calculate_tip()
# reference:How to Build a Tip Calculator in Python


def apply_discount(x):
    ori_pric = float(input('Enter original price here: '))
    disc = float(input('Enter discount: '))
    total_pric = ori_pric - (ori_pric * disc) 
    print(total_pric, ":is the total price")

    
    

def get_letter_grade():
    grade = float(input('Enter score :'))
    if grade >= 88:
        print('Grade: A')
    elif grade >= 80:
        print('Grade: B')
    elif grade >= 70:
        print('Grade: C')
    elif grade >= 60:
        print('Grade: D')
    else:
        print('Grade: F')
#get_letter_grade()


no_vowels = ""
vowels = ('a', 'e', 'i', 'o', 'u')
def remove_vowels(x):
    for i in x:
        if i in vowels:
            no_vowels = x.replace(i, "")
    return no_vowels
#remove_vowels("clear")
            
# reference stack overflow   

def normalize_name(x):
    x = x.replace("%", '')
    for i in x:
        x = x.lower()
        x = x.strip()
        x = x.replace(' ', '_')
    return x
    
#normalize_name(' % Completed')
#normalize_name(' Name ') 
#normalize_name(' first_name ') 
def cumulative_sum(x):
    lst = []
    p = lst.append(1)
    for i in x:
        if x[0] + x[1]:
            x.append()
#cumulative_sum([1, 1, 1])

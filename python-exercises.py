#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This is the first line
# This is the second line


# 3 + 5
# 

# In[ ]:





# In[4]:


# A demonstration of the type function
type(123)
# The data type is int (for integer)


# In[5]:


type ('hello')
# The data type is str (for string)


# In[6]:


type (True)


# In[7]:


# boolean data type is True or False


# In[8]:


type ('True')


# In[10]:


# Assign a value to a variable
favorite_number = 42
n = favorite_number + 7


# In[11]:


# Print favorite_number
print(favorite_number)


# In[12]:


# Return the data type for favorite_number
type(favorite_number)


# In[13]:


# This is a string named favorite_number
type('favorite_number')


# In[14]:


print(n)


# In[17]:


x = 1
print(x)
x = x + 1
print(x)
x = x * 3 + x
print(x)


# In[18]:


# Boolean value
# True (captial T)
# False (captial F)

# Check equality

True == True



# In[19]:


# Does True equal False?

True == False


# In[20]:


# Checking inequality
# Is True NOT EQUAL to True
True != False


# In[22]:


# NOT operator
# Take the opposite Boolean value
not not not False


# In[23]:


# and operator
# Equal True when both statements are true
True and True


# In[25]:


# Evaluating and operators

# True and True = True
# True and False = False
# False and False = False

False and False
True and False


# In[ ]:


True and False


# In[ ]:


# Evaluating or operators

# True or False = True
# True or True = True
# False or False = False


# In[26]:


True or False

True or True
# In[27]:


False or False


# In[30]:


is_first_of_the_month = False
report_has_been_sent = True

should_process_report = is_first_of_the_month and not report_has_been_sent



print(should_process_report)


# In[31]:


# comparison Operators
# Check equality
1 == 1


# In[33]:


# Check inequality
# Is 1 NOT EQUAL to 0
1 != 0


# In[35]:


# Check if value is greater than another value
# Is 1 greater than 0?
1 > 0


# In[32]:


# Compare two strings
'hello' == 'hello'


# In[36]:


# Check if value is greater than another value
# Is 1 greater than 0?
1 > 0


# In[37]:


# is 5 < 4
5 < 4


# In[39]:


# Greater than or equal to 
5 <= 5


# In[40]:


2 <= 0


# In[41]:


'hello' == 'hello'


# In[42]:


'hello' == 'Hello'


# In[43]:


'hello there!'
''
'123'
"here is a number: 42. It's a nice number"


# In[ ]:


# Strings


# In[48]:


# Manipulate the string
# Not modify the string
# Assign a string to the variable s
s = '      Hello, Codeup!      '
# Apply the string method lower to variable s
s.lower()


# In[49]:


#Apply the string method strip
s.strip()


# In[50]:


# Apply  the string method isdigit
# Returns True if string is a digit
s.isdigit()


# In[51]:


# Apply isdigit to the string '123'
'123'.isdigit()


# In[52]:


'hello'.isdigit()


# In[53]:


s.strip().split(',')


# In[54]:


# Create a list
# Enclosed in square brackets
[1, 2, 3]


# In[55]:


# Contains integers
# Enclosed in square brackets
[1, 2, 3]


# In[56]:


type([1, 2, 3])


# In[57]:


#List with 3 strings
['one', 'two', 'three']


# In[58]:


#Assign the list to a variable
my_list = ['one', 'two', 'three']
print(my_list)


# In[59]:


# A list with 3 lists
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# In[61]:


# Creating lists with list comprehension
[n for n  in range(10)]
# Start with 0
# Do not include 10


# In[62]:


[ n * 2 for n in range (10)]


# In[ ]:


[ n * 2 for n in range (10) if n% 2 ==0]
# Checking for equality
# If n % 2 == 0
# n = 0 Condition is True
# n = 1 Condition is False
# n = 2 Conditino is True
# n = 3 Condition is False (2 * 3) is not included


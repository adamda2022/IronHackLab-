#!/usr/bin/env python
# coding: utf-8

# # Lab -Python Strings Operations

# # Challenge 1 - Combining Strings
# 
# Combining strings is an important skill to acquire. There are multiple ways of combining strings in Python, as well as combining strings with variables. We will explore this in the first challenge. In the cell below, combine the strings in the list and add spaces between the strings (do not add a space after the last string). Insert a period after the last string.

# In[18]:


str_list = ['I', 'am', 'strengthening', 'my', 'programming', 'skills', 'in', 'order', 'to', 'become', 'a', 'great', 'Data','Analyst']
' '.join(str_list) + '.'


# In the cell below, use the list of strings to create a grocery list. Start the list with the string `Grocery list: ` and include a comma and a space between each item except for the last one. Include a period at the end. Only include foods in the list that start with the letter 'b' and ensure all foods are lower case.

# In[21]:


food_list = ['Bananas', 'Chocolate', 'bread', 'diapers', 'Ice Cream', 'Brownie Mix', 'broccoli']
mylist =[]
for x in food_list:
    x=x.lower()
    if x[0]=='b':
        print('Grocery list: '+x+',')
        mylist.append(x)

print('Grocery list: '  + ', '.join(mylist) + '.')


# In the cell below, compute the area of a circle using its radius and insert the radius and the area between `string1` and `string2`. Make sure to include spaces between the variable and the strings. 
# 
# Note: You can use the techniques we have learned so far or use f-strings. F-strings allow us to embed code inside strings. You can read more about f-strings [here](https://www.python.org/dev/peps/pep-0498/).

# In[22]:


import math

string1 = "The area of the circle with radius:"
string2  = "is:"
radius = 4.5
pi = math.pi
area= pi*radius**2

string1 + " " + str(radius) +  " " + string2 + " " + str(area)


# # (Optional) Challenge 2 - Splitting Strings
# 
# We have first looked at combining strings into one long string. There are times where we need to do the opposite and split the string into smaller components for further analysis. 
# 
# In the cell below, split the string into a list of strings using the space delimiter. Count the frequency of each word in the string in a dictionary. Strip the periods, line breaks and commas from the text. Make sure to remove empty strings from your dictionary.

# In[5]:


poem = """Some say the world will end in fire,
Some say in ice.
From what I’ve tasted of desire
I hold with those who favor fire.
But if it had to perish twice,
I think I know enough of hate
To say that for destruction ice
Is also great
And would suffice."""

# Your code here:


# In the cell below, find all the words that appear in the text and do not appear in the blacklist. You must parse the string but can choose any data structure you wish for the words that do not appear in the blacklist. Remove all non letter characters and convert all words to lower case.

# In[6]:


blacklist = ['and', 'as', 'an', 'a', 'the', 'in', 'it']

poem = """I was angry with my friend; 
I told my wrath, my wrath did end.
I was angry with my foe: 
I told it not, my wrath did grow. 

And I waterd it in fears,
Night & morning with my tears: 
And I sunned it with smiles,
And with soft deceitful wiles. 

And it grew both day and night. 
Till it bore an apple bright. 
And my foe beheld it shine,
And he knew that it was mine. 

And into my garden stole, 
When the night had veild the pole; 
In the morning glad I see; 
My foe outstretched beneath the tree."""

# Your code here:


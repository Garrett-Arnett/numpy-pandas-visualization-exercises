#!/usr/bin/env python
# coding: utf-8

# In[77]:


import numpy as np


# In[ ]:


# Use the following code for the questions below:


# In[24]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a


# In[ ]:


# 1. How many negative numbers are there?


# In[9]:


mask = a < 0
len(a[mask])


# In[ ]:


# 2. How many positive numbers are there?


# In[10]:


mask = a > 0
len(a[mask])


# In[ ]:


# 3. How many even positive numbers are there?


# In[22]:


a = a[a % 2 == 0]
a = a[a > 0]
len(a)


# In[25]:


# 4. If you were to add 3 to each data point,
# how many positive numbers would there be?

a1 = a + 3
a1 = a1[a1 > 0]
len(a1)


# In[ ]:


# 5. If you squared each number, what would the new mean and
# standard deviation be?


# In[33]:


a2 = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7]) ** 2
a2 = a2.mean(), a2.std()
a2


# In[ ]:


# 6. A common statistical operation on a dataset is centering.
# This means to adjust the data such that the mean of the data is 0.
# This is done by subtracting the mean from each data point. 
# Center the data set. See this link for more on centering.


# In[34]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
x = a-a.mean()
x 


# In[ ]:


# 7. Calculate the z-score for each data point. 
# Recall that the z-score is given by:


# In[35]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
z = ( a -a.mean()) / a.std()
z


# In[ ]:


# 8. Copy the setup and exercise directions from More Numpy 
# Practice into your numpy_exercises.py and add your solutions.


# In[60]:


import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:


# In[ ]:


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list


# In[40]:


sum_of_a = sum(a)
sum_of_a


# In[ ]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list


# In[41]:


min_of_a = min(a)
min_of_a


# In[ ]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list


# In[42]:


max_of_a = max(a)
max_of_a


# In[ ]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list


# In[43]:


mean_of_a = (sum(a) / len(a))
mean_of_a


# In[ ]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together


# In[46]:


product_of_a = np.prod(a)
product_of_a


# In[ ]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]


# In[62]:


squares_of_a = np.square(a)
squares_of_a


# In[ ]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers


# In[61]:


odds_in_a = a[a % 2 != 0]
odds_in_a


# In[ ]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.


# In[64]:


evens_in_a = a[a % 2 == 0]
evens_in_a


# In[80]:


## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]


# In[67]:


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
sum_of_b


# In[68]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1]) 
min_of_b


# In[69]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b


# In[70]:


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b


# In[71]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
product_of_b


# In[72]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
squares_of_b


# In[73]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
evens_in_b


# In[86]:


# Exercise 9 - print out the shape of the array b.
np.shape(b)


# In[83]:


# Exercise 10 - transpose the array b.
np.transpose(b)


# In[101]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
np.reshape(b,6)


# In[106]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b = np.array ([
    [3, 4, 5],
    [6, 7, 8]]).reshape(6,1)
b


# In[115]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.


# In[118]:


c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


# In[121]:


# Exercise 1 - Find the min, max, sum, and product of c.
cm = c.min(), c.max(), c.sum(), c.prod()
cm


# In[124]:


# Exercise 2 - Determine the standard deviation of c.
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
c = c.std()
c


# In[125]:


# Exercise 3 - Determine the variance of c.
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
cstd = c.std()
cstd


# In[126]:


# Exercise 4 - Print out the shape of the array c
c.shape


# In[127]:


# Exercise 5 - Transpose c and print out transposed result.
c.transpose


# In[128]:


# Exercise 6 - Get the dot product of the array c with c. 
np.dot(c,c)


# In[130]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
c1 = c.transpose()

prod = c * c1

s = prod.sum()

s


# In[132]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
c1 = c.transpose()

p = c * c1

prd = p.prod()

prd


# In[164]:


## Setup 4
d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])


# In[135]:


# Exercise 1 - Find the sine of all the numbers in d
sine = np.sin(d)
sine


# In[139]:


# Exercise 2 - Find the cosine of all the numbers in d
cos = np.cos(d)
cos


# In[140]:


# Exercise 3 - Find the tangent of all the numbers in d
tan = np.tan(d)
tan


# In[145]:


# Exercise 4 - Find all the negative numbers in d
d = d[d < 0]
d


# In[150]:


# Exercise 5 - Find all the positive numbers in d
d1 = d[d > 0]
d1


# In[151]:


# Exercise 6 - Return an array of only the unique numbers in d.
unique = np.unique(d)
unique


# In[152]:


# Exercise 7 - Determine how many unique numbers there are in d
unique = np.unique(d)
len(unique)


# In[153]:


# Exercise 8 - Print out the shape of d.
d.shape


# In[165]:


# Exercise 9 - Transpose and then print out the shape of d.
d = d.transpose()
d.shape


# In[156]:


# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9,2)


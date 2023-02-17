#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd
import numpy as np
from pydataset import data


# In[2]:


''' Make a file named pandas_series.py or pandas_series.ipynb for the following exercises.

Use pandas to create a Series named fruits from the following list:

["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

Use Series attributes and methods to explore your fruits Series.'''


# In[71]:


fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]


# In[4]:


fruits_series = pd.Series(fru
                          its)
fruits_series


# In[5]:


# 1. Determine the number of elements in fruits.


# In[6]:


fruits_series.size


# In[7]:


# 2. Output only the index from fruits.


# In[8]:


fruits_series.index


# In[9]:


# 3. Output only the values from fruits.


# In[10]:


fruits_series.values


# In[11]:


# 4. Confirm the data type of the values in fruits.


# In[12]:


fruits_series.dtype


# In[13]:


# 5. Output only the first five values from fruits. 
# Output the last three values. 
# Output two random values from fruits.


# In[14]:


print(fruits_series.head(5))
print("---------------------- ")
print(fruits_series.tail(2))
print("---------------------- ")
print(fruits_series.sample(2))


# In[15]:


# 6. Run the .describe() on fruits to see what information
# it returns when called on a Series with string values.


# In[16]:


fruits_series.describe()


# In[17]:


# 7. Run the code necessary to produce only the 
# unique string values from fruits.


# In[18]:


fruits_series.unique()


# In[19]:


# 8. Determine how many times each unique string value occurs in fruits.


# In[20]:


fruits_series.nunique()


# In[21]:


# 9. Determine the string value that occurs most frequently in fruits.


# In[22]:


fruits_series.value_counts()[:1]


# In[23]:


# 10. Determine the string value that occurs least frequently in fruits.


# In[24]:


fruits_series.value_counts().sort_values()[:11]


# In[25]:


''' 5. Exercises Part II
Explore more attributes and methods while you continue to work 
with the fruits Series. '''


# In[26]:


# 1. Capitalize all the string values in fruits.

fruits_series.str.capitalize()


# In[27]:


# 2. Count the letter "a" in all the string values (use string vectorization).
fruits_series.str.lower().str.count(r'[a]')


# In[28]:


# 3. Output the number of vowels in each and every string value.


# In[75]:


fv = fruits_series.str.lower().str.count(r'[aeiou]')
fv


# In[ ]:





# In[30]:


num_vowels= pd.DataFrame({'fruits': fruits_series, 'vowel_count': fv})
num_vowels # fancy


# In[31]:


# 4. Write the code to get the longest string value from fruits.


# In[88]:


fruits_series[fruits_series.str.len() >= 16]


# In[ ]:





# In[33]:


# 5. Write the code to get the string values with 5 or more letters in the name.


# In[84]:


fruits_series[fruits_series.str.len() >= 5]


# In[35]:


# 6. Find the fruit(s) containing the letter "o" two or more times.


# In[36]:


fruits_series[fruits_series.apply(lambda row: row.count('o')>=2)]


# In[37]:


# 7. Write the code to get only the string values containing the substring "berry".

fruits_series[fruits_series.str.contains('berry')]


# In[38]:


# 8. Write the code to get only the string values containing the substring "apple".


# In[39]:


fruits_series[fruits_series.str.contains('apple')]


# In[40]:


# 9. Which string value contains the most vowels?

fruits_series[fruits_series.str.lower().str.count(r'[aeiou]').max()]


# In[41]:


''' 7. Exercises Part III
Use pandas to create a Series named letters from the
following string. The easiest way to make this string 
into a Pandas series is to use list to convert each 
individual letter into a single string on a basic Python list.'''


# In[42]:


letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))
letters 


# In[43]:


# 1. Which letter occurs the most frequently in the letters Series?


# In[44]:


print(letters.describe().top)
print(letters.describe().freq)


# In[45]:


# or
letters.value_counts().nlargest(n=1, keep= 'all')


# In[46]:


# 2.Which letter occurs the Least frequently?


# In[47]:


letters.value_counts().nsmallest(n=1, keep= 'all')


# In[48]:


# 3. How many vowels are in the Series?


# In[49]:


lc = letters[letters.str.lower().str.contains(r'[aeiou]')]
lc.count()


# In[50]:


# 4. How many consonants are in the Series?


# In[97]:


letters[~letters.str.lower().str.contains(r'[aeiou]')]


# In[98]:


# or
lcc = letters[letters.str.lower().str.contains(r'[qwrtypsdfghjklzxcvbnm]')]
lcc.count()


# In[52]:


# 5. Create a Series that has all of the same letters but uppercased.


# In[53]:


cap = letters.str.capitalize()
cap


# In[54]:


# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.


# In[99]:


letters.value_counts()[:6].plot.bar()


# In[56]:


''' Use pandas to create a Series named numbers from the 
following list: '''


# In[57]:


numbers1 = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']


# In[58]:


numbers = pd.Series(numbers1)
numbers


# In[59]:


# 1. What is the data type of the numbers Series?


# In[60]:


numbers.dtype


# In[61]:


# 2. How many elements are in the number Series?


# In[62]:


numbers.size


# In[63]:


# 3. Perform the necessary manipulations by accessing 
# Series attributes and methods to convert the 
# numbers Series to a numeric data type.


# In[105]:


numf = numbers.str.replace('$','', regex=False).str.replace(',','', regex=False)
numf = numf.astype('float')
numf


# In[ ]:


# 4. Run the code to discover the maximum value from the Series.


# In[100]:


numf.max()


# In[101]:


# 5. Run the code to discover the minimum value from the Series.


numf.min()


# In[ ]:


# 6. What is the range of the values in the Series?


# In[106]:


range_of_numf = numf.max() - numf.min()
range_of_numf


# In[ ]:


# 7. Bin the data into 4 equally sized intervals or bins and 
# output how many values fall into each bin.


# In[113]:


numf.value_counts(bins=4)


# In[118]:


# 8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.

pd.cut(numf, bins = 4).value_counts().sort_index().plot.barh(title='Value').set(xlabel='count of instances', ylabel='value bins in USD')


# In[ ]:


''' Use pandas to create a Series named exam_scores 
from the following list: '''


# In[67]:


exam_scores = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
es = pd.Series(exam_scores)
es


# In[ ]:


# 1. How many elements are in the exam_scores Series?


# In[ ]:


es.size


# In[ ]:


# 2. Run the code to discover the minimum, the maximum, 
# the mean, and the median scores for the exam_scores Series.


# In[ ]:


print(es.max(), '|', es.min(), '|', es.mean(), '|', es.median())


# In[122]:


#or
es.describe()


# In[ ]:


# 3. Plot the Series in a meaningful way and make sure your
# chart has a title and axis labels.


# In[120]:


import matplotlib.pyplot as plt
es.value_counts(bins = 4).sort_values().sort_index().plot.bar()
plt.title('Test Scores')
plt.xlabel("Freq")
plt.ylabel("Score")


# In[ ]:


# 4. Write the code necessary to implement a curve for your 
# exam_grades Series and save this as curved_grades. 
# Add the necessary points to the highest grade to make it 100, 
# and add the same number of points to every other score in 
# the Series as well.


# In[68]:


curved_grades = es + 4
curved_grades


# In[ ]:


# 5. Use a method to convert each of the numeric values in the 
# curved_grades Series into a categorical value of letter grades.
# For example, 86 should be a 'B' and 95 should be an 'A'. 
# Save this as a Series named letter_grades.


# In[69]:


def score(s):
    if s >= 90:
        return "A"
    elif s >= 80:
        return "B"
    elif s >= 70:
        return "C"
    else:
        return "F"
letter_grades = curved_grades.apply(score)
letter_grades


# In[ ]:


# 6. Plot your new categorical letter_grades Series in a meaninful
# way and include a title and axis labels.


# In[121]:


letter_grades.value_counts().sort_values().sort_index().plot.bar()
plt.title('Test Scores')
plt.xlabel("Letter Grade")
plt.ylabel("Total")


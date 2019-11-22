#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Enter 'x' for exit.");   #question1
print("Enter marks obtained in 5 subjects: ");
mark1 = input();
if mark1 == 'x':
    exit();
else:
    mark1 = int(mark1);
    mark2 = int(input());
    mark3 = int(input());
    mark4 = int(input());
    mark5 = int(input());
    sum = mark1 + mark2 + mark3 + mark4 + mark5;
    average = sum/5;
    if(average>=91 and average<=100):
    	print("Your Grade is A+");
    elif(average>=81 and average<=90):
    	print("Your Grade is A");
    elif(average>=71 and average<=80):
    	print("Your Grade is B+");
    elif(average>=61 and average<=70):
    	print("Your Grade is B");
    elif(average>=51 and average<=60):
    	print("Your Grade is C+");
    elif(average>=41 and average<=50):
    	print("Your Grade is C");
    elif(average>=0 and average<=40):
    	print("Your Grade is F");
    else:
    	print("Strange Grade..!!");


# In[4]:


num = int(input("Enter a number: "))   #question2
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# In[5]:


#question3
str = input("Enter a string: ")


counter = 0
for s in str:
      counter = counter+1
print("Length of the input string is:", counter)


# In[6]:


def sum_list(items):  #q4
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))


# In[7]:


def max_num_in_list( list ):   #q5
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))


# In[ ]:





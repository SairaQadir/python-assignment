#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("1. Addition");   #question1
print("2. Subtraction");
print("3. Multiplication");
print("4. Division");
print("5. Exit");
choice = int(input("Enter your choice: "));
if (choice>=1 and choice<=4):
    print("Enter two numbers: ");
    num1 = int(input());
    num2 = int(input());
    if choice == 1:
    	res = num1 + num2;
    	print("Result = ", res);
    elif choice == 2:
    	res = num1 - num2;
    	print("Result = ", res);
    elif choice == 3:
    	res = num1 * num2;
    	print("Result = ", res);
    else:
    	res = num1 / num2;
    	print("Result = ", res);
elif choice == 5:
    exit();
else:
    print("Wrong input..!!");


# 

# In[6]:


d = {0:10, 1:20}  #q3
print(d)
d.update({2:30})
print(d)

  


# In[7]:


my_dict = {'data1':100,'data2':-54,'data3':247}  #q4
print(sum(my_dict.values()))


# In[9]:


def unique_list(list): #q5
    uniq_list = []
    uniq_set = set()
    for item in list:
       if item not in uniq_set:
            uniq_list.append(item)
            uniq_set.add(item)
    return uniq_list
 
list = [10,20,30,10,10,30,40,50]
print(unique_list(list))


# In[15]:


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}   #q6
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)


# In[ ]:





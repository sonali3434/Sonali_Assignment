#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Ans 14:count number of characters in a string.
a='Happy Happy!!'
b=a.count('p')
print(b)


# In[ ]:


#Ans 15:what are negative indexes and why they are used?
#negative indexing can be done like [-n,.....,-3,-2,-1],it is used to access lastmost elements of given iterable.


# In[3]:


#Ans 16:count occurences of substring in a string.
s1='selly sells seashells by the sea shore'
s2=s1.count('se')
print(s2)


# In[34]:


#Ans 17:count occurence of each word in a given sentence.??


# In[10]:


#Ans 18:to get single string from two given string and swap the first two characters of each string.
p=input('first string:')
q=input('second string:')
r=p.replace(p[0:2],q[0:2])
s=q.replace(q[0:2],p[0:2])
print('new string after swapping first two characters of each string:',r ,end=' ')
print(s)


# In[12]:


#Ans 19:to add ing at the end of a given string(length should be at least three).if the given string already ends with ing then add ly
m=input('enter string:')
if len(m)>=3:
    
    if m.endswith('ing'):
        print(m.replace('ing','ly'))
    else:
        print(m+'ing')
else:
    print(m)


# In[1]:


#Ans 20:to find first appearence of the substring not and poor,if not follows poor replace whole not poor substring with good.
i='he is poor not greedy'
y=i.find('poor')
z=i.find('not')
print(y)
print(z)
if z-y==5:
    print(i.replace('poor not','good'))
else:
    print(i )


# In[15]:


#Ans 21:Write a Python function that takes a list of words and returns the length of the longest one.
a=['heliconia','cacao','orchid']
b=[]
for i in a:
    b.append(len(i))
b.sort()
print('length of longest element in given list is:',b[-1])


# In[19]:


#Ans 22:Write a Python function to reverses a string if its length is a multiple of 4.
a=input('enter a string:')
if len(a)%4==0:
    print('reversed string:',a[-1::-1])
else:
    print('length of given string is not multiple of 4',a)


# In[20]:


#Ans 23:Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length islessthan 2,return instead of the empty string.
a=input('enter a string:')
if len(a)>2:
    print(a[0:2] +a[-2:])
if len(a)==2:
    print(a+a)
if len(a)<2:
    print('')


# In[35]:


#Ans 24: Write a Python function to insert a string in the middle of a string.
a=input('enter a string:')
b=input('enter a string you want to add:')
c=len(a)//2
print('new string:',a[:c]+b+a[c:])


#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[10]:


import pandas as pd 
import numpy as np

df = pd.read_csv("anime.txt")
def genres(colum):
    content = []
    for i in df['genre'].dropna() :
        for j in i.split():
            content.append(j.strip(','))
    return content
def bestAnimes(typ , aORm):
    if aORm == 'a':
        
        x = df[(df['genre'].fillna('0').str.contains(typ)) & (df['rating'] > avg )& (df['type'] == 'TV')]['name'] # tv == anime
        
    else:
        x = df[(df['genre'].fillna('0').str.contains(typ) )& (df['type'] == 'Movie')& (df['rating'] > avg )]['name']
    names = ''
    count = 1
    for i in x.head():
        names = names+str(count)+'-'+ i+ ' , ' 
        count += 1
        
    return names
avg = df['rating'].dropna().mean()    #average


    
userInput1 = ''
cols = df.columns
cols =list(df.columns)

names= ''
content = genres(cols) #check the genres
 
while userInput1 != 'q' : #sential value
    userInput1 = input("are you looking for a good (anime) or a (moive)? Q to quit").lower()
    if userInput1 == 'anime':
        userInput2 = input("Enter the anime's type: (e.g drama)").capitalize() #to match the name
     
        if userInput2 in content :
    
            names = bestAnimes(userInput2, 'a')
            break
        else:
            print("NOT A TYPE")
    elif userInput1 == 'movie':
            userInput2 = input("Enter the movie's type(e.g Drama)").capitalize()
            if userInput2 in content :
                names = bestAnime(userInput2, 'm')
                break

if len(names) != 0:
    print("Best", userInput2 , userInput1 +'s :', names )
    


# In[8]:





# In[ ]:





# In[ ]:





# In[ ]:





# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 15:40:07 2016

@author: Sonix
"""

lst=[]
fp=open("abc_terrorist_news.txt","r")
lst=fp.readlines()
#print lst

wrd_lst=[]
new_lst=[]
for i in lst:
    wrd_lst.append(i.split(' '))

for i in wrd_lst:
    if (len(i)>8 and (len(i[0])<20 and len(i[1])<20 and len(i[2]))):
        #print i
        new_lst.append(i)
        
s=''
for i in new_lst:
    for j in range(0,len(i)):
            s=''
            for k in i[j]:
                if(k.isalpha()):
                    s=s+k
                else:
                    break
            i[j]=s



fp1=open("nltk_dictionary words.txt","r")
eng=fp1.readlines()

for i in range(0,len(eng)):
    s=''
    for j in range(0,len(eng[i])-1):
        s=s+eng[i][j]
    eng[i]=s

hsh={}

for i in eng:
    if (len(i)>1):
        hsh[i]=''

final=[]
k=0
for i in new_lst:
    c=0
    for j in i:
        j=j.lower()
        try:
            hsh[j]
            c=c+1
        except:
            continue
    if (c>3):
        final.append(i)
        
        
fp2=open("NewTerroristData.txt","w")
s=''
for i in final:
    s=s+' '.join(i)
    s=s+'\n\n'     
       
fp2.write(s)       

fp1.close()
fp2.close()
fp.close()




        


    
  
        
        
    
    
import sys
import json
import math
import re, string
import nltk
from collections import defaultdict

model=sys.argv[1]
pos=sys.argv[2]
output=sys.argv[3]
#output=sys.argv[2]

pos_tag=json.load(open(pos))
dic_all=json.load(open(model))
dic_its=dic_all['its']
dic_your=dic_all['your']
dic_their=dic_all['their']
dic_lose=dic_all['lose']
dic_too=dic_all['too']

n_its1=dic_all['n_its1']
n_its2=dic_all['n_its2']
n_your1=dic_all['n_your1']
n_your2=dic_all['n_your2']
n_their1=dic_all['n_their1']
n_their2=dic_all['n_their2']
n_lose1=dic_all['n_lose1']
n_lose2=dic_all['n_lose2']
n_too1=dic_all['n_too1']
n_too2=dic_all['n_too2']

p_its1=math.log(n_its1/float(n_its1+n_its2))
p_its2=1-p_its1
p_your1=math.log(n_your1/float(n_your1+n_your2))
p_your2=1-p_your1
p_their1=math.log(n_their1/float(n_their1+n_their2))
p_their2=1-p_their1
p_lose1=math.log(n_lose1/float(n_lose1+n_lose2))
p_lose2=1-p_lose1
p_too1=math.log(n_too1/float(n_too1+n_too2))
p_too2=1-p_too1


class1=["it's","It's","you're","You're","they're","They're","loose","Loose","to","To"]
class2=["its","Its","your","Your","their","Their","lose","Lose","too","Too"]
Its1=["it's","It's"]
Its2=["its","Its"]

Your1=["you're","You're"]
Your2=["your","Your"]

Their1=["they're","They're"]
Their2=["their","Their"]

Lose1=["loose","Loose"]
Lose2=["lose","Lose"]

Too1=["to","To"]
Too2=["too","Too"]

whole_class=["it's","It's","its","Its","you're","You're","they're","They're","loose","Loose","to","To","your","Your","their","Their","lose","Lose","too","Too"]

line_ID=0
line_j=0
with open(output,'r') as f:
     f1=f.read().splitlines()
     for line in f1:
       line_ID+=1
       if line =='':
            sys.stdout.write('\n')
       if line !='':

         new_line='. '+line+' .'
         words=new_line.split()

         for i in range(1,len(words)-1):
             word=words[i]

             whole_r=0
             its_r=0
             your_r=0
             their_r=0
             its_index=0
             your_index=0
             their_index=0
             lose_index=0
             too_index=0

             if word in whole_class:
                whole_r=1

             if whole_r!=1:
                if re.search("It's$",word)>0 or re.search("Its$",word)>0:
                   its_r=1
                if re.search("You're$",word)>0 or re.search("Your$",word)>0:
                   your_r=1
                if re.search("They're$",word)>0 or re.search("Their$",word)>0:
                   their_r=1

             if whole_r+its_r+your_r+their_r>0: 
                tag=pos_tag[str(line_ID)]

                #tag=nltk.pos_tag(words)

                pw='p:'+words[i-1]
                nw='n:'+words[i+1]
                pt='pt:'+tag[i-1][1]
                nt='nt:'+tag[i+1][1]

                buffer_dic=defaultdict()
                buffer_dic[pw]=0
                buffer_dic[nw]=0
                buffer_dic[pt]=0
                buffer_dic[nt]=0

## for its
                if whole_r+its_r>0:
                   j0_its=p_its1       # it's 
                   j1_its=p_its2       # its
                   if word in Its1 or word in Its2:

                      if word in Its1:
                         its_index=Its1.index(word)
                      if word in Its2:
                         its_index=Its2.index(word)

                      for b_i in buffer_dic:
                          if b_i in dic_its:
                             j0_its+=math.log(dic_its[b_i][0]/float(n_its1))
                             j1_its+=math.log(dic_its[b_i][1]/float(n_its2))

                      if math.log(2.5)+j1_its>j0_its:
                          word=Its2[its_index]
                      else:
                          word=Its1[its_index]  


                   if its_r==1:
                      for b_i in buffer_dic:
                          if b_i in dic_its:
                             j0_its+=math.log(dic_its[b_i][0]/float(n_its1))
                             j1_its+=math.log(dic_its[b_i][1]/float(n_its2))

                      if math.log(0.1)+j1_its>j0_its:
                          word=Its2[1]
                          word='"'+word
                      else:
                          word=Its1[1]  
                          word='"'+word
                              
                 #  print(j0_its,j1_its)
## for your
                if whole_r+your_r>0:
                   j0_your=p_your1       # you're
                   j1_your=p_your2       # your
                   if word in Your1 or word in Your2:
                      if word in Your1:
                         your_index=Your1.index(word)
                      if word in Your2:
                         your_index=Your2.index(word)

                      for b_i in buffer_dic:
                          if b_i in dic_your:
                             j0_your+=math.log(dic_your[b_i][0]/float(n_your1))
                             j1_your+=math.log(dic_your[b_i][1]/float(n_your2))

                      if math.log(0.7)+j1_your>j0_your:
                          word=Your2[your_index]
                      else:
                          word=Your1[your_index]  

                   if your_r==1:
                      for b_i in buffer_dic:
                          if b_i in dic_your:
                             j0_your+=math.log(dic_your[b_i][0]/float(n_your1))
                             j1_your+=math.log(dic_your[b_i][1]/float(n_your2))

                      if math.log(0.8)+j1_your>j0_your:
                          word=Your2[1]
                          word='"'+word
                      else:
                          word=Your1[1]  
                          word='"'+word 

                  # print(j0_your,j1_your)
## for their
                if whole_r+their_r>0:
                   j0_their=p_their1       # it's 
                   j1_their=p_their2       # its
                   if word in Their1 or word in Their2:
                      if word in Their1:
                         their_index=Their1.index(word)
                      if word in Their2:
                         their_index=Their2.index(word)

                      for b_i in buffer_dic:
                          if b_i in dic_their:
                             j0_their+=math.log(dic_their[b_i][0]/float(n_their1))
                             j1_their+=math.log(dic_their[b_i][1]/float(n_their2))

                      if math.log(0.7)+j1_their>j0_their:
                          word=Their2[their_index]
                      else:
                          word=Their1[their_index]  

                   if their_r==1:
                      for b_i in buffer_dic:
                          if b_i in dic_their:
                             j0_their+=math.log(dic_their[b_i][0]/float(n_their1))
                             j1_their+=math.log(dic_their[b_i][1]/float(n_their2))

                      if math.log(0.01)+j1_their>j0_their:
                          word=Their2[1]
                          word='"'+word
                      else:
                          word=Their1[1]  
                          word='"'+word
                  # print(j0_their,j1_their)
## for lose
                if whole_r>0:
                   j0_lose=p_lose1       # it's 
                   j1_lose=p_lose2       # its
                   if word in Lose1 or word in Lose2:

                      if word in Lose1:
                         lose_index=Lose1.index(word)
                      if word in Lose2:
                         lose_index=Lose2.index(word)

                      for b_i in buffer_dic:
                          if b_i in dic_lose:
                             j0_lose+=math.log(dic_lose[b_i][0]/float(n_lose1))
                             j1_lose+=math.log(dic_lose[b_i][1]/float(n_lose2))

                      if math.log(0.5)+j1_lose>j0_lose:# 0.06
                          word=Lose2[lose_index]
                      else:
                          word=Lose1[lose_index]  

                   #print(j0_lose,j1_lose) 
## for too
                if whole_r>0:
                   j0_too=p_too1       # it's 
                   j1_too=p_too2       # its
                   if word in Too1 or word in Too2:

                      if word in Too1:
                         too_index=Too1.index(word)
                      if word in Too2:
                         too_index=Too2.index(word)

                      for b_i in buffer_dic:

                          if b_i in dic_too:
                             j0_too+=math.log(dic_too[b_i][0]/float(n_too1))
                             j1_too+=math.log(dic_too[b_i][1]/float(n_too2))

                      if math.log(0.000155)+j1_too>j0_too:#0.000155
                         word=Too2[too_index]
                      else:
                         word=Too1[too_index] 
         

             sys.stdout.write(word)
             sys.stdout.write(' ')
             if i==len(words)-2:
                sys.stdout.write('\n')

## 456 dev error

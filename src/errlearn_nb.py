import sys
import json
import re, string
import nltk
from collections import defaultdict

input=sys.argv[1]
pos=sys.argv[2]
model=sys.argv[3]

dic_its = defaultdict(float)
dic_your = defaultdict(float)
dic_their = defaultdict(float)
dic_lose = defaultdict(float)
dic_too = defaultdict(float)


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

pos_tag=json.load(open(pos))

line_ID=0
dic_all=defaultdict()

n_its1=0
n_its2=0
n_your1=0
n_your2=0
n_their1=0
n_their2=0
n_too1=0
n_too2=0
n_lose1=0
n_lose2=0
with open(input,'r') as f:
    for line in f:
      line_ID+=1
      if line!='':
        new_line='. '+line+' .'
        words=new_line.split()

        for i in range(1,len(words)-1):
            word=words[i]

            if word in whole_class:
               tag=pos_tag[str(line_ID)]
               if word in Its1 or word in Its2:
                  if word in Its1:
                     k=0
                     n_its1+=1
                  if word in Its2:
                     k=1
                     n_its2+=1

                  pw='p:'+words[i-1]
                  nw='n:'+words[i+1]
                  pt='pt:'+tag[i-1][1]
                  nt='nt:'+tag[i+1][1]

                  buffer_dic=defaultdict()
                  buffer_dic[pw]=0
                  buffer_dic[nw]=0
                  buffer_dic[pt]=0
                  buffer_dic[nt]=0

                  for b_i in buffer_dic:
                      if b_i not in dic_its:
                         dic_its[b_i]=[0]*2
                         dic_its[b_i][k]=1   # rank is it's:0 its:1

                      if b_i in dic_its:
                         dic_its[b_i][k]+=1

## for your
               if word in Your1 or word in Your2:
                  if word in Your1:
                     k=0
                     n_your1+=1
                  if word in Your2:
                     k=1
                     n_your2+=1

                  pw='p:'+words[i-1]
                  nw='n:'+words[i+1]
                  pt='pt:'+tag[i-1][1]
                  nt='nt:'+tag[i+1][1]

                  buffer_dic=defaultdict()
                  buffer_dic[pw]=0
                  buffer_dic[nw]=0
                  buffer_dic[pt]=0
                  buffer_dic[nt]=0

                  for b_i in buffer_dic:
                      if b_i not in dic_your:
                         dic_your[b_i]=[0]*2
                         dic_your[b_i][k]=1   # rank is it's:0 its:1

                      if b_i in dic_your:
                         dic_your[b_i][k]+=1

## for their

               if word in Their1 or word in Their2:
                  if word in Their1:
                     k=0
                     n_their1+=1
                  if word in Their2:
                     k=1
                     n_their2+=1

                  pw='p:'+words[i-1]
                  nw='n:'+words[i+1]
                  pt='pt:'+tag[i-1][1]
                  nt='nt:'+tag[i+1][1]

                  buffer_dic=defaultdict()
                  buffer_dic[pw]=0
                  buffer_dic[nw]=0
                  buffer_dic[pt]=0
                  buffer_dic[nt]=0

                  for b_i in buffer_dic:
                      if b_i not in dic_their:
                         dic_their[b_i]=[0]*2
                         dic_their[b_i][k]=1   # rank is it's:0 its:1

                      if b_i in dic_their:
                         dic_their[b_i][k]+=1

## for lose
               if word in Lose1 or word in Lose2:
                  if word in Lose1:
                     k=0
                     n_lose1+=1
                  if word in Lose2:
                     k=1
                     n_lose2+=1

                  pw='p:'+words[i-1]
                  nw='n:'+words[i+1]
                  pt='pt:'+tag[i-1][1]
                  nt='nt:'+tag[i+1][1]

                  buffer_dic=defaultdict()
                  buffer_dic[pw]=0
                  buffer_dic[nw]=0
                  buffer_dic[pt]=0
                  buffer_dic[nt]=0

                  for b_i in buffer_dic:
                      if b_i not in dic_lose:
                         dic_lose[b_i]=[0]*2
                         dic_lose[b_i][k]=1   # rank is it's:0 its:1

                      if b_i in dic_lose:
                         dic_lose[b_i][k]+=1

## for too
               if word in Too1 or word in Too2:
                  if word in Too1:
                     k=0
                     n_too1+=1
                  if word in Too2:
                     k=1
                     n_too2+=1

                  pw='p:'+words[i-1]
                  nw='n:'+words[i+1]
                  pt='pt:'+tag[i-1][1]
                  nt='nt:'+tag[i+1][1]

                  buffer_dic=defaultdict()
                  buffer_dic[pw]=0
                  buffer_dic[nw]=0
                  buffer_dic[pt]=0
                  buffer_dic[nt]=0

                  for b_i in buffer_dic:
                      if b_i not in dic_too:
                         dic_too[b_i]=[0]*2
                         dic_too[b_i][k]=1   # rank is it's:0 its:1

                      if b_i in dic_too:
                         dic_too[b_i][k]+=1
dic_all['its']=dic_its
dic_all['your']=dic_your
dic_all['their']=dic_their
dic_all['lose']=dic_lose
dic_all['too']=dic_too


for d in dic_all:
    dic=dic_all[d]
    for w in dic:
       for i in range(2):
           if dic[w][i]==0:
              dic[w][i]=1
              for j in range(2):
                  if j!=i:
                     dic[w][j]+=1

dic_all['n_its1']=n_its1
dic_all['n_its2']=n_its2
dic_all['n_your1']=n_your1
dic_all['n_your2']=n_your2
dic_all['n_their1']=n_their1
dic_all['n_their2']=n_their2
dic_all['n_lose1']=n_lose1
dic_all['n_lose2']=n_lose2
dic_all['n_too1']=n_too1
dic_all['n_too2']=n_too2

json.dump(dic_all,open(model,'w')) 
     

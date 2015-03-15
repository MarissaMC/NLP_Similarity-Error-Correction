import sys
import json
import pickle
import re, string
import nltk
from nltk.tag.simplify import simplify_wsj_tag
from collections import defaultdict

input=sys.argv[1]
output=sys.argv[2]

whole_class=["it's","It's","its","Its","you're","You're","they're","They're","loose","Loose","to","To","your","Your","their","Their","lose","Lose","too","Too"]
dic=defaultdict()

line_ID=20411

with open(input,'r') as f:
     f1=f.read().splitlines()
     for line in f1:
         line_ID+=1
         if line !='':
            judge=0
            new_line='. '+line+' .'
            for word in whole_class:
            	if line.find(word)>=0:
            	   judge=1
            if judge==1:
               words=new_line.split()
               tagged_sent=nltk.pos_tag(words)
               tag_s=[(word, simplify_wsj_tag(tag)) for word, tag in tagged_sent]
               dic[line_ID]=tag_s

json.dump(dic,open(output,'w')) 
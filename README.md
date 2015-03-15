CSCI 544 Homework 3
=====================
This is an instruction for CSCI544 Homework 3(http://appliednlp.bitbucket.org/hw3/index.html)

The code written for Python 2.7
Open source used: NLTK 


Description
-----------------
The goal is to develop an approach for detecting and correcting errors with similar sounds but different meaning:

           it's vs its
           you're vs your
           they're vs their
           loose vs lose
           to vs too

For example, given a file containing:

Then pour water or light oil from a graduated beaker into the chamber to fill the chamber too its gasket surface. 
The horses moved at a clump; they were no more on parade than was they're driver; one fork of the road was as good as another. 


I will give a corrected text file containing:

Then pour water or light oil from a graduated beaker into the chamber to fill the chamber to its gasket surface.
The horses moved at a clump; they were no more on parade than was their driver; one fork of the road was as good as another.


Because different pair of words have quite different language environment, I deal with the above 5 pairs of words separately. The features I use are: 
   
           p:prev_word   pt:prev_POS   n:next_word   nt:next_POS

And I choose Naive Bayes algorithm to run the model.

Data Source
-----------------
The dataset I used as train dataset is from NLTK gutenberg, which contains several novels. 

Usage
-----------------
In the src directory, there are four files:

    errlearn_nb.py  # to train data
    errclassify_nb.py # to classify test data
    pos.py  # to get pos file

The training program, errlearn_nb.py, run as follows:

    python errlearn_nb.py TRAININGFILE POSFILE MODEL

where TRAININGFILE is the input file with correct words. For example, a small training file might contain these lines:

Her mother had died too long ago for her to have more than an indistinct remembrance of her caresses.

POSFILE contains pos tag of TRAININGFILE, run as follows:

    python pos.py TRAININGFILE POSFILE

and MODEL is the output file containing the model.

The errclassify_nb.py program runs as follows:

    python errclassify.py MODEL POSFILE TESTINGFILE > OUTPUT

where MODEL is the model generated by errlearn_nb.py and POSFILE is the pos tag file of TESTINGFILE.
In the OUTPUT file there are text corrected.


Accuracy
-----------------
Accuracy of dev dataset is as below:

Total instance(lines):100000

Total lines need to be corrected: 6453

Total lines corrected: 5997

Total lines not corrected: 456
(of the 456, 260 lines are wrong at classifying "too" and "to")

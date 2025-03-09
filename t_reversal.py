import json
import time
start1 = time.time()



with open("paras_1000.txt", "r") as f:
    data = f.read()

# number of lines
lines = data.split("\n")


# function that checks number of words in a line
def word_count(sentence):
    words = sentence.split(" ")
    num_words = len(words)
    return num_words # Number of words in each line

# array of arrays of number of line and number of words

def get_pos_and_words_num(sent_arr):
    arr = []
    for i in sent_arr:
        arr.append([sent_arr.index(i)+1,word_count(i)]) 
        
    return arr

def rev_lines(lines_arr): # reverses the letters of a line
    rev_lines_arr = []
    for line in lines_arr:
        rev_lines_arr.append(str(lines_arr.index(line)+1) + ". " + line[::-1])
    return rev_lines_arr

def rev_line(arr): # reverse lines 
    rev_arr = arr[::-1]
    return rev_arr

# print(get_pos_and_words_num(lines))
print(rev_line(rev_lines(lines)))

with open("newfile.txt",'w') as output:
    for line in rev_line(rev_lines(lines)):
        output.write(line +"\n")





end1 = time.time()
print("Time taken: ", end1 - start1)
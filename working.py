# This is a triple reversal program in python. It takes a file of unknown number of lines, reverses the characters of each word, the order of the words in a line and the order of the lines in the file.
# It then writes the transformed content into a new file.

import time
start = time.time()

def read_char(line1,file,line2):
    line1 = file.read(1)  # read the first immediate Character
    line1 = line1.decode('utf-8').strip("\r") # convert binary to str and remove carriage characters
    line2 = line2 + line1 # update the final line: line2
    return [line1,line2] # results

old_f_name = input("Type the path of old file: ") # input for path original file with content
new_f_name = input("Type the path of new file: ") # input for to be path of output file with content 

try: 
    with open(old_f_name,'rb') as r_file: # open original file for reading in binary mode
        with open(new_f_name,'w') as w_file: # create new file for writing
            num_lines = len(r_file.readlines()) # get total number of lines of original file
            r_file.seek(0,2) # move cursor to last position of original file
            last_pos = r_file.tell() # Get value of last position the original file

            i = 0 # reference to track position of cursor
            while r_file.tell() != 0 and last_pos>i: # iterates line by line and stops when cursor is at position zero

            # get line
                line = ''
                line_f = "" # holds a line
                line_f = str(num_lines) + ". "  # initialise start of a reversed line with its original number
                while (not line.startswith("\n")): # iterates letter by letter of a line
                    r_file.seek(last_pos-i,0) # put cursor to the (last_pos-i)th position
                    if r_file.tell() == 0: # check if cursor is at the beginning of the file
                        [line,line_f] = read_char(line,r_file,line_f)
                        break
                    [line,line_f] = read_char(line,r_file,line_f)
                    
                    i+=1 # update i
                
                num_lines-=1 # update reference to next line

                w_file.write(line_f) # at the end of the loop, write line_f to output file

except FileNotFoundError:
    print("Oops!  That was not a valid file.  Try again...")

except:
    print("There was an error")              

end = time.time()
print("Run time:", end-start)
print(start,end)


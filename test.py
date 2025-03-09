# with open('text.txt','rb') as r_file:
#     r_file.seek(0,2)
#     last_pos = r_file.tell()
#     i = 1



#     line_f = ''
#     while (("\n" not in line_f)):
        
#         r_file.seek(last_pos-i,0)
#         line = r_file.read(1)
#         line = line.decode('utf-8')
#         line_f = line_f + line
#         i+=1

#     print(line_f.strip('\n'))

# with open("paras_1000.txt",'rb') as f:
#     print(len(f.readlines()))





# import time
# start = time.time()


# def read_char(line1,file,line2):
#     line1 = file.read(1)  
#     line1 = line1.decode('utf-8').strip("\r") 
#     line2 = line2 + line1
#     return [line1,line2]

# old_f_name = input("Type the path of old file: ") 
# new_f_name = input("Type the path of new file: ") 

# with open(old_f_name,'rb') as r_file:
#     with open(new_f_name,'w') as w_file:
#         num_lines = len(r_file.readlines()) 
#         r_file.seek(0,2) 
#         last_pos = r_file.tell() 

#         i = 0 
#         while r_file.tell() != 0 and last_pos>i: 
#             line = ''
#             line_f = "" 
#             line_f = str(num_lines) + ". "  
#             while (not line.startswith("\n")): 
#                 r_file.seek(last_pos-i,0) 
#                 if r_file.tell() == 0: 
#                     [line,line_f] = read_char(line,r_file,line_f)
#                     break
#                 [line,line_f] = read_char(line,r_file,line_f)
                
#                 i+=1 
            
#             num_lines-=1 

#             w_file.write(line_f)          

# end = time.time()
# print("Run time:", end-start)
def lines_gen():
    # documentation
    num_lines = input("Enter number of lines: ")

    with open(num_lines + "_lines.txt", 'w') as f:
        i = 0
        lines = [
    'God bless our homeland Ghana',
    'And make our nation great and strong',
    'Bold to defend for ever',
    'The cause of Freedom and of Right',
    'Fill our hearts with true humility',
    'Make us cherish fearless honesty',
    'And help us to resist oppressors rule',
    'With all our will and might for evermore',
    '',
    'And help us to resist oppressors rule']
        
        while i < int(num_lines): 
            for line in lines:
                f.write(line + '\n')
            i+=10


# lines_gen()

import time
s = time.time()
print("Hi")
e = time.time()
print(e-s,e,s)
# --------------
#Code starts here

def palindrome_check(num):
  num=str(num)
  return (num[::-1]==num)

#Function to find the smallest palindrome
def palindrome(num):
    while(1):
        num=num+1
        if palindrome_check(num):
            return num


# --------------
#Code starts here
def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)



# --------------
#Importing header files
from math import sqrt

#Code starts here

#Function to check for perfect square 
def is_perfect_square(x):
 
    s = sqrt(x)
    return (int(s)*int(s) == x) 
 
#Function to check for fibonacci number
def check_fib(num):
    if is_perfect_square((5*num*num) + 4) or is_perfect_square((5*num*num) - 4): #Formula for checking fibonacci number
        return True
    
    return False     

#Code ends here


# --------------
def compress(word):
    word = word.lower()
    res = ""
    count = 1
    #Add in first character
    res += word[0]
    #Iterate through loop, skipping last one
    for i in range(len(word)-1):
        if(word[i] == word[i+1]):
            count+=1
        else:
            if(count >= 1):
                #Ignore if no repeats
                res += str(count)
            res += word[i+1]
            count = 1
    #print last one
    if(count >= 1):
        res += str(count)
    return res




# --------------
#Code starts here

#Function to check existence of k distinct characters in string
def k_distinct(string,k):
    s_list=(set(string.lower()))
    return len(s_list)>=k

#Code ends here



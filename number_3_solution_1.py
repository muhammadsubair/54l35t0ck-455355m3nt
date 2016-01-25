'''
Env: python 2.7.6
Purpose: 
    Solve question number 3;
    Let's go back to Jakarta again. Now, you are the owner of an online shop. 
    You have been running your shop for a long time, and have a list of 1 Million blacklisted name and phone number. 
    Each line is one word(name), followed by space, then the phone number.

    Example blacklist.txt:
    ============================
    Andi 1341441
    Melisa 8565467
    Aslam 2908345
    ============================

    You want to build an API server that receive the name and phone number as an input, then output boolean whether this name and phone number is in the blacklist. 
    How would you write these two functions to optimize the latency for each API call (no need to write an API server):

    - initialize(blacklist)
    This function takes string input, which is the file name of the blacklist you have, and called when the API server is starting.

    -check_blacklist(name, phone_number)
    This function takes 2 arguments, name(string) and phone number(int). This function is called whenever the API is called, and return boolean the input name and phone number is in the blacklist.

Method:
    Because the file is not too large, better read it into a global variable string in meory in initialize(), and just directly find using (faster than reading and checking line per line) in check_blacklist()

Sample execution:
    Edit manually variable name and phone_number to get True and False result in def main(), the functions initialize() and check_blacklist() will be used in API
'''
import time

blacklist_data = '' #setup global variable to save blacklist data in memory

def initialize(blacklist):
    return open(blacklist).read()

def check_blacklist(name, phone_number):
    # print blacklist_data
    if str(name).lower() + ' ' + str(phone_number) in blacklist_data:
        return True
    else:
        return False

def main():
    initialize_start = time.time() #start count the time
    
    global blacklist_data
    blacklist_data = initialize('blacklist.txt')
    
    initialize_time = time.time() - initialize_start #get the time
    print 'time for initialize: ', str(initialize_time) #print the time
    
    check_start = time.time() #start count the time
    '''
    This part of blacklist sample word to get True result
    sqcwpq 39643088
    uybwnk 34271577
    '''
    name = 'kxwpul'
    phone_number = '20068903'
    print 'Result is', check_blacklist(name, phone_number)
    
    check_time = time.time() - check_start #get the time
    print 'time for check blacklist: ', str(check_time) #print the time

main()
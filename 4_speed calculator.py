from time import *

import random as r

def mistake(partest,usertest):
    error=0
    for i in range (len(partest)):
        try:
            if partest[i] != usertest[i]:
                error=error+1
        except Exception as e:
            error=error+1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay=time_e - time_s
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)
if __name__ =='__main__':
    while True:
        ck = input("ready to test yes/no: ")
        if ck == "yes":
            test=["A Paragraph Is A Self Contained Unit Of Discourse In Writing Dealig With Particular Idea.",
            "Python programming Is Good Language","my name is mohammad gaus nadaf"]
            test1=r.choice(test)
            print("***** Typing Speed *****")
            print(test1)
            print()
            print()
            time_1=time()
            user_input=input(("enter any sentence:"))
            time_2=time()

            print("Speed : ",speed_time(time_1,time_2,user_input),"w/sec")
            print("Error : ",mistake(test1,user_input))
        elif ck == "no":
            print("Thank You")
            break

        else:
            print("wrong input")
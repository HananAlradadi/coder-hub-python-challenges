from typing import List
def convert_time(time: str) -> str:
    if 'am' in time:
        if int(time.split(":")[0]) -12 == 0 :
            return '0:00'
            
        return time.split(" ")[0]
    if 'pm' in time:
        timeNum = time.split(":")[0]
        return str(int(timeNum)+12)+time[time.index(':'):time.index(' ')]
    timeNum = time.split(":")[0]
    if int(timeNum) >= 12 :
        if int(timeNum) == 12 :
            return '12'+time[time.index(':'):]+ ' pm'  
        return str(int(timeNum)-12)+time[time.index(':'):]+ ' pm'  
    else :
        
        if int(timeNum) == 0 :
            return '12' +time[time.index(':'):]+ ' am'
        return str(int(timeNum))+time[time.index(':'):]+ ' am'   

    # write your code here ^_^

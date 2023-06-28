from typing import List
def date_format(date: str) -> str:
    # write your code here ^_^
    datearr = date.split('/')
    dateformat2 = " | " + datearr[0] + "-" + datearr[1] + "-" +datearr[2] + ' |'
    dateformat3 = " " + datearr[1] +'/' + datearr[2] + '/'+ datearr[0]
    return date + dateformat2  + dateformat3

from typing import List
from datetime import datetime
def timePeriod(date1: str, date2: str) -> bool:
    # write your code here ^_^
    try :
        date1 = datetime.strptime(date1, '%Y-%m-%dT%H:%M:%S')
        date2 = datetime.strptime(date2, '%Y-%m-%dT%H:%M:%S')
        current_date = datetime.now()
        if not (date1 < date2 and date1 < current_date and date2 < current_date):
            raise ValueError()
        return True
    except ValueError:
        return False
    

    


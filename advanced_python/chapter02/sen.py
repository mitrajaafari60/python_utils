from datetime  import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%Y/%m/%d").strftime('%Y/%m/%d'):
            raise ValueError
        return True
    except ValueError:
        return False

birth = input()
if validate(birth) :
    start_date = datetime.strptime(birth, "%Y/%m/%d" )
    end_date = date.today()
    difference_in_years = relativedelta(end_date, start_date).years
    print(difference_in_years)
else:
    print("WRONG")

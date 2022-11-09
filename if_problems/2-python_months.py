#!/usr/bin/python3
months = {
        "January" : 31,
        "February" : "28 or 29",
        "March" : 31,
        "April" : 30,
        "May" : 31,
        "June" : 30,
        "July" : 31,
        "August" : 31,
        "September" : 30,
        "October" : 31,
        "November" : 30,
        "December" : 31,
        }

month = "January"
def get_month(month):
    month = str(input("Month: "))
    return (month)
def get_days(months, month):    
    for each, days in months.items():
        try:
            if each == month:
                return(days)

        except:
            print("App has crashed :( ")


def main():
    fetch_month = get_month(month)
    fetch_days = get_days(months, fetch_month)
    if fetch_month in months:
        print("The month of {} has {} days".format(fetch_month, fetch_days))
    else:
        print("Month does not exist")
    
main()

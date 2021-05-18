#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May, 12, 2021
# This program asks the user to input a month and year
# and then displays how many days are in that month on that year

def main():
    global month
    try:
        month = str.lower(input("Enter a month: "))
    except ValueError:
        print("Please enter a valid month.")
        main()
    else:
        if (month == "jan" or month == "january" or
            month == "feb" or month == "february" or
            month == "mar" or month == "march" or
            month == "apr" or month == "april" or
            month == "may" or
            month == "jun" or month == "june" or
            month == "jul" or month == "july" or
            month == "aug" or month == "august" or
            month == "sep" or month == "sept" or month == "september" or
            month == "oct" or month == "october" or
            month == "nov" or month == "november" or
                month == "dec" or month == "december"):
            year_input()

        else:
            print("Please enter a valid month.")
            main()


def year_input():
    global year
    try:
        year = int(input("Enter a year: "))
        if (year < 0):
            print("Please enter a valid year.")
            year_input()

        else:
            print("\n")
            output_message()

    except ValueError:
        print("Please enter a valid year.")
        year_input()


def output_message():
    if (month == "jan" or month == "january"):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("In {} (a leap year),\
 January has 31 days.".format(year))
                else:
                    print("In {} (not a leap year),\
 January has 31 days.".format(year))
            else:
                print("In {} (a leap year),\
 January has 31 days.".format(year))
        else:
            print("In {} (not a leap year),\
 January has 31 days.".format(year))

    elif (month == "feb" or month == "february"):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("In {} (a leap year),\
 February has 29 days.".format(year))
                else:
                    print("In {} (not a leap year),\
 February has 28 days.".format(year))
            else:
                print("In {} (a leap year),\
 February has 29 days.".format(year))
        else:
            print("In {} (not a leap year),\
 February has 28 days.".format(year))

    elif (month == "mar" or month == "march"):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("In {} (a leap year),\
 March has 31 days.".format(year))
                else:
                    print("In {} (not a leap year),\
 March has 31 days.".format(year))
            else:
                print("In {} (a leap year),\
 March has 31 days.".format(year))
        else:
            print("In {} (not a leap year),\
 March has 31 days.".format(year))

    elif (month == "apr" or month == "april"):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("In {} (a leap year),\
 April has 30 days.".format(year))
                else:
                    print("In {} (not a leap year),\
 April has 30 days.".format(year))
            else:
                print("In {} (a leap year),\
 April has 30 days.".format(year))
        else:
            print("In {} (not a leap year),\
 April has 30 days.".format(year))

    elif (month == "may"):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("In {} (a leap year),\
 May has 31 days.".format(year))
                else:
                    print("In {} (not a leap year),\
 May has 31 days.".format(year))
            else:
                print("In {} (a leap year),\
 May has 31 days.".format(year))
        else:
            print("In {} (not a leap year),\
 May has 31 days.".format(year))

    elif (month == "jun" or month == "june"):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("In {} (a leap year),\
 June has 30 days.".format(year))
                else:
                    print("In {} (not a leap year),\
 June has 30 days.".format(year))
            else:
                print("In {} (a leap year),\
 June has 30 days.".format(year))
        else:
            print("In {} (not a leap year),\
 June has 30 days.".format(year))

    elif (month == "jul" or month == "july"):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("In {} (a leap year),\
 July has 31 days.".format(year))
                else:
                    print("In {} (not a leap year),\
 July has 31 days.".format(year))
            else:
                print("In {} (a leap year),\
 July has 31 days.".format(year))
        else:
            print("In {} (not a leap year),\
 July has 31 days.".format(year))

    elif (month == "aug" or month == "august"):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("In {} (a leap year),\
 August has 31 days.".format(year))
                else:
                    print("In {} (not a leap year),\
 August has 31 days.".format(year))
            else:
                print("In {} (a leap year),\
 August has 31 days.".format(year))
        else:
            print("In {} (not a leap year),\
 August has 31 days.".format(year))

    elif (month == "sep" or month == "sept" or month == "september"):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("In {} (a leap year),\
 September has 30 days.".format(year))
                else:
                    print("In {} (not a leap year),\
 September has 30 days.".format(year))
            else:
                print("In {} (a leap year),\
 September has 30 days.".format(year))
        else:
            print("In {} (not a leap year),\
 September has 30 days.".format(year))

    elif (month == "oct" or month == "october"):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("In {} (a leap year),\
 October has 31 days.".format(year))
                else:
                    print("In {} (not a leap year),\
 October has 31 days.".format(year))
            else:
                print("In {} (a leap year),\
 October has 31 days.".format(year))
        else:
            print("In {} (not a leap year),\
 October has 31 days.".format(year))

    elif (month == "nov" or month == "november"):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("In {} (a leap year),\
 November has 30 days.".format(year))
                else:
                    print("In {} (not a leap year),\
 November has 30 days.".format(year))
            else:
                print("In {} (a leap year),\
 November has 30 days.".format(year))
        else:
            print("In {} (not a leap year),\
 November has 30 days.".format(year))

    elif (month == "dec" or month == "december"):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("In {} (a leap year),\
 December has 31 days.".format(year))
                else:
                    print("In {} (not a leap year),\
 December has 31 days.".format(year))
            else:
                print("In {} (a leap year),\
 December has 31 days.".format(year))
        else:
            print("In {} (not a leap year),\
 December has 31 days.".format(year))


if __name__ == "__main__":
    main()

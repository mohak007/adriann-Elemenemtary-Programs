def find_leap_years(given_year):
    count = 0


    while (count < 20):

        if (given_year % 4 == 0 or given_year % 400 == 0 and given_year % 100 == 0):
            print(given_year,"is leap year")
            count = count + 1

        given_year = given_year + 1


find_leap_years(2021)




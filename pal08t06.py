year_start = int(input("Insert year: "))
if( (year_start % 4) == 0):
    if ( (year_start % 100 ) == 0):

        if ( (year_start % 400) == 0):

            print("Is leap year!")
        else:

            print("Is not leap year!")
    else:

        print("Is leap year!")

else:

 print("Is not leap year!")
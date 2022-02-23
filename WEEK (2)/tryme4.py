
#this fundtion will print a dot.
def new_line():

    print('.')
#this function will print 3 dots using new_line funtion three times.
def three_lines():

    new_line()

    new_line()

    new_line()

# three_lines()

#nine_lines function will print 9 dots(.) using three_line function three times.
def nine_lines():

    three_lines()
    three_lines()
    three_lines()

    

#clear_function will print 25 dots(.) using nine_line two times three_times two times and new_line one time. 
def clear_screen():
    ph = print("calling clear_screen()")
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

nine_lines() #calling nine_line()
clear_screen() #calling clear_sreen()
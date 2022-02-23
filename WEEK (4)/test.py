def multi_table(n,t):
    if n == 11:
        return
    else:
        print(t + " X "  + str(n)+ " = " + str(n*t)) #Here I am not converting "t" to a string
        return multi_table(n+1,t)

t = int(input("Enter a number: "))
multi_table(1,t)
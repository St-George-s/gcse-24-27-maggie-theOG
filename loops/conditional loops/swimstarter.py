swimtime = float(input("enter a swim time: "))
if swimtime < 55.0:
    print("participant qualifies for gold category")
elif swimtime > 55.0 and swimtime < 60.1:
    print("participant qualifies for silver")
elif swimtime > 60.0 and swimtime < 70.0:
    print("participant qualifies for bronze")
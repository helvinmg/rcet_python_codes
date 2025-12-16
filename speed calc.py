speed=float(input("Enter the speed (km/h): "))
if speed<=70:
    print("No fine")
else:
    exc_speed=speed-70
    points=exc_speed//5
    print("Points: ",points)
    if points<=5:
        print("Fine: Rs.5000)
    elif points>5 and points<=10:
        print("Fine: Rs.10000)
    elif points>10 and points<=15:
        print("Fine: Rs.25000)
    else:
        print("License Suspended")

print("""
Wimco Nagar Depot; 1
Wimco Nagar; 2
Tiruvottriyur; 3
Tiruvottriyur Theradi; 4
Kaladipet; 5
Tollgate; 6
New Washermanpet; 7
Tondiarpet; 8
Sir Theagaraya College; 9
Washermanpet; 10
Mannadi; 11
High Court; 12
Puratchi Thalaivar Dr. M.G. Ramachandran Central; 13
Government Estate; 14
LIC; 15
Thousand Lights; 16
AG - DMS; 17
Teynampet; 18
Nandanam; 19
Saidapet; 20
Little Mount; 21
Guindy; 22
Arignar Anna Alandur; 23
Nanganallur Road; 24
Meenambakkam; 25
Chennai International Airport; 26
""")


## user input
stn_one = (input("What is the station of entry? Enter a number: "))
stn_two = (input("What is the station of exit? Enter a number: "))

dist = int(stn_two) - int(stn_one)

## calculating costs
def costcalc():
    if dist >= 10:
        print('Cost is 50 INR')
    elif dist <= 8:
        print('Cost is 40 INR')
    elif dist <= 6:
        print('Cost is 30 INR')
    elif dist <= 4:
        print('Cost is 20 INR')
    elif dist <= 2:
        print('Cost is 10 INR')
    else:
        print('No cost')
    if stn_two == 23:
        print("You can transfer lines at this station!")
costcalc()
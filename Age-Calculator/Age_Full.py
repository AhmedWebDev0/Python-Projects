age =input("Please Write Your Age:").strip()

unite =input("Please Write Your Age With months,weeks,days,hours,minutes,seconds:")

print(unite)

# All time unite

months = int(age) * 12
weeks = months * 4
days = weeks * 7
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

if unite == months or unite == "mo" :

    print(f"you lifed for {months:} months nearly")
    
elif unite == weeks or unite == "we" :
    
    print(f"you lifed for {weeks:} months nearly")

elif unite == days or unite == "de" :
    
    print(f"you lifed for {days:} days nearly")

elif unite == hours or unite == "ho" :
    
    print(f"you lifed for {hours:} hours nearly")

elif unite == minutes or unite == "mi" :
    
    print(f"you lifed for {minutes:} minutes nearly")

elif unite == seconds or unite == "se" :
    
    print(f"you lifed for {seconds:} seconds nearly")

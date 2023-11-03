"""
IGWE CHIDUBEM WINNER
ENG2103118
MECHANICAL ENGINEERING
"""


month = input("Enter the month of the year:  ").lower().strip()

first_quarter = {"january","february","march"}
second_quarter = {"april","may","june"}
third_quarter = {"july","august","september"}
fourth_quarter = {"october","november","december"}

combined_months = first_quarter.union(second_quarter).union(third_quarter).union(fourth_quarter)


while month not in combined_months:
    print("Pls enter a valid month input (: ")
    month = input("Enter the month of the year:  ").lower().strip()


if month in first_quarter:
    print("First_quarter")
elif month in second_quarter:
    print("Second_quarter")
elif month in third_quarter:
    print("Third_quarter")
else:
    print ("Fourth_quarter")


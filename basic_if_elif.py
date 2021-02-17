"""
Program: basic_if_elif
Author: Chris Geralds
Date: Feb/15/2021
Program asks for users desired subscription level and prints the cost
"""
print(" The five levels are: Platinum Gold Silver Bronze Free")
sub_level = input("Please enter desired subscription level:")
sub_level = sub_level.lower()[0]
cost = "The price per month is: "
pl = "$60"
au = "$50"
ag = "$40"
br = "$30"

if  sub_level == 'p':
    print(cost + pl)
elif sub_level == 'g':
    print(cost + au)
elif sub_level == 's':
    print(cost + 'ag')
elif sub_level == 'b':
    print(cost + br)
else:
    print("FREE!")


"""  Input   Expected output  Results
      Gold      $50             $50
      No        Free            Free
      Platinum  $60             $60
"""
height=int(input("WELCOME TO THE ROLLERCOSTER\nenter your current height in cms:"))
bill=0
if height >=120:
  print("you can ride the rollercoaster!")
  age=int(input("enter your current age:"))
  if age <=12:
    bill=10
    print("children tickets are $10")
  elif age <=18:
    bill=12
    print("adult tickets are $12")
  elif age >=45 and age <=55:
    bill=0
    print("dont be affraid,you have free ticket from us!")
  else:
    bill=15
    print("elder tickets are $15")
    photo=input("do you want to take photo? Y or N :")
    if photo=="y":
      bill+=3
  print(f"your finall bill is {bill}")
else:
  print("sorry!you have to grow taller before you ride it.")

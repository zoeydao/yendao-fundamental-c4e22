#Q1: A boolean value is either True or False
#3 expressions:
print(5 == 6)
print(5 == (3+2))
j =     "yen"
print(j + " dao" == "yendao")

#Q2
import webbrowser
webbrowser.open("https://drive.google.com/file/d/1TMUXGXD1F6HORBkz-B28iV_0M97g3kYv/view?usp=sharing")

#Q3: Nested conditionals mean one condition can be nested within another condition
#Example:

age = int(input("Enter your age: "))
if age < 18:
    if age > 14:
        print ("Teenager")
    else:
        print ("Child")
else:
    print ("Others")

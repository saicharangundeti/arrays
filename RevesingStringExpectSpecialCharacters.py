string=input("Enter a string")
for i in string :
    if i == " ":
        print(list(string[::-1]))
        
print("Program exited")
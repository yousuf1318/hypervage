inp=input("Enter Your Word : ")
palindrome =""
for i in inp:
    palindrome= i+palindrome

if inp==palindrome:
    print("It's a palindrome")
else:
    print("it's not a palindrome.")
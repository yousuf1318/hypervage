a = input("Enter Your Str Here : ")
string1 = ''
for i in a:
    if i not in string1:
        string1 +=i
    else:
        print("Your Duplicates : ", i)
mypassword = "Ahmed@123"
tries = 5
inputpassword = input("Please ,Your password:\t")

while mypassword != inputpassword :

    tries -= 1
    print("The password you entered is incorrect; please try again.")
    inputpassword = input("Please ,Your password:\t")
    print(f"Wrord ,{'Last' if tries == 0 else tries } Cance left.")
    
    
    if tries == 0 :
    
        print("All Tries Is Finished.")
        break

else :

    print("correct password.")

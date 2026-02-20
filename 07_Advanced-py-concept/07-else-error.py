try:
    a=200/0

except Exception as e :
    print(e)

else :
    print("Hey, I'm doing good!")  #This will only get printed when there is no error in the try block otherwise it wont print anything on the screen.
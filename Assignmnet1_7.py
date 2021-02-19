#Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
def chknum(number):
    if(number % 5 == 0):
        print("Given Number is Divisible by 5")
    else:
        print("Given Number is Not Divisible by 5")
        
def main():
    value = int(input("Enter any Integer : "))
    
    chknum(value)

if __name__ == "__main__" :
    main() 



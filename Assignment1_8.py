#Write a program which accept number from user and print that number of "*" on screen.
def chknum(number):
    icnt = 0
    for icnt in range(0,number):
        print("*", end = " ")
        
def main():
    value = int(input("Enter any Integer : "))
    
    chknum(value)

if __name__ == "__main__" :
    main()
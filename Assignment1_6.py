#Write a program which accept number from user and check whether that number is positive or negative or zero.
def chknum():
    no = int(input("Enter a number:"))
    if no > 0:
        print("Positive number")
    elif no == 0:
        print("Zero")
    else:
        print("Negative number")
        
def main():
    chknum()

if __name__ == "__main__" :
    main() 
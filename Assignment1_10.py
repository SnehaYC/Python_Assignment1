#Write a program which accept name from user and display length of its name.
def FindLen(string): 
    i = 0    
    for a in string: 
        i = i+1
    return i 

def main():
    
    str = input("Enter string:")
    
    st = FindLen(str)
    
    print("Length of the string is:",st)
    
    
if __name__ == "__main__":
    main() 


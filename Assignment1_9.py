#Write a program which display first 10 even numbers on screen.
def ChkNum():
    
    for num in range(1,21): 
        if num % 2 == 0: 
            print(num, end = " ") 
        
def main():
    ChkNum()
        
if __name__ == "__main__":
    main() 
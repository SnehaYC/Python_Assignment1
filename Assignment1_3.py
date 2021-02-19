#write a program which contains one function named as Add() which accepts two numbers from user and return addition of that numbers.
def Add(value1,value2):
    ret = value1 + value2 
    return ret 
  
def main(): 
    print("Enter first number:")
    no1 = int(input())
    
    print("Enter second number:")
    no2 = int(input())
    
    ans = Add(no1,no2)
    
    print("Addition is :",ans)

if __name__ == "__main__" :
    main() 
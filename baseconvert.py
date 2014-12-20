'''
Created on 12 Dec 2014

@author: MuresanVladut
'''





BASE2 = "01"
BASE3= "012"
BASE4 = "0123"
BASE5 = "01234"
BASE6= "012345"
BASE7 = "0123456"
BASE8 = "01234567"
BASE9 = "012345678"
BASE10 = "0123456789"
BASE11 = "0123456789A"
BASE12 = "0123456789AB"
BASE13 = "0123456789ABC"
BASE14 = "0123456789ABCD"
BASE15 = "0123456789ABCDE"
BASE16 = "0123456789ABCDEF"


print("""-------------------------
|BASE CONVERSION PROGRAM|
-------------------------""")



def printMenu():
    print('''1. Operations.
2. Conversions.
3. Exit.''')


def run():
    menu={1:operations,2:conversions,3:exit}
    while True:
        printMenu()
        try:
            opt=int(input("Choose option: "))
            menu[opt]()
        except ValueError:
            print("Invalid option")
        except KeyError:
            print("Unimplemented option")


def exit():
    raise SystemExit



def operations():
    menu={1:add,2:sub,3:mul,4:div}
    
    try:
        opt=int(input('''Please choose the desired operations: 
1. addition
2. subtraction
3. multiplication
4. division'''))
        menu[opt]()
    except ValueError:
        print("Invalid option")
    except KeyError:
        print("Unimplemented option")
        
def add():
    while True:
        try:
            base=int(input("Please enter the numbers base: "))
            if base==2:
                base=BASE2
            if base==3:
                base=BASE3
            if base==4:
                base=BASE4
            if base==5:
                base=BASE5
            if base==6:
                base=BASE6
            if base==7:
                base=BASE7
            if base==8:
                base=BASE8
            if base==9:
                base=BASE9
            if base==10:
                base=BASE10
            if base==11:
                base=BASE11
            if base==12:
                base=BASE12
            if base==13:
                base=BASE13
            if base==14:
                base=BASE14
            if base==15:
                base=BASE15
            if base==16:
                base=BASE16
            break
        except ValueError:
            print("Invalid base input.")
    number1=input("Please enter the first number: ")
    number2=input("Please enter the second number: ")
    num1=baseconvert(number1,base,BASE10)
    num2=baseconvert(number2,base,BASE10)
    add=int(num1)+int(num2)
    print("THE NUMBER ADDITION IS: ")
    print(baseconvert(add,BASE10,base))
    
    
def sub():
    while True:
        try:
            base=int(input("Please enter the numbers base: "))
            if base==2:
                base=BASE2
            if base==3:
                base=BASE3
            if base==4:
                base=BASE4
            if base==5:
                base=BASE5
            if base==6:
                base=BASE6
            if base==7:
                base=BASE7
            if base==8:
                base=BASE8
            if base==9:
                base=BASE9
            if base==10:
                base=BASE10
            if base==11:
                base=BASE11
            if base==12:
                base=BASE12
            if base==13:
                base=BASE13
            if base==14:
                base=BASE14
            if base==15:
                base=BASE15
            if base==16:
                base=BASE16
            break
        except ValueError:
            print("Invalid base input.")
    number1=input("Please enter the first number: ")
    number2=input("Please enter the second number: ")
    num1=baseconvert(number1,base,BASE10)
    num2=baseconvert(number2,base,BASE10)
    add=int(num1)-int(num2)
    print("THE NUMBER SUBTRACTION IS: ")
    print(baseconvert(add,BASE10,base))


def mul():
    while True:
        try:
            base=int(input("Please enter the numbers base: "))
            if base==2:
                base=BASE2
            if base==3:
                base=BASE3
            if base==4:
                base=BASE4
            if base==5:
                base=BASE5
            if base==6:
                base=BASE6
            if base==7:
                base=BASE7
            if base==8:
                base=BASE8
            if base==9:
                base=BASE9
            if base==10:
                base=BASE10
            if base==11:
                base=BASE11
            if base==12:
                base=BASE12
            if base==13:
                base=BASE13
            if base==14:
                base=BASE14
            if base==15:
                base=BASE15
            if base==16:
                base=BASE16
            break
        except ValueError:
            print("Invalid base input.")
    number1=input("Please enter the first number: ")
    number2=input("Please enter the second number: ")
    num1=baseconvert(number1,base,BASE10)
    num2=baseconvert(number2,base,BASE10)
    add=int(num1)*int(num2)
    print("THE NUMBER MULTIPLICATION IS: ")
    print(baseconvert(add,BASE10,base))
    
def div():
    while True:
        try:
            base=int(input("Please enter the numbers base: "))
            if base==2:
                base=BASE2
            if base==3:
                base=BASE3
            if base==4:
                base=BASE4
            if base==5:
                base=BASE5
            if base==6:
                base=BASE6
            if base==7:
                base=BASE7
            if base==8:
                base=BASE8
            if base==9:
                base=BASE9
            if base==10:
                base=BASE10
            if base==11:
                base=BASE11
            if base==12:
                base=BASE12
            if base==13:
                base=BASE13
            if base==14:
                base=BASE14
            if base==15:
                base=BASE15
            if base==16:
                base=BASE16
            break
        except ValueError:
            print("Invalid base input.")
    number1=input("Please enter the first number: ")
    number2=input("Please enter the second number: ")
    num1=baseconvert(number1,base,BASE10)
    num2=baseconvert(number2,base,BASE10)
    add=int(num1)/int(num2)
    print("THE NUMBER MULTIPLICATION IS: ")
    print(baseconvert(add,BASE10,base))
    
    
        
    
    
    
    
    
    
    
    
    

def conversions():
    number=input("Please enter the number: ")
    while True:
        try:
            fromdigits=int(input("Please enter the number base: "))
            if fromdigits==2:
                fromdigits=BASE2
            if fromdigits==3:
                fromdigits=BASE3
            if fromdigits==4:
                fromdigits=BASE4
            if fromdigits==5:
                fromdigits=BASE5
            if fromdigits==6:
                fromdigits=BASE6
            if fromdigits==7:
                fromdigits=BASE7
            if fromdigits==8:
                fromdigits=BASE8
            if fromdigits==9:
                fromdigits=BASE9
            if fromdigits==10:
                fromdigits=BASE10
            if fromdigits==11:
                fromdigits=BASE11
            if fromdigits==12:
                fromdigits=BASE12
            if fromdigits==13:
                fromdigits=BASE13
            if fromdigits==14:
                fromdigits=BASE14
            if fromdigits==15:
                fromdigits=BASE15
            if fromdigits==16:
                fromdigits=BASE16
            break
        except ValueError:
            print("Invalid base input.")
    while True:
        try:
            todigits=int(input("Please enter the desired base conversion: "))
            if todigits==2:
                todigits=BASE2
            if todigits==3:
                todigits=BASE3
            if todigits==4:
                todigits=BASE4
            if todigits==5:
                todigits=BASE5
            if todigits==6:
                todigits=BASE6
            if todigits==7:
                todigits=BASE7
            if todigits==8:
                todigits=BASE8
            if todigits==9:
                todigits=BASE9
            if todigits==10:
                todigits=BASE10
            if todigits==11:
                todigits=BASE11
            if todigits==12:
                todigits=BASE12
            if todigits==13:
                todigits=BASE13
            if todigits==14:
                todigits=BASE14
            if todigits==15:
                todigits=BASE15
            if todigits==16:
                todigits=BASE16  
            break
        except ValueError:
            print("Invalid base input.")
    
    
    print("THE NUMBER REPRESENTATION: ")
    print(baseconvert(number,fromdigits,todigits))
    
    
    while True:
        i=input("Do you want to contiune? y/n ")
        if i=='y':
            run()
        else:
            break
    
    
    

    

def baseconvert(number,fromdigits,todigits):
    if str(number)[0]=='-':
        number = str(number)[1:]
        neg=1
    else:
        neg=0
         
    x=0
    try:
        for digit in str(number):
        
            x = x*len(fromdigits) + fromdigits.index(digit)
    except Exception:
        print("Please enter a valid number in that base.")
            
    if x == 0:
        res = todigits[0]
    else:
        res=""
        while x>0:
            digit = x % len(todigits)
            res = todigits[digit] + res
            x = int(x / len(todigits))
        if neg:
            res = "-"+res
         
    return res




run()

if __name__ == '__main__':
    pass

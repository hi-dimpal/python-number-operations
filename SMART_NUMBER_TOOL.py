def getNumber():
    return int(input("Enter Number = "))

def makePositive(num):
    if num < 0:
        return -num
    return num

def reverseNumber(num):
    rev = 0
    while num > 0:
        lastDigit = num % 10
        rev = rev * 10 + lastDigit
        num //= 10
    return rev

def isPalindrome(num, rev):
    if num == rev:
        print("Palindrome Number")
    else:
        print("Not a Palindrome")

def isEvenOdd(num):
    if num % 2 == 0:
        print(f"{num} is an Even Number")
    else:
        print(f"{num} is an Odd Number")

def main():
    num = getNumber()
    num = makePositive(num)

    while True:
        print("\n--- MENU ---")
        print("1. Reverse Number")
        print("2. Check Palindrome")
        print("3. Check Even / Odd")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            rev = reverseNumber(num)
            print("Reverse Number:", rev)
            print("\n")

        elif choice == "2":
            rev = reverseNumber(num)
            isPalindrome(num, rev)
            print("\n")


        elif choice == "3":
            isEvenOdd(num)
            print("\n")


        elif choice == "4":
            print("Thank you, exiting program.")
            break
            print("\n")


        else:
            print("Invalid input.")

main()

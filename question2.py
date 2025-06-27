def check_palindrome():
    text = input("Enter a string to check if it's a palindrome: ")
    cleaned = text.replace(" ", "").lower()
    if cleaned == cleaned[::-1]:
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")

# Run it
check_palindrome()

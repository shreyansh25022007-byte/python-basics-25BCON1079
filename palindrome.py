# Check whether a user-provided word or phrase is a palindrome.

text = input("Enter a word or phrase: ")
cleaned = "".join(ch.lower() for ch in text if ch.isalnum())

if cleaned == cleaned[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

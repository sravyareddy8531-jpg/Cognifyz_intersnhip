def is_palindrome(text):
    text = text.lower()
    
    reversed_text = text[::-1]

    if text == reversed_text:
        return True
    else:
        return False

word = input("Enter a word to check: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
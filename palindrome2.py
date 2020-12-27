# Palindrome Exercise:
word=str(input("Please enter the word here="))
i=0
isPalindrome = 1;
x = len(word)-1;
while word:
    if(i>=x/2):
        break
    if word[i]==word[x-i]:
        i = i + 1
        continue
    else:
        print("This isn\'t a palindrome.")
        isPalindrome = 0
        break
if(isPalindrome):
    print("This is palindrome")





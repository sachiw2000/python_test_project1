# Palindrome Exercise:
word=str(input("Please enter the word here="))
count=0
while word:
    x=len(word)
    count=count+1
    i=0
    if word[i]==word[x-count]:
        i=i+i
        print("This is a palindrome.")
        break

    else:
        print("This isn\'t a palindrome.")
        break




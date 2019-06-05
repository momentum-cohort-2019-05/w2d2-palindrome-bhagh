import re

#grab user input
submission = input("Enter a word or sentence(s): ")

#function to clean up text by user
def cleantext (submission):
    submission = (re.sub("[^a-zA-Z0-9]+", '', submission).replace(" ",""))
    return submission

print(cleantext(submission))

#create a string that's the reverse of the text by the user
backwards_string = (cleantext(submission)[::-1])

#check if both strings match
if str(cleantext(submission).lower()) == str(backwards_string.lower()):
    print(submission, "is a palindrome")
else:
    print(submission, "is not a palindrome")



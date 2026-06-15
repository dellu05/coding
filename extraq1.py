#Reverse the words in the sentence “have a nice day”. It should be changed to “day nice a have”.
text = input("Enter a sentence: ")
reversed_text = " ".join(text.split()[::-1])
print("Reversed:", reversed_text)

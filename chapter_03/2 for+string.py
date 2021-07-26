str = input("Enter your text = ")
count = 0
for i in str:
    count = count + 1

print("The number of string = ", count)

#---------------------------------------------------
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = input("Enter your string = ")
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

#--------------------------------------------------
my_str = "Hello this Is an Example with The word oders"

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
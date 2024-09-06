# Nidhi is creating a program in python for her school project. In between the program, she is converting numerical numbers
# into word format again and again. Then she realizes that she needs a function that can convert a number into word format
#  with hyphens between each word. ( for example 57 = five-seven ). To help Nidhi create a function toWord() that can do
#  the same thing. Hint: Use for loop and
#   use if-elif-else condition Sample run: >> toWord(89) >> eight-nine >> toWord(398) >> three-nine-eight




def wordsofnum(x):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    conv=[]
    y=str(x)
    for digit in y:
        word=words[int(digit)]
        conv.append(word)
    return conv


a=int(input("Enter a number : "))
wordsofnum(a)
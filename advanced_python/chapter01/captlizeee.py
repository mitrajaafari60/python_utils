text = input()
words1 = text.split()
words = words1[1:]
cnt=2
isEnd = False
for word in words:
    if not(isEnd):
        if word[-1] == '.' or word[-1] == ',':
            word = word[:-1]  # Remove trailing period or comma
            isEnd= True
        else:
            isEnd= False

        if word== word.capitalize():
            print (cnt,":",word)
        cnt +=1
    else:
        cnt +=1
        isEnd= False
    
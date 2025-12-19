a = input("Enter your text : ")
words = a.split()
words_count = {}
for word in words:
    word = word.lower()
    if word in words_count:
        words_count[word]+=1
    else:
        words_count[word]=1
print("Word Occurrence : ")      
for word,count in words_count.items():
    print(f"{word}:{count}")
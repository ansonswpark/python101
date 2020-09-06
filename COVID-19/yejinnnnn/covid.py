file = open("00.txt", "r")
text = file.read()
words = text.split()
wordCount = dict()
for word in words:
    wordCount[word] = wordCount.get(word, 0) + 1
for word, count in wordCount.items():
    pritn(word, count)


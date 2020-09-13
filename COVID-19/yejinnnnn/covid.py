import glob
news_list = glob.glob("COVID-19/news/*.txt")
total_count = 0

for news in news_list:
    with open(news, "r") as file:
        contents = file.read()
    total_count += contents.count("COVID-19")
print(total_count)


# file = open("00.txt", "r")
# text = file.read()
# words = text.split()
# wordCount = dict()
# for word in words:
#     wordCount[word] = wordCount.get(word, 0) + 1
# for word, count in wordCount.items():
#     print(word, count)
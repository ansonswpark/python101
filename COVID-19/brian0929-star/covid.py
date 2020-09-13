import glob
news_list = glob.glob("C:/Users/marsg/python101/COVID-19/news/*.txt")

total_count = 0

for news in news_list:
    with open(news, "r", encoding='UTF8') as file:
        contents = file.read()
        total_count += contents.count('COVID-19')

print(total_count)
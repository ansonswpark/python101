import glob
news_files = glob.glob("C:/Users/user/Documents/python101/COVID-19/news/*.txt")
total_count = 0
for news_file in news_files:
    with open(news_file, "r", encoding='UTF-8') as f:
        contents = f.read()
        count = contents.count("COVID-19")
        total_count += count

print(total_count)
import glob

path = '/Users/cubana/python101/COVID-19/news/*.txt'
files = glob.glob(path)
count_num = 0
for file in files:
    with open(file, 'r', encoding='UTF-8') as f:
        contents = f.read()
        c = contents.count('COVID-19')
        count_num += c

print(count_num)
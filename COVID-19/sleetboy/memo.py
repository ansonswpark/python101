# 한 파일에서만 카운팅 하고 다른 파일로 넘어가지 못해서 실패함

def count_words():  
    with open(r"C:\Users\cubana\python101\COVID-19\news\00.txt", "r") as file:
        contents = file.read()
        c = contents.count("COVID-19")
        return print(c)
        
count_words()

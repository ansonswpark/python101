import glob


def count_text(path, string):
    """
    :param path: str() 입력 데이터 경로
    :param string: str() 데이터에서 찾을 단어
    :return: 데이터에서 단어 등장 횟수
    """
    with open(path, encoding='utf-8') as fin:
        return fin.read().count(string)


def main():
    target_word = 'COVID-19'
    num_of_target_word = 0
    path_in_dir = '/Users/cubana/python101/COVID-19/news'
    file_list = glob.glob(f'{path_in_dir}/*.txt')

    for file_name in file_list:
        num_of_target_word += count_text(file_name, target_word)

    print(f'target_word: {target_word}\nnum_of_target_word: {num_of_target_word}')


if __name__ == '__main__':
    main()
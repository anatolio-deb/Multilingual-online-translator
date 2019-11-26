import requests
from bs4 import BeautifulSoup

def translate_word():
    languages_list = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese', 'dutch', 'polish', 'portuguese', 'romanian', 'russian', 'turkish']
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
    mod = input(f"Hello, you're welcome to translator. Translator supports \n{', '.join(languages_list)}\n Type your language: ").strip().lower()

    while mod in languages_list:
        word = input('Type word you want to translate: ')
        URL = f'https://context.reverso.net/translation/{mod}-{mod}/' + word.replace(" ", "+").lower().replace("'", "%27")
        print(f'URL = {URL}')

        try:
            response = requests.get(URL, headers=headers) #  send request
            if response.status_code == 200:
                print(response.status_code, 'OK')
            else:
                print(f'Error {response.status_code}!')
        except requests.exceptions.ConnectionError:
            print('Something wrong with your internet connection')
            return False

            only_translations_list = []
            translation_text = ''

            soup = BeautifulSoup(response.text, "html.parser")
            only_translations_of_word = soup.find_all(['div', 'a'], {"class": ['translation']})
            for translation in only_translations_of_word:
                only_translations_list.append(translation.text.replace('\n', '').strip())
                for translation in only_translations_list:
                    if len(translation) > 0:
                        if translation == 'Translation':
                            translation = f'\n{language} {translation.lower()}:'.title()
                            translation_text += f'{translation}\n'

                            if len(translation_text) <= len('Translation:\n\n'):  #  If there are no translations, exit from function
                                print("Sorry, there's no such word")
                            return False

                            with open(f'{word}-translations.txt', 'a') as file:
                                file.write(translation_text)
                                translation_text = ''
                                only_translations_list.clear()
                                return True

    else:
        print('Sorry, we currently support languages named above')
        return False

if __name__ == "__main__":
    flag = False
    while not flag:
         flag = translate_word()

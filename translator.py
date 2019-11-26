import requests
from bs4 import BeautifulSoup
import shelve

def translate_word():
    #  init variables:
    mod = input('Type "en" if you want to translate from russian into english, or "ru" if you want to translate from english into russian: ')
    if mod not in ['en', 'ru']: #  if mod incorrect exit from function
        print('Sorry, we currently support English and Russian')
        return False

    word = input('Type word you want to translate: ')
    translations_with_examples_list, only_translations_list = [], []
    translation_text = ''
    example_text = "Context examples:\n"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
    #  create request:
    if mod == 'en':
        URL = 'https://context.reverso.net/translation/russian-english/' + word.replace(" ", "+").lower().replace("'", "%27")
    elif mod == 'ru':
        URL = 'https://context.reverso.net/translation/english-russian/' + word.replace(" ", "+").lower().replace("'", "%27")
    print(f'URL = {URL}')  #  if URL is correct, we will see it

    with requests.Session() as s:
        response = s.get(URL, headers=headers) #  send request
        try:
            response = s.get(URL, headers=headers) #  send request
            if response.status_code == 200:
                print(response.status_code, 'OK')
            else:
                print(f'Error {response.status_code}!')
        except requests.exceptions.ConnectionError:
            print('Connection Error! Check your internet!')
        soup = BeautifulSoup(response.text, "html.parser")  #  parse web page
        #  find all translations and examples allowed:
        translations_with_examples = soup.find_all(['div', 'a'], {"class": ['translation', 'src', 'trg']})
        #  if programm is correct, write it into a file to see what is html language:
        with open('translations_with_examples.html', 'w') as file:
            file.write(str(translations_with_examples))
        #  find only translations of word:
        only_translations_of_word = soup.find_all(['div', 'a'], {"class": ['translation']})
        #  also write in into a file:
        with open('only_translations_of_word.html', 'w') as file:
            file.write(str(only_translations_of_word))
        #  get text from html and format it:
        for example in translations_with_examples:
            translations_with_examples_list.append(example.text.replace('\n', '').strip())
        for translation in only_translations_of_word:
            only_translations_list.append(translation.text.replace('\n', '').strip())
        #  we need see the result:
        #print(translations_with_examples_list)
        #print(only_translations_list)
        #  but there are the same elements at the begining two lists, delete them from larger list
        #  delete olnly translations from "translations and examples list". only examples left
        translations_with_examples_list = translations_with_examples_list[translations_with_examples_list.index(only_translations_list[-1]) + 1:]
        #  format output for readable translations:
        for translation in only_translations_list:
            if len(translation) > 0:
                if translation == 'Translation' or translation in word:
                    translation = '\n{}:'.format(translation)
                translation_text += '{}\n'.format(translation)

        #  format output for readable examples:
        example_count = 0
        for example in translations_with_examples_list:
            if len(example) > 0:
                example_count += 1
                if example_count % 2 == 1 and len(translation_text) != 10:
                    example = '\n{}:'.format(example)
                example_text += example + '\n'

        if len(translation_text) <= len('Translation:\n\n'):  #  If there are no translations, exit from function
            print("You typed incorrect word, we can't translate it!")
            return False
        print(example_text)
        print(translation_text)
    return True


if __name__ == "__main__":
    flag = False
    while not flag:
         flag = translate_word()

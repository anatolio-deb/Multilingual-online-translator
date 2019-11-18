import requests
from bs4 import BeautifulSoup

def translate_word():
    mod = input('Type "en" if you want to translate from russian into english, or "ru" if you want to translate from english into russian: ')
    if mod not in ['en', 'ru']:
        print('Sorry, we currently support English and Russian')
        return False

    word = input('Type the word you want to translate: ')
    print("You chose "+"«"+mod+"»"+" as a language "+"to translate","«"+word+"».")

    if mod == 'en':
        URL = 'https://context.reverso.net/translation/russian-english/' + word.replace(" ", "+").lower().replace("'", "%27")
    elif mod == 'ru':
        URL = 'https://context.reverso.net/translation/english-russian/' + word.replace(" ", "+").lower().replace("'", "%27")

    useragent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

    try:
        response = requests.get(URL, headers=useragent)
# Below you can check if the url is accepted by the server
        if response.status_code == 200:
            print(response.status_code, 'OK')
        else:
            print(f'Error {response.status_code}!')
    except requests.exceptions.ConnectionError:
        print('Something wrong with your internet connection')
        return False

    translations_with_examples_list, only_translations_list = [], []
    translation_text = ''
    example_text = "Context examples:\n"

    soup = BeautifulSoup(response.text, "html.parser")
    translations_with_examples = soup.find_all(['div', 'a'], {"class": ['translation', 'src', 'trg']})
    only_translations_of_word = soup.find_all(['div', 'a'], {"class": ['translation']})
    for example in translations_with_examples:
        translations_with_examples_list.append(example.text.replace('\n', '').strip())
    for translation in only_translations_of_word:
        only_translations_list.append(translation.text.replace('\n', '').strip())
    # Below you can check the data you recieve
    #    print(translations_with_examples_list)
    #    print(only_translations_list)
    #    return False

    translations_with_examples_list = translations_with_examples_list[translations_with_examples_list.index(only_translations_list[-1]) + 1:]

    for translation in only_translations_list:
         if len(translation) > 0:
            if translation == 'Translation' or translation in word:
                translation = '\n{}:'.format(translation)
            translation_text += '{}\n'.format(translation)

    example_count = 0
    for example in translations_with_examples_list:
        if len(example) > 0:
            example_count += 1
            if example_count % 2 == 1 and len(translation_text) != 10:
                example = '\n{}:'.format(example)
            example_text += example + '\n'

    if len(translation_text) <= len('Translation:\n\n'):
        print("Sorry, unable to find this word")
        return False
    print(example_text)
    print(translation_text)
    return True



if __name__ == "__main__":
    translate_word()

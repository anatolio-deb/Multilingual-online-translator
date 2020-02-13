import requests
from bs4 import BeautifulSoup
def translate():
	language = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
	word = input('Type the word you want to translate:')
	print(f'You chose «{language}» as a language to translate «{word}».')
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

	if language == 'en':
		URL = f'https://context.reverso.net/translation/french-english/' + word.replace(" ", "+").lower().replace("'", "%27")
	elif language == 'fr':
		URL = f'https://context.reverso.net/translation/english-french/' + word.replace(" ", "+").lower().replace("'", "%27")

	# print(f'URL = {URL}')  #  if URL is correct, we will see it
	try:
		response = requests.get(URL, headers=headers)  # send request
		if response.status_code == 200:
			print(response.status_code, 'OK')
	except:
		pass
	soup = BeautifulSoup(response.text, "html.parser")  # parse web page
	#  find translations with examples:
	translations_with_examples = soup.find_all(['div', 'a'], {"class": ['translation', 'src', 'trg']})
	#  find only translations of word:
	only_translations_of_word = soup.find_all(['div', 'a'], {"class": ['translation']})
	only_translations_list = []
	translations_with_examples_list = []
	for example in translations_with_examples:
		translations_with_examples_list.append(example.text.replace('\n', '').strip())
	for translation in only_translations_of_word:
		only_translations_list.append(translation.text.replace('\n', '').strip())
	print(only_translations_list)
	print(translations_with_examples_list)


translate()
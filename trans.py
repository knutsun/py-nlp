#-*- coding: utf-8 -*-

from google.cloud import translate

def translateText(text, target='en'):
	translateClient = translate.Client()
	with open('test.csv', 'a+') as test:
		output = translateClient.translate(text, target_language=target)
		test.write(output['translatedText'] + '\n')
		print(output['translatedText'])
	

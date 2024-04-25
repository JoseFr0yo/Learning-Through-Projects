from translate import Translator
print('Enter the language you want to translate to: ')
print('List of Available Languages: \n Afrikaans: af \n Catalan: ca \n Chinese: zh \n Dutch: nl \n French: fr \n German: de \n Greek: el \n Hebrew: he \n Hindi: hi \n Icelandic: is \n Italian: it \n Japanese: ja \n Kongo: kg \n Korean: ko \n Latin: la \n Norwegian: no \n Portuguese: pt \n Russian: ru \n Samoan: sm \n Spanish: es \n Swedish: sv \n')
print('Enter the language code:')
translator = Translator(to_lang=input(""))

try:
    # Create a file to store user input
    with open('./txt4transl.txt', mode='w') as userInput:
        inputText = input('Enter text to translate: ')
        userInput.write(inputText)

    # Read the file and translate the text
    with open('./txt4transl.txt', mode='r') as translateFile:
        text = translateFile.read()
        translated = translator.translate(text)
    print(translated)

    with open('./translation.txt', mode='w', encoding='utf-8') as translationFile:
        translationFile.write(translated)

except FileNotFoundError as err:
    print('File not found')

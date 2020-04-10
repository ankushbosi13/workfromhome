from translate import Translator
translator = Translator(to_lang="zh")
try:
    with open("test.py",mode="r") as file:
        text=file.read()
        translation=translator.translate(text)
        print(translation)

except FileNotFoundError as e:
    print("no file exists")


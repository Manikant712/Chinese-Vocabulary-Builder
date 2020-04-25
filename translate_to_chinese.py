from googletrans import Translator
import pinyin 
translator = Translator()
file1 = open("words_meaning.txt","w")
with open('words.txt') as f:
    for line in f:
        for word in line.split():
            try:
                ts = translator.translate(word)
                pn = pinyin.get(word)
                ws = word + ",  " + pn + ",  " + ts.text
                file1.write(ws)
                file1.write("\n")
                print(word)
            except Exception:
                pass
        
    

##ts = translator.translate('你好!')
##
##print(ts.text)

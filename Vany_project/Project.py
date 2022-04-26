import os
import time


# составление списка слов
def Spis(doc,param): # param - параметр, определяющий что будет результатом функции
    print(doc)
    print('')
    j = 0
    word: str
    word2: str
    file: str
    inde: int
    S = []
    Add = []
    Add2 = []
    alphav = 'йцукенгшщзхъфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm'
    znak = '.`~@"№#$;%:^&?*()-–_=+{}][|\/,!?<>«»0123456789…— '
    file = open(doc,'r')
    line = '-'

    Di = {}
    Add_A = [] # будет списком списков
    number = 1 # номер строки
    while line != '':
        line = file.readline()
        line = line.lower()
        word = ''

        while(line.count('ё') > 0):
            line = line.replace('ё','е')

        while(line.count('\xa0') > 0):
            line = line.replace('\xa0',' ')

       
        for k in line:              
            if not (k in znak) : # если k это буква
                if(k == '\n'):
                    Add.append(word)
                    Add_A.append([word,number])
                    Di[word] = number
                else:
                    word = word + k
            else :
                Add.append(word)
                Add_A.append([word,number])
                Di[word] = number
                word = ''

        number += 1


    file.close()
    if param == 1:
        # удаляем пустые элементы в списке
        # ---------------------------
        Add2 = []
        for k in Add:
            if k != '':
                Add2.append(k)
        Add = Add2
        return Add  # список слов текста

    elif param == 2:
        # удаляем пустые элементы в списке списков
        # ---------------------------
        for k in Add_A:
            if k[0] == '':
                Add_A.remove(k)
        return Add_A  # список списков, где первый элемент вложенного списка - слово, второй - номер строки

    elif param == 3:
        # удаляем пустые элементы в словаре
        # ---------------------------
        g = 0
        while g == 0:
            g = Di.pop('',1)
        return Di # словарь, где ключ - слово, значение - номер строки




    


# поиск слов в тексте. - ПРАВИЛО 1
# Будем искать слова в сформированном нами списке списков Add_A, так как он содержит номер строки для каждого слова
def Poisk(S,words):
    for k in S:
        for g in words[0]:
            if k[0] == g:
                print('личное местоимение ',g,' в ',k[1],' строке')
                #S[k] = ['***',2] # временно заменяем местоимение на ***
        for g in words[1]:
            if k[0] == g:
                print('указательное местоимение ',g,' в ',k[1],' строке')
                #S[k] = ['***',2] # временно заменяем местоимение на ***
    #print(S)
    return S


# замена союза "потому что" на "так как"(/"вследствии того, что"/"ввиду того, что"/"в силу того, что") - ПРАВИЛО 2
def Pravil2(S):
    words = [['так','как'],['вследствии','того','что'],['ввиду','того','что'],['в','силу','того','что']]
    # пока все "потому что" заменяются на "так как", но можно с помощью рандома выбирать один из вариантов
    i = 0
    zam = 0
    while i < len(S)-1:  # проверить правильно ли проходит границы
        if S[i] == 'потому':
            if S[i+1] == 'что':
                S[i] = words[0][0]
                S[i+1] = words[0][1]
                zam += 1
        i += 1
    print('было заменено ',zam,'союза "потому что"')
    return S

    # если надо - можно сделать запись измененного текста в файл
 

# сейчас первые 2 правила работают по отдельности 
def main():
    os.system('cls')
    print('какое правило запустить?')
    print('1 - первое правило')
    print('2 - второе правило')
    vvod = int(input(': '))
    

    #path = 'D:\\WORK\\Project\\5.txt' # путь к файлу
    path = '5.txt'
    if vvod == 1:
        S = Spis(path,2)  
        print('длина текста: ',len(S))
        #print(S[0:100])
        print(S)
        print('')

        # личные местоимения
        words1 = ['я','ты','мы','вы','он','она','оно','они']
        # указательные местоимения
        words2 = ['этот','тот','такой','таков','этакий','столько']
        words = [words1,words2]
        Rez1 = Poisk(S,words)
        #print(Rez1)
        print('')
    elif vvod == 2:
        S2 = Spis(path,1)
        print('текст до применения правила: ')
        print(S2)
        print('')
        Rez2 = Pravil2(S2)
        print('текст после применения правила: ')
        print(Rez2)
        
        # Если надо чтобы измененный текст выводился нормально, а не списком слов
        # (из текста удалены все знаки препинания)
        #Text = ''
        #for h in Rez2:
        #    Text = Text + h + ' '
        #print(Text)

    else:
        print('вы ввели неправильный символ. Введите "1" или "2"')

print(main())
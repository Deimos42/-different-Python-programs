import pyautogui # библиотека для работы с клавиатурой и мышью
import mss # библиотека для создания снимков экрана
import time
import pydirectinput
#import tkinter
from threading import Thread
import keyboard
#import PIL
from PIL import Image, ImageFilter
import numpy as np
import cv2 # OpenCV

# pyautogui не работает во многих приложениях и очень медленно кликает
# можно использовать 

# https://cyberguru.tech/%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/python/pyautogui
def spravka():
    # включение прерывания программы при нажатии CTRL+C
    pyautogui.FAILSAFE = True 
    
    while True:
        print(9)

    # клик мышью по заданной координате
    pyautogui.click(2880,1000) 

    # перемещение мыши в заданные координаты
    pyautogui.moveTo(3800,10,duration=5) # duration время перетаскивания в секундах

    # перемещение мыши относительно текущей позиции
    pyautogui.moveRel(1000,0,duration=2) # duration время перетаскивания в секундах

    # перетаскивание(перемещение мыши с зажатой левой кнопкой)
    pyautogui.dragTo(x,y,duration)
    pyautogui.dragRel(x,y,duration)

    # PyAutoGUI может позволить нам использовать многие из этих функций. Некоторые из них:

    # Одиночный, двойной и тройной клик
    # Кнопка мыши верх и вниз
    # Левый, правый и средний щелчок
    pyautogui.click(x=None, y=None, clicks=1, interval=0.0, button='left', duration=0.0)

    # прокрутка мышью

    # КЛАВИАТУРА

    # печать текста
    pyautogui.typewrite('Hello world!')

    # печать текста с задержкой перед каждой буквой
    pyautogui.typewrite('Hello world!', interval = 0.25) 


    # нажатие клавиши
    pyautogui.press('enter')

    # сочетания клавиш
    pyautogui.hotkey('ctrl', 'shift', 'esc') # одновременно нажать клавиши CTRL + SHIFT + ESC

    # окно оповещения
    pyautogui.alert(text = '', title = '', button = 'OK')
    # окно подтверждения
    text = pyautogui.confirm(text = '', title = '', buttons = ['OK', 'Cancel'])
    # окно подсказки
    pyautogui.prompt (text = '', title = '', default = '')
    # окно пароля
    passw = pyautogui.password(text='', title='', default='', mask='*')
    print(passw)

    # позиция курсора
    x,y = pyautogui.position()
    print(x,y)
    #
    #
    #
    #
    #

# для pyautogui
# скорость - 10 кликов в секунду(не зависит от герцовости мышки)
def click_speed():
    t1 = time.time()
    i = 0 
    pyautogui.moveTo(537,268)
    while i < 100:
        pyautogui.click(clicks=1)
        i += 1
    t2 = time.time()
    return (t2 - t1)
    
#timee = click_speed()
#print(timee)

# 10 кликов в секунду(так же как и двойных) вне зависимости от мышки
def click_speed3():
    print('двойной клик ')
    res = 0
    pyautogui.moveTo(537,268)
    N = 10
    for k in range(1,N):
        t1 = time.time()      
        pyautogui.click(clicks=2) 
        t2 = time.time()
        print('прогонка',k,': ',t2 - t1)
        res += t2-t1
    print('-------------------')
    print('среднее: ',res/N)
    return

#click_speed3()

# для pyautogui
def click_speed2():
    t1 = time.time()
    i = 0 
    while i < 100:
        pydirectinput.click(537,268)
        i += 1
    t2 = time.time()
    print(t2 - t1)
    return
    # скорость - 5 кликов в секунду...

#click_speed2()

# 5 кликов в секунду
def paint_black(x,y):
    t1 = time.time()
    pyautogui.click(x,y)
    cord = pyautogui.position()
    while cord[0] < x + 50:     
        pyautogui.moveRel(1,0)
        pyautogui.click()
        cord = pyautogui.position()
    t2 = time.time()
    print(t2 - t1)


# 5 кликов в секунду
def paint_black2(x,y):
    t1 = time.time()
    #pyautogui.click(x,y)
    pyautogui.moveTo(x,y)
    cord = pyautogui.position()  
    y_new = y
    while cord[1] < 715: #518
        if keyboard.is_pressed('Ctrl'):
          return

        print(x,y)
        pyautogui.dragTo(x+5,y_new) 
        y_new += 1
        pyautogui.moveTo(x,y_new)
        cord = pyautogui.position() 
    
    t2 = time.time()
    print(t2 - t1)

# функция для работы с изображением в paint
def paint_image(x,y):
    t1 = time.time()
    pyautogui.moveTo(x,y)
    cord = pyautogui.position()
    y_new = y
    #colorD = (0,0,0)

    # закрашиваем изображение в paint попиксельно
    while cord[1] < 518 : #518
        if keyboard.is_pressed('Ctrl'):
          return

        colorD = pyautogui.pixel(x,y_new)
        print(x,y_new,colorD)

        x_new = x
        while True:
            if not colorD == (255,255,255):
                pyautogui.click(x_new,y_new)  
            x_new += 1
            colorD = pyautogui.pixel(x_new,y_new)
            print(x_new,y_new,colorD)
            if x_new > 900:
                break
            
            if keyboard.is_pressed('Ctrl'):
                break
   
        y_new += 1
        pyautogui.moveTo(x,y_new)
        cord = pyautogui.position() 
      

    t2 = time.time()
    print(t2 - t1)

# считывает изображение из paint
def paint_image_read(x,y):
    t1 = time.time()
    pyautogui.moveTo(x,y)
    cord = pyautogui.position()
    y_new = y


    Result = []
    while cord[1] < 255:
        if keyboard.is_pressed('Ctrl'):
          return
    
        colorD = pyautogui.pixel(x,y_new)
        #print(x,y_new,colorD)

        x_new = x
        res = []
        while True:
            if not colorD == (255,255,255):
                res.append(colorD)
            x_new += 1
            colorD = pyautogui.pixel(x_new,y_new)

            if x_new > 900:
                break        
            if keyboard.is_pressed('Ctrl'):
                break

        Result.append(res)
        y_new += 1
        pyautogui.moveTo(x,y_new)
        cord = pyautogui.position() 


    t2 = time.time()
    print(t2 - t1)
    return Result

# рисует изображение в paint
def paint_image_draw(Image):
    #img = Image.new('RGB', (250, 250), (255, 0, 0))
    #img.show()
    for res1 in Image:
        for res2 in res1:
            print(res2)

def test():
    # создание и отображение нового изображения(красного квадрата)
    img = Image.new('RGB', (250, 250), (255, 0, 0))
    #img.show()
   
    image = Image.open('1.jpg') # открываем изображение
    a = np.asarray(image) # считываем его в массив numpy
    image2 = Image.fromarray(a) # воссоздаём изображение из массива
    #image2.show() # отображаем изображение


    im3 = Image.effect_mandelbrot((1000,1000),(20,10,70,100),20)
    im4 = Image.effect_noise((500,500),82) # гауссовский шум
    im5 = Image.linear_gradient('L') # градиент от черного к белому
    im5.show()

    # накладывание  гауссовский шума на изображение
    image3 = image2.filter(ImageFilter.GaussianBlur(3))
    #image3.show()

    spisok = image.getcolors(maxcolors=1000000) # список цветов изображения
    print(len(spisok)) # количество цветов

    # получение значения каждого пикселя изображения
    print('PIL.IMAGE')
    t1 = time.time()
    Result = []
    for i in range(0,1920):
        for j in range(0,1080):
            pix = image.getpixel((i,j))
            Result.append((i,j,pix))
    t2 = time.time()
    print(t2 - t1)

    #print('pyautogui')
    #t1 = time.time()
    #for i in range(0,1920):
        #for j in range(0,1080):
        #pix = pyautogui.pixel(i,1)
    #t2 = time.time()
    #print(t2 - t1)

    # PIL.IMAGE выполянется в 1500 раза! быстрее чем pyautogui

    # вставляем одно изображение в другое изображение
    #image_new = image2
    #image_new.paste(img,(200,500))
    #image_new.show()

    # попикcельное! закрашивание изображения черным цветом(работает значительно быстрее чем серез манипуляции с мышкой в pyautogui)
    t1 = time.time()
    image_new = image2
    pix_black = Image.new('RGB',(1,1),(0,0,0))
    for i in range(0,1920):
        for j in range(0,1080):
            image_new.paste(pix_black,(i,j))
    t2 = time.time()
    image_new.show()
    print(t2 - t1)

    # восстановление изображения по пикселям
    # Result - список кортежей цветов всех пикселей которые мы получили ранее из изображения image
    image_new2 = image_new
    for i,j,im in Result:
        pix = Image.new('RGB',(1,1),(im[0],im[1],im[2]))
        image_new2.paste(pix,(i,j))

    image_new2.show()

    # игра с гауссовскими шумами разной интенсивности(значение sigma)
    #t1 = time.time()
    #image_new = image2
    #sigma = 1
    #pix_gauss = Image.effect_noise((5,5),sigma) # пиксель гауссовского шума
    #for i in range(0,1920,5):
    #    for j in range(0,1080,5):
    #        image_new.paste(pix_gauss,(i,j))
    #    sigma += 1
    #    pix_gauss = Image.effect_noise((5,5),sigma)

    #t2 = time.time()
    #image_new.save('gauss_5.png')
    #image_new.show()
    #print(t2 - t1)



#paint_black(5,175)
#paint_black2(5,175) 
#click_speed3()
#paint_image(5,250)
#Image = paint_image_read(5,250)


test()
img = Image.new('RGB', (250, 250), (255, 0, 0))
img.show()
paint_image_draw(img)

pass


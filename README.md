# Bigram Language Model
 Биграмма , если кратко обьяснить это - последовательность из двух последовательных элементов в слове.
 Например в слове "Dilnaz" дает нам - '^D', 'Di', 'il', 'ln', 'na', 'az', 'z$'
 (^ и $ — начало и конец слова.)
 Буквенные биграммы используются для лучшего понимания того, какие пары букв чаще всего встречаются в слове. Это может помочь, например, предсказать следующее слово в    предложении или определить, на каком языке написано предложение.
 Моя задача была сделать так чтобы через bigram генерировать слово вытягивая рандомно разные буквы , в то же время считать вероятность повтора существующих Биграмм
# Это интерфейс данной задачи :
![Screenshot_1](https://user-images.githubusercontent.com/118353735)
# Когда выбираем функционал 1 : Value "chose_name" выдает нам готовое слово , сделанное из рандомных букв под всевозможные генерации . 
![Screenshot_2](https://user-images.githubusercontent.com/118353735/236491557-9c75266c-7ec0-40c0-825e-fb4979a75183.png)
# Когда выбираем функционал 2 : Value " bigram_in_console " показывает нам вероятность частоты всех существующих биграмм для создания именных слов и иллюстрирует это все в таблице .
![Screenshot_3](https://user-images.githubusercontent.com/118353735/236493494-ddd8c77f-0fd1-4c21-bb66-43a464d8de77.png)
# Когда выбираем функционал 3 : Value " bigram_in_picture "  - открывает новое окно , а точнее PNG-файл чтобы рассмотреть вероятность всех биграмм в процентах .
![Screenshot_4](https://user-images.githubusercontent.com/118353735/236494796-e6a583da-57fe-46bf-80ca-b2062b37bab8.png)
# Когда выбираем функционал 4 : Value " bigram_in_graph" - открывает теперь окно через pycharm , и показывает нам в формате графики (а точнее диаграммы) всех вероятностей .
![Screenshot_5](https://user-images.githubusercontent.com/118353735/236495844-2bbc41d5-49ee-4de6-88d2-1ed9ed93ebbb.png)
# Так как мы использовали функцию : While(True) , это будет повторятся пока мы не получим желаемое в конце концов . 

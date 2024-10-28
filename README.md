# TESTING APP for LOGIKA LECTORS COURSE from Ruslan Yupyn
This is an kivy application for demonstration my scills that I got from votching webinars

## GOAL

The origin description of task was look like that:

```
Необхідно розробити додаток з декількома екранами, комбінацією лейаутів, застосувати параметри size_hint та pos_hint для налаштування віджетів і використати додаткові фішки, які ми обговорювали на вебінарах. Розроблений додаток треба завантажити на GitHub у публічний репозиторій і написати посилання на нього в це поле (наприкінці вебінару № 3 міститься опис практичного завдання https://youtu.be/AdWGTsu-IS4?si=bRbFSG1NNBPg1eB6).
```

## Project hierarhy

```
PythonPro2LogikaTestingRuslanYupyn/
│
├── main.py
```

## Classes description

```MenuScreen``` this is a class-extension for Screen kivy module class that contains description label about this project and 4 buttons below. Each of button shows their own screen with different dirrection transition style.

```NextScreen``` this is also class-extension for next screen with customizable back dirrection to menu screen button. Also it contains label on the top that describu current screen.

```TestApp``` this is a class-extension of App class that set root ScreenManager widget and screens those shoud managed by it.



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

```MenuScreen```: This class extends the Screen class from the Kivy module. It contains a descriptive label about this project and four buttons below. Each button shows its own screen with a different transition direction.

```NextScreen```: This class also extends the Screen class and includes a customizable back direction button to the menu screen. It contains a label at the top that describes the current screen.

```TestApp```: This class extends the App class, sets the root ScreenManager widget, and manages the screens.

## CHANGELOGS

To see changelogs, follow this [link](./CHANGELOGS.md).
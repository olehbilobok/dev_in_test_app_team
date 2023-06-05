### Ajax Systems, Python developer in test for Application team
Для выполнения тестового задания Вам нужно установить приложение Ajax Systems на телефон (если у вас нет реального андроид устройства то вы можете использовать эмулятор).

### Описание

Тесты выполнялися на андроид эмуляторе Pixel 4 API 29 Emulator. Все тесты прошли проверку со статусом PASSED

### Запустить проект локально

1) Используя Android Studio выбрать и настроить эмулятор
2) Запустить appium server

3) Клонировать проект 

```bash
git clone https://github.com/olehbilobok/dev_in_test_app_team.git
```
4) Перейти в папку проекта 

```bash
cd dev_in_test_app_team

```
5) Установить зависимости

```bash
pip install -r requirements.txt

```
6) В файле .env указать абсолютный путь к adb (используется для динамического определения udid телефона или эмулятора)

7) (Опционально) Поместить файл Ajax Security System_2.28.0_Apkpure.apk в директорию dev_in_test_app_team. Файл может использоваться в файле android_utils.py в функции android_get_desired_capabilities для установки приложения перед выполнением тестов. 

8) Запустить тесты

```bash
pytest -v tests/

```

### Задание
1) Написать базовый функционал для работы с приложением (поиск элемента, клик элемента и тд).
2) Написать тест логина пользователя в приложение (позитивный и негативные кейсы).
3) Использовать параметризацию.
4) Закомитить выполненное задание на гитхаб.

### Дополнительное задание (опционально)
1) *Реализовать логирование теста.
2) *Реализовать динамическое определение udid телефона через subprocess
3) **Написать на проверку элементов SideBar (выезжающее меню слева).

### Полезные ссылки
1) Приложение - https://play.google.com/store/apps/details?id=com.ajaxsystems
2) Работа с реальным телефоном - https://developer.android.com/studio/command-line/adb
3) Настройка эмулятора - https://developer.android.com/studio/run/emulator
4) Настройка аппиума - https://appium.io/docs/en/about-appium/getting-started/#installing-appium
5) Инспектор приложения - https://appium.io/docs/en/drivers/android-uiautomator2/

### Login credentials
login - qa.ajax.app.automation@gmail.com
password - qa_automation_password

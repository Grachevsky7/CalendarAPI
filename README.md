# CalendarAPI
Проект представляет собой веб-сервис для создания заметок по календарным дням

Запуск проекта:
1.Создание виртуального окружения.
  Для создания виртуального окружения, перейдите в директорию проекта и выполните:
  python -m venv venv
2.Активация виртуальной среды.
  В зависимости от операционной системы, используйте соответствующую команду для активации виртуальной среды:
  venv\Scripts\activate.bat- для Windows;
  source venv/bin/activate - для Linux и MacOS.
3. Установка зависимостей:
  pip install -r requirements.txt
4. Запуск проекта:
  python api.py

Тестирование проекта:
HTTP методы c URL и примерами запросов:
POST: localhost:5000/api/v1/calendar/ - "1|2021-12-01|title|text" #Создание заметки
GET: localhost:5000/api/v1/calendar/ #Вывод списка заметок
GET: localhost:5000/api/v1/calendar/1 #Чтение конкретной записи, в данном случае id заметки = 1
PUT: localhost:5000/api/v1/calendar/1 - "1|2021-12-01|another_title|another_text" #Изменение заметки с id = 1
DELETE: localhost:5000/api/v1/calendar/1 #Удаление заметки с id = 1

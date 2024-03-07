# CalendarAPI
Проект представляет собой веб-сервис для создания заметок по календарным дням

---

### Запуск проекта:
__1.Создание виртуального окружения.__ <br />
  Для создания виртуального окружения, перейдите в директорию проекта и выполните:<br />
  python -m venv venv<br />
__2.Активация виртуальной среды.__ <br />
  В зависимости от операционной системы, используйте соответствующую команду для активации виртуальной среды:<br />
  venv\Scripts\activate.bat- для Windows;<br />
  source venv/bin/activate - для Linux и MacOS.<br />
__3. Установка зависимостей:__<br />
  pip install -r requirements.txt<br />
__4. Запуск проекта:__<br />
  python api.py<br />

---

### Тестирование проекта:<br />
__HTTP методы c URL и примерами запросов:__<br />
POST: localhost:5000/api/v1/calendar/ - "1|2021-12-01|title|text" #Создание заметки<br />
GET: localhost:5000/api/v1/calendar/ #Вывод списка заметок<br />
GET: localhost:5000/api/v1/calendar/1 #Чтение конкретной записи, в данном случае id заметки = 1<br />
PUT: localhost:5000/api/v1/calendar/1 - "1|2021-12-01|another_title|another_text" #Изменение заметки с id = 1<br />
DELETE: localhost:5000/api/v1/calendar/1 #Удаление заметки с id = 1

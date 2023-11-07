# Сервис получения вопросов для викторины

## Что делает сервис:

- принимает POST-запрос с количеством вопросов
- отправляет запрос к публичному API https://jservice.io/api/ на получение вопросов в количестве, указанном в POST запросе
- сохраняет в БД вопросы, которых еще не было
- осуществляет повторный запрос к внешнему API в случае, если в ответ на запрос поступили вопросы, которые уже есть в БД
- возвращает предыдущий сохранённый вопрос для викторины

## Технологии проекта:

- Python 3.11.4
- Docker 24.0.6
- Docker Compose v2.22.0
- Postgres 16.0
- FastAPI 0.103.2
- Uvicorn 0.23.2
- SqlAalchemy 2.0.22
- Pydantic 2.4.2
- Alembic 1.12.0

## Локальный запуск проекта:

Для запуска проекта необходимо, чтобы на локальном компьютере были установлены Python 3.11.4 и Docker 24.0.6

- Клонируем репозиторий: **git clone [Сервис получения вопросов для викторины](https://github.com/Olga-Zholudeva/Questions-for-the-quiz.git)**
- Создаем и заполняем файл .env по образцу из: **.env.example**
- Cоздаем виртуальное окружение: **python3.11 -m venv venv**
- Активируем виртуальное окружение: **. venv/bin/activate**
- Устанавливаем зависимости из файла requirements.txt: **pip install -r requirements.txt**
- Запускаем на локальном компьютере Docker и выполняем команду для создания и запуска БД: **docker compose up -d**
- Применяем миграции: **alembic upgrade head**
- Запускаем сервер: **uvicorn main:app**

После запуска сервера документация к API будет доступна по адресу: http://127.0.0.1:8000/docs   
В том числе по данному адресу доступна возможность отправки POST-запроса

Пример POST-запроса к API:

{    
  "count": 2   
}    

Пример ответа:

{
  "created": "2022-12-30",   
  "question": "You \"betta\" believe this type of \"fighting fish\" will even attack its own image in a mirror",   
  "question_id": 166552,   
  "id": 1,   
  "ancwer": "a Siamese fighting fish"   
}   

## Проект выполнен:   
Ольга Жолудева

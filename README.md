# API Tarantool KV-storage

## Запуск

1. Клонируйте репозиторий:
```
git clone https://github.com/promaxV/tarantool-kv-storage.git
cd tarantool-kv-storage
```
2. Запустите с помощью Docker Compose:
```
docker-compose up -d
```
API будет доступен по адресу `http://localhost:8000`.

## API Документация

### Получение токена авторизации

Endpoint: `POST /api/login`

Запрос:
```json
{
    "username": "admin",
    "password": "presale"
}
```
Ответ:
```json
{
    "token": "your_generated_token"
}
```
### Запись данных
Endpoint: `POST /api/write`
Заголовки:
```
Authorization: Bearer your_generated_token
```
Запрос:
```json
{
    "data": {
        "key1": "value1",
        "key2": "value2",
        "key3": 1
    }
}
```
Ответ:
```json
{
    "status": "success"
}
```
### Чтение данных
Endpoint: `POST /api/read`
Заголовки:
```
Authorization: Bearer your_generated_token
```
Запрос:
```json
{
    "keys": ["key1", "key2", "key3"]
}
```
Ответ:
```json
{
    "data": {
        "key1": "value1",
        "key2": "value2",
        "key3": 1
    }
}
```

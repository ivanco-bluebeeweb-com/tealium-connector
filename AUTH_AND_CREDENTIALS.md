# Tealium Connector — Auth & Credentials Standard

**Compliance:** AUTH_AND_CREDENTIALS_STANDARD.md (B1–B10)

## Схема аутентификации
- **Метод:** Tealium API Bearer Token (POST /v2/auth)
- **Хранение:** Секреты сохраняются изолированно в хранилище секретов платформы Imperal.
- **Валидация:** При сохранении ключа выполняется тестовый запрос `GET /v2/event`.
- **Отключение:** Удаление локальных ключей без воздействия на аккаунт вендора.

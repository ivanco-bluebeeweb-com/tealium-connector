# Tealium Connector — Discovery

**Vendor:** Tealium (https://tealium.com)  
**API Base URL:** `https://api.tealiumiq.com/v2`  
**Authentication:** Tealium API Bearer Token (POST /v2/auth)

## Архитектура API
- **Ключевые сущности:** профили и аккаунты, источники EventStream, атрибуты посетителей AudienceStream, коннекторы действий
- **Формат обмена данными:** JSON / HTTPS REST.
- **Обработка ошибок:** Стандартные HTTP-коды (400, 401, 403, 404, 429, 500) с типизацией ответа.
- **Тестовая точка проверки подключения:** `GET /v2/event`.

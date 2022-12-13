Проект сохраняет метки данных о просмотрах фильмов
из приложения (fast_api) в аналитическое хранилище.


Предполагается, что информация о метке просмотра фильма приложение получает из фронтенда.
Метка просмотра - формат timestamp.
Имея информацию о том, сколько длится фильм, и сколько посмотрел конкретный пользователь,
можно сделать вывод - досмотрел пользователь до конца фильм или нет.

Самый просматриваемый фильм - фильм, у которого процент досмотренности самый высокий.


# Запуск проекта
`docker network create ugc_service`

`docker-compose -f docker-compose.yml -f docker-compose.kafka.yml up`

[Переменные окружения](/fast_api/src/core/.env.example)

### Описание архитектуры
[as_is](uml/as_is.drawio)

as_is в формате [png](uml/as_is.png)

[to_be](uml/to_be.drawio)

to_be в формате [png](uml/to_be.png)

### Spark Jupyter

Задание №1 - рассчитанный [rating by reviews](/spark_data/combined/rating_by_reviews)

Задание №2 - в [products.csv](/spark_data/combined/products_with_ratings.csv) добавлена колонка "rating_by_reviews"

[Код](/spark_data/Ice_cream_rating.ipynb)

### ClickHouse

[Схема](/click_house/clickhouse_schema.drawio) кластера 

В формате [.png](/click_house/click_house_schema.png)

# Загрузка данных из Kafka в Clickhouse

[API](/fast_api) - загрузка данных в Kafka.

[ETL](/etl) - перегрузка данных из Kafka в ClickHouse






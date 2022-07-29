# Проектная работа 8 спринта

[Репозиторий ugc_sprint_1 (проектная работа 8-го спринта)](https://github.com/NataliaLaktyushkina/ugc_sprint_1)

# Запуск проекта
`docker compose -f docker-compose.spark.python.yml -f docker-compose.kafka.yml`

# Описание архитектуры
[as_is](uml/as_is.drawio)

as_is в формате [png](uml/as_is.png)

# Spark Jupyter

Задание №1 - рассчитанный [rating by reviews](/spark_data/combined/rating_by_reviews)

Задание №2 - в [products.csv](/spark_data/combined/products_with_ratings.csv) добавлена колонка "rating_by_reviews"

[Код](/spark_data/Ice_cream_rating.ipynb)

# ClickHouse

Разберите до конца конфигурационный файл и опишите процесс добавления, хранения, поиска данных в кластере, построенном в уроке. Нарисуйте схему кластера с таблицами для каждого сценария:
 - В какой базе и таблице будут хранится данные?
 - В какую базу и таблицу реплицироваться?
 - В какую базу и таблицу будут приходить запросы от дистрибутивной таблицы?
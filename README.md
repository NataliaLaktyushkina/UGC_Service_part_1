# Проектная работа 8 спринта

[Репозиторий ugc_sprint_1 (проектная работа 8-го спринта)](https://github.com/NataliaLaktyushkina/ugc_sprint_1)

# Запуск проекта
`docker compose -f docker-compose.spark.python.yml -f docker-compose.kafka.yml`

# Описание архитектуры
[as_is](uml/as_is.drawio)

as_is в формате [png](uml/as_is.png)

# Spark Jupyter

Задание №1 - рассчитанный [rating by reviews](/data/combined/rating_by_reviews)

Задание №2 - в [products.csv](/data/combined/products_with_ratings.csv) добавлена колонка "rating_by_reviews"

[Код](/data/Ice_cream_rating.ipynb)
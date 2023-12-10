from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product


class Products:
    pass


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Список категорий для добавления в бд
        categories = [

            {'category_name': 'Боты', 'description': "Бот, специальная программа, выполняющая автоматически и/или по "
                                                     "заданному расписанию какие-либо действия через интерфейсы, "
                                                     "предназначенные для людей."},
            {'category_name': 'Рассылки', 'description': 'Рассылка — это отправка одного уведомления большому '
                                                         'количеству получателей'},
            {'category_name': 'Веб-приложения', 'description': 'Веб-приложение — клиент-серверное приложение, '
                                                               'в котором клиент взаимодействует с веб-сервером при '
                                                               'помощи браузера.'},
            {'category_name': 'Устройства', 'description': 'Устройство — рукотворный объект (прибор, механизм, '
                                                           'конструкция,установка, аппарат, машина) со сложной '
                                                           'внутренней структурой, созданный для выполнения '
                                                           'определённых функций, обычно в области техники.'},
        ]

        # Очистка таблицы Category
        Category.objects.all().delete()

        # Сброс автоинкремента для поля `pk` в таблице Category
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")

        # Список экземпляров класса Category
        categories_for_create = []
        for category in categories:
            categories_for_create.append(Category(**category))

        # Добавление категорий в базу данных
        Category.objects.bulk_create(categories_for_create)

        # Список продуктов для добавления в БД
        products = [

            {'product_name': 'Стрим Анонсер',
             'description': 'Уведомляет о начале ваших трансляций с различных платформ',
             'category': categories_for_create[0], 'price': '2500'},  # Категория боты
            {'product_name': 'Удобный сервис рассылок',
             'description': 'Позволяет в пару кликов оповестить большое кол-во пользователей через почтовые сервисы',
             'category': categories_for_create[1], 'price': '5000'},  # Категория рассылки
            {'product_name': 'Новости и точка',
             'description': 'Новостной сайт',
             'category': categories_for_create[2], 'price': '3800'},  # Категория веб-приложения
            {'product_name': 'Стрим Дека',
             'description': 'Макро клавиатура предназначенная упростить управление вашей трансляцией через программу OBS',
             'category': categories_for_create[3], 'price': '6500'},  # Категория устройства

        ]

        # Очистка таблицы Product
        Product.objects.all().delete()

        # Сброс автоинкремента для поля `pk` в таблице Product
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1")

        # Список экземпляров класса Product
        products_for_create = []
        for product in products:
            products_for_create.append(Product(**product))

        # Добавление продуктов в базу данных
        Product.objects.bulk_create(products_for_create)

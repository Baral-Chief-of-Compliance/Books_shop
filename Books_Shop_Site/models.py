from django.db import models
from django.urls import reverse


class Book(models.Model):
    Detective = "Детектив"
    Science_fiction = "Фантастика"
    Adventures = "Приключения"
    Novel = "Роман"
    Scientific_book = "Научная книга"
    Folklore = "Фольклор"
    Humor = "Юмор"
    Reference_book = "Справочная книга"
    Poetry = "Поэзия"
    Children_book = "Детская книга"
    Documentary_literature = "Документальная литература"
    Business_literature = "Деловая литература"
    Religious_literature = "Религиозная литература"
    Educational_book = "Учебная книга"
    Books_about_psychology = "Книги о психологии"
    Hobby = "Хобби"
    Foreign = "Зарубежная"
    Equipment = "Техника"

    CHOISE_GROUP = {
        (Detective, "Детектив"),
        (Science_fiction, "Фантастика"),
        (Adventures, "Приключения"),
        (Novel, "Роман"),
        (Scientific_book, "Научная книга"),
        (Folklore, "Фольклор"),
        (Humor, "Юмор"),
        (Reference_book, "Справочная книга"),
        (Poetry, "Поэзия"),
        (Children_book, "Детская книга"),
        (Documentary_literature, "Документальная литература"),
        (Business_literature, "Деловая литература"),
        (Religious_literature, "Религиозная литература"),
        (Educational_book, "Учебная книга"),
        (Books_about_psychology, "Книги о психологии"),
        (Hobby, "Хобби"),
        (Foreign, "Зарубежная"),
        (Equipment, "Техника"),
    }

    name_of_book = models.CharField("Название книги", max_length=128)
    description = models.TextField("Описание книги")
    price = models.IntegerField("Цена")
    availability = models.BooleanField("Наличие")
    group = models.CharField("Жанр", max_length=100,choices=CHOISE_GROUP,default=Detective)
    img = models.ImageField("Обложка", default='Books_Shop_Site/no_image.jpg', upload_to='Books_Shop_Site/product_image')

    def _str_(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse ("book-detail", kwargs={"pk": self.id})

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

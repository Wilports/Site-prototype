from django.db import models
from django.urls import reverse

class Orders(models.Model):

    email = models.EmailField("email", blank=True)
    telephone = models.CharField("Телефон", max_length=50)
    name = models.CharField("ФИО", max_length=50)
    organization = models.CharField("Организация (если есть)", max_length=50, blank=True)
    full_text = models.TextField("описание заказа", blank=True)
    status = models.CharField("Статус заказа", max_length=50, default="НА ПРОВЕРКЕ")
    time = models.DateTimeField("Дата добавления заказа", auto_now_add = True)

    class Meta:
        verbose_name = "Управление всеми заказами"
        verbose_name_plural = "Управление всеми заказами"

class Comments(models.Model):

    email = models.EmailField("email")
    name = models.CharField("Имя или название организации", max_length=50)
    full_text = models.TextField("Отзыв")
    time = models.DateTimeField("Дата добавления отзыва", auto_now_add = True)

    class Meta:
        verbose_name = "Редактирование комментариев"
        verbose_name_plural = "Редактирование комментариев"

class News(models.Model):

    title = models.CharField("Заголовок новости", max_length=100)
    time = models.DateTimeField("Дата добавления", auto_now_add = True)
    full_text = models.TextField("Текст новости")
    image = models.ImageField("Иллюстрация", upload_to="images/%Y/%m/%d")
    published = models.BooleanField("Публикация", default=False)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('post',  args=(self.slug,))

    class Meta:
        verbose_name = "Добавить или изменить новость"
        verbose_name_plural = "Добавить или изменить новость"

class Trucks(models.Model):

    tipe = models.CharField("Тип грузового автомобиля", max_length=100)
    image = models.ImageField("Иллюстрация", upload_to="images/%Y/%m/%d")
    tonnage = models.CharField("Тоннаж", max_length=50)
    model = models.CharField("Модель", max_length=50)
    price = models.CharField("Цена в руб/км", max_length=50)

    class Meta:
        verbose_name = "Машины и расценки"
        verbose_name_plural = "Машины и расценки"

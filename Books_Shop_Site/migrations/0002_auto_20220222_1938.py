# Generated by Django 3.2.3 on 2022-02-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books_Shop_Site', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterField(
            model_name='book',
            name='availability',
            field=models.BooleanField(verbose_name='Наличие'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Описание книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='group',
            field=models.CharField(choices=[('Фантастика', 'Фантастика'), ('Научная книга', 'Научная книга'), ('Справочная книга', 'Справочная книга'), ('Учебная книга', 'Учебная книга'), ('Деловая литература', 'Деловая литература'), ('Книги о психологии', 'Книги о психологии'), ('Техника', 'Техника'), ('Документальная литература', 'Документальная литература'), ('Религиозная литература', 'Религиозная литература'), ('Фольклор', 'Фольклор'), ('Поэзия', 'Поэзия'), ('Роман', 'Роман'), ('Юмор', 'Юмор'), ('Хобби', 'Хобби'), ('Приключения', 'Приключения'), ('Зарубежная', 'Зарубежная'), ('Детектив', 'Детектив'), ('Детская книга', 'Детская книга')], default='Детектив', max_length=100, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(default='Books_Shop_Site/no_image.jpg', upload_to='Books_Shop_Site/product_image', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name_of_book',
            field=models.CharField(max_length=128, verbose_name='Название книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]
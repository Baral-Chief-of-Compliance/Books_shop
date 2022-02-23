# Generated by Django 3.2.3 on 2022-02-23 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books_Shop_Site', '0002_auto_20220222_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='group',
            field=models.CharField(choices=[('Фантастика', 'Фантастика'), ('Документальная литература', 'Документальная литература'), ('Научная книга', 'Научная книга'), ('Поэзия', 'Поэзия'), ('Учебная книга', 'Учебная книга'), ('Книги о психологии', 'Книги о психологии'), ('Деловая литература', 'Деловая литература'), ('Техника', 'Техника'), ('Детская книга', 'Детская книга'), ('Детектив', 'Детектив'), ('Юмор', 'Юмор'), ('Справочная книга', 'Справочная книга'), ('Фольклор', 'Фольклор'), ('Религиозная литература', 'Религиозная литература'), ('Хобби', 'Хобби'), ('Зарубежная', 'Зарубежная'), ('Роман', 'Роман'), ('Приключения', 'Приключения')], default='Детектив', max_length=100, verbose_name='Жанр'),
        ),
    ]

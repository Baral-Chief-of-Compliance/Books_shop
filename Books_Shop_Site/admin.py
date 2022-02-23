from django.contrib import admin
from Books_Shop_Site.models import Book
from django.utils.safestring import mark_safe


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name_of_book", "get_img", "availability", "price", )
    search_fields = ("name_of_book",)

    def get_img(self, obj):
        return mark_safe(f'<img src ={obj.img.url} width="100"  height = "120">')

    get_img.short_description = "Изображение"

from django.contrib import admin
from .models import Title, Category, Genre, User, Comment, Review


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'username', 'email', 'bio', 'role'
    )
    list_filter = ('role',)
    empty_value_display = '-пусто-'
    model = User


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'slug'
    )
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    empty_value_display = '-пусто-'


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'category', 'genre', 'description')
    search_fields = ('name',)
    list_filter = ('year',)
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'slug'
    )
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    empty_value_display = '-пусто-'


admin.site.register(User)
admin.site.register(Title)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Comment)

from django.contrib import admin
from p_library.models import Book, Author, Publishing


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    # @staticmethod
    # def author_full_name(obj):
    #     return obj.author.full_name

    # author_full_name.admin_order_field = 'publishing'

    list_display = ('title', 'publishing', 'author_full_name')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'publishing', 'price')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    
    @staticmethod
    def author_full_name(obj):
        return obj.full_name
    
    list_display = ('author_full_name', )

@admin.register(Publishing)
class PublishingAdmin(admin.ModelAdmin):
    
    @staticmethod
    def publishing_name(obj):
        return obj.publishing_name

    list_display = ('publishing_name', )
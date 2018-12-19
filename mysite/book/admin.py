from django.contrib import admin

from .models import Author
from .models import BookInstance
from .models import Genre
from .models import Book
# Register your models here.

# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Genre)

# ******************** add a BookInstance simultaneously when we add a Book:
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name',
              'last_name',
             ('date_of_birth', 'date_of_death')
             ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

    # display_genre has (many to many) Relation so we must view it in list this way:
    # another way of this is to display in the model class which it was created 
    def display_genre(self, obj):
        return ', '.join([genre.name for genre in obj.genre.all()[:3]])

    display_genre.short_description = 'Genre'


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        # None is the name of the field which is givend as 'Availability' in the next field:
        (None, {
            'fields': ('book',
                       'imprint',)
        }),
        # Second section:
        ('Availability', {
            'fields': ('status',
                       'due_back')
        })
    )
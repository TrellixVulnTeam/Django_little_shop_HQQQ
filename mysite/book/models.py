from django.db import models
import uuid


    # Programmed by Alireza Bagheri


class Genre(models.Model):
    name = models.CharField(max_length = 200, help_text = 'Enter a book genre (e.g. Science Fiction, Poetry etc...)')


    def __str__(self):
        return self.name

class Book(models.Model):
    """
        Model Representing a book but not a specific copy of one
    """

    title = models.CharField(max_length = 200)
    summary = models.CharField(max_length = 1000, help_text = 'Enter a brief description of the book')
    isbn = models.CharField(max_length = 13, help_text = '13 char ISBN <a href="https://www.isbn-international.org/">What is ISBN? </a>')

    # every book has several genre and every genre can have several books(ManyToMany Relation), the Genre class must be declared above
    genre = models.ManyToManyField(Genre, help_text = 'Select a genre for this book')
    
    # every author can have several books(One To Many Relation)
    # books can have only one author but authors can have multiple books(One To Many Relation)
    author = models.ForeignKey('Author', on_delete = models.SET_NULL, null = True)

     
    # Programmed by Alireza Bagheri

    def __str__(self):
        return self.title


class Author(models.Model):
    """
    Model Representing an Author
    """

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    # null: can have no value, blank: user is free wheather to enter this field or not
    date_of_birth = models.DateField(null = True, blank = True)
    date_of_death = models.DateField('Died', null = True, blank = True)

    class Meta:
        ordering = ["last_name", "first_name"]


    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)


class BookInstance(models.Model):
    # A more complex id from the default id of the ORM
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,
                        help_text = 'Unique id for only this book across the whole library.')

    # has a link to the calss Book which is declared Above
    book = models.ForeignKey('Book', on_delete = models.SET_NULL, null = True)
    imprint = models.CharField(max_length = 200)
    # when the book exactly was delivered to the library by a customer
    due_back = models.DateField(null = True, blank = True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length = 1,
                                choices = LOAN_STATUS,
                                blank = True,
                                default = 'm',
                                help_text = 'Book availability')

    class Meta:
        ordering = ["due_back"]

    
    def __str__(self):
        return '{0} ({1})'.format(self.id, self.book.title)
from django.shortcuts import render, Http404

from django.views import generic

    # Programmed by Alireza Bagheri


from .models import Author
from .models import Book
from .models import BookInstance
from .models import Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instancces = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()
    num_author = Author.objects.count()


    context = {
        'num_books': num_books,
        'num_instancces': num_instancces,
        'num_instances_available': num_instances_available,
        'num_author': num_author
    }

    return render(request, 'book/index.html', context)
    
# Opens the media/templates/book/book_list.html page
class BookListView(generic.ListView):
    model = Book
    # context_object_name = "my_book_list"
    # template_name = 'book/book_list.html'
    # queryset = Book.objects.filter(title__icontains = 'django')[:5]
    paginate_by = 5

# Opens the media/templates/book/book_detail.html page
class BookDetailView(generic.DetailView):
    model = Book
# we could write two lines above like this: (if we don't want to use generic based views)

# def book_detail_view(request, pk):
#     try:
#         book_id = Book.objects.get(pk = pk)
#     except Book.DoesNotExist:
#         raise Http404("Book does not exist.")

    #book_id = get.object_or_404(Book, pk = pk)

    # return render(
    #     request,
    #     'book/book_detail.html',
    #     context={'book': book_id}
    # )


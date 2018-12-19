from django.urls import path, re_path

from . import views

app_name = 'book'

urlpatterns = [
    path('', views.index, name = 'index'),
    # Using a generic view for routing target: (".as_view()")
    path('list', views.BookListView.as_view(), name = 'bookList'),

    # path('detail/<int:pk>', views.BookDetailView.as_view(), name = 'bookDetail'), #Regex Form next line:
    # pk = 1234... :
    re_path(r'^detail/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name = 'bookDetail'),
    # book/detail/[the-secret-id-found-here]:
    # re_path(r'^detail/(?P<uid>[-\w])$')
]
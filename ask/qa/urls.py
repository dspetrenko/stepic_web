from django.urls import path

from .views import test
from .views import main
from .views import popular
from .views import queation


urlpatterns = [
    path('', main),
    path('popular/', popular),
    path('login/', test),
    path('signup/', test),
    path('question/<int:id>/', queation),
    path('ask/', test),
    path('popular/', test),
    path('new/', test),
]

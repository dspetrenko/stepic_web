from django.urls import path

from .views import test
from .views import main
from .views import popular


urlpatterns = [
    path('', main),
    path('popular/', popular),
    path('login/', test),
    path('signup/', test),
    path('question/<int:id>/', test),
    path('ask/', test),
    path('popular/', test),
    path('new/', test),
]

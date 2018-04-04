from django.urls import path

from .views import test
from .views import main
from .views import popular
from .views import question


urlpatterns = [
    path('', main),
    path('popular/', popular),
    path('login/', test),
    path('signup/', test),
    path('question/<int:question_id>/', question),
    path('ask/', test),
    path('popular/', test),
    path('new/', test),
]

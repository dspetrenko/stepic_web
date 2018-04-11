from django.urls import path

from .views import test
from .views import main
from .views import popular
from .views import question
from .views import ask
from .views import signup


urlpatterns = [
    path('', main),
    path('popular/', popular),
    path('login/', test),
    path('signup/', signup),
    path('question/<int:question_id>/', question),
    path('ask/', ask),
    path('popular/', test),
    path('new/', test),
]

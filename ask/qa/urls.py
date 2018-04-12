from django.urls import path

from .views import test
from .views import main
from .views import popular
from .views import question
from .views import ask
from .views import signup
from .views import login_view


urlpatterns = [
    path('', main),
    path('popular/', popular),
    path('login/', login_view),
    path('signup/', signup),
    path('question/<int:question_id>/', question),
    path('ask/', ask),
    path('popular/', test),
    path('new/', test),
]

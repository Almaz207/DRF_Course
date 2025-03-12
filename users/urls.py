from rest_framework.routers import SimpleRouter
from django.urls import path

from users.apps import UsersConfig
from users.views import (
    PaymentsListApiView,
    PaymentsCreateApiView,
    PaymentsUpdateApiView,
    PaymentsRetrieveApiView,
    PaymentsDestroyApiView,
    PaymentsSerializer,
)

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lesson/", LessonListApiView.as_view(), name="lesson"),
    path("lesson/create", LessonCreateApiView.as_view(), name="lesson_create"),
    path("lesson/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_retrieve"),
    path("lesson/<int:pk>/update", LessonUpdateApiView.as_view(), name="lesson_update"),
    path(
        "lesson/<int:pk>/delete", LessonDestroyApiView.as_view(), name="lesson_delete"
    ),
]

urlpatterns += router.urls

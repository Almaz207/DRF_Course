from rest_framework.routers import SimpleRouter
from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import (
    CourseViewSet,
    LessonCreateApiView,
    LessonListApiView,
    LessonRetrieveApiView,
    LessonUpdateApiView,
    LessonDestroyApiView,
    SubscriptionView,
)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lesson", LessonListApiView.as_view(), name="lesson"),
    path("lesson/create", LessonCreateApiView.as_view(), name="lesson_create"),
    path("lesson/<int:pk>", LessonRetrieveApiView.as_view(), name="lesson_retrieve"),
    path("lesson/<int:pk>/update", LessonUpdateApiView.as_view(), name="lesson_update"),
    path(
        "lesson/<int:pk>/delete", LessonDestroyApiView.as_view(), name="lesson_delete"
    ),
    path("subscribe", SubscriptionView.as_view(), name="subscribe"),
]

urlpatterns += router.urls

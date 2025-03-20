from rest_framework.serializers import ModelSerializer, URLField, SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_youtubelink


class LessonSerializer(ModelSerializer):
    link = URLField(validators=[validate_youtubelink])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    count_of_lessons = SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_count_of_lessons(self, obj):
        return obj.lessons.count()


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["user", "course"]
        read_only_fields = ["user", "course"]

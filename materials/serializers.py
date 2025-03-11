from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
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

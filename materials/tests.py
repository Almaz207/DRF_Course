from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from materials.models import Course, Lesson, Subscription
from users.models import CustomUser


class CourseTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(first_name="userus", last_name="test", username="userus_test")
        self.course = Course.objects.create(name="Какой-то курс")
        Lesson.objects.all().delete()
        self.lesson = Lesson.objects.create(
            title="Первый урок",
            course=self.course,
            link="https://youtube.com/sample_video",
            owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        data = {
            "title": "Новый урок",
            "description": "Описание нового урока",
            "link": "https://youtube.com/sample_video_2",
            "course": self.course.id,
        }

        response = self.client.post("/course/lesson/create", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 2)

    def test_get_lessons(self):
        response = self.client.get("/course/lesson")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_update_lesson(self):
        data = {
            "title": "Второй урок",
            "description": "Описание второго урока",
            "link": "https://youtube.com/updated_video",
            "course": self.course.id,
        }
        response = self.client.put(f"/course/lesson/{self.lesson.id}/update", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, "Второй урок")

    def test_delete_lesson(self):
        response = self.client.delete(f"/course/lesson/{self.lesson.id}/delete")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 0)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="tekst@email.com")
        self.course = Course.objects.create(name="Курс по DRF")
        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):
        data = {"course_id": self.course.id}
        response = self.client.post("/course/subscribe", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.count(), 1)
        subscription = Subscription.objects.first()
        self.assertEqual(subscription.user, self.user)
        self.assertEqual(subscription.course, self.course)

    def test_unsubscribe_from_course(self):
        Subscription.objects.create(user=self.user, course=self.course)
        data = {"course_id": self.course.id}
        response = self.client.post("/course/subscribe", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subscription.objects.count(), 0)

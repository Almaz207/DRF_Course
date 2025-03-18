from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Название курса", help_text="Название курса"
    )
    preview = models.ImageField(
        upload_to="materials/preview",
        verbose_name="Превью",
        help_text="Превью",
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name="Описание курса", help_text="Описание курса"
    )

    owner = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="course",
        null=True,
        blank=True,
        verbose_name="Владелец",
        help_text="Укажите автора курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Название урока", help_text="Название урока"
    )
    preview = models.ImageField(
        upload_to="materials/preview",
        verbose_name="Превью",
        help_text="Превью",
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name="Описание урока", help_text="Описание урока", null=True, blank=True
    )
    link = models.URLField(max_length=200, verbose_name="ссылка", null=True, blank=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="lessons",
    )

    owner = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="lessons",
        null=True,
        blank=True,
        verbose_name="Владелец",
        help_text="Укажите автора урока",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} подписан на {self.course.name}"

    class Meta:
        unique_together = ('user', 'course')

from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify


class Skill(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=50, blank=True, null=True, verbose_name='Никнейм')
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Фамилия Имя')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='E-Mail')
    bio = models.TextField(blank=True, null=True, verbose_name='Биография')
    intro = models.CharField(max_length=100, blank=True, null=True, verbose_name='Основная специальность')
    image = models.ImageField(blank=True, null=True, default='profile/default.jpg', upload_to='profile')
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name='Город')
    skills = models.ManyToManyField(Skill, blank=True, verbose_name='Скилы')
    github = models.URLField(blank=True, null=True, verbose_name='GitHub')
    youtube = models.URLField(blank=True, null=True, verbose_name='YouTube')
    twitter = models.URLField(blank=True, null=True, verbose_name='Twitter')
    instagram = models.URLField(blank=True, null=True, verbose_name='Instagram')
    telegram = models.URLField(blank=True, null=True, verbose_name='Telegram')
    linkedin = models.URLField(blank=True, null=True, verbose_name='LinkedIn')
    website = models.URLField(blank=True, null=True, verbose_name='Мой сайт')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        ordering = ['created_at']

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = [
            'is_read',
            '-created_at',
        ]

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    """Модель пользователя"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name','last_name','phone_number', 'password')

    email = models.EmailField(
        'Электронная почта',
        unique=True,
        blank=False,
        max_length=100,
        help_text='Введите вашу электронную почту',
    )
    username = models.CharField(
        'Логин',
        unique=True,
        max_length=100,
        help_text='Введите уникальный логин',
        validators=[
            UnicodeUsernameValidator
        ]
    )
    password = models.CharField(
        'Пароль',
        max_length=100,
        help_text='Введите пароль',
    )
    first_name = models.CharField(
        'Имя',
        max_length=100,
        blank=False,
        help_text='Введи вашем имя',
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=100,
        blank=False,
        help_text='Введите вашу фамилию',
    )
    phone_number = PhoneNumberField(
        verbose_name='Телефон',
        unique=True,
        null=True,
        blank=False,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return f'{self.username}, {self.email}'

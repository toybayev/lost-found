from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
        ('claimed', 'Claimed')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='lost')
    telegram_contact = models.CharField(max_length=255, help_text="Введите ссылку на ваш Telegram")  # Новое поле
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30) 
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)  # داخلي
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # باش نعرفوا هل تبعثت للإيميل ولا لا
    email_sent = models.BooleanField(default=False)
    email_error = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject or 'No subject'}"

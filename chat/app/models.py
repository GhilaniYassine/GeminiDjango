from django.db import models

class chatHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user_input = models.CharField(max_length=1000)
    response = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)  # Convert id to string before returning
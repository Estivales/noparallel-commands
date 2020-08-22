from django.db import models

class CommandHistory(models.Model):
    command = models.CharField(
        max_length=250,
    )
    started_at = models.DateTimeField(auto_now_add=True)
    done_at = models.DateTimeField(default=None, blank=True, null=True)
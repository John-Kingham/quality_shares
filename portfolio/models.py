from django.db import models


class Portfolio(models.Model):
    """
    Content for the Portfolio page.
    """

    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated"]
        verbose_name_plural = "Portfolio"

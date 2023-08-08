from django.conf import settings
from django.db import models
from django.urls import reverse


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]

    def get_admin_url(self, absolute=False):
        url = reverse(
            "admin:%s_%s_change" % (self._meta.app_label, self._meta.model_name),
            args=[self.id],
        )
        if absolute:
            url = settings.ADMIN_URL + url
        return url


class JsonModel(models.Model):
    json_field = models.JSONField(blank=True, null=True, default=dict)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.json_field)

    def get_admin_url(self, absolute=False):
        url = reverse(
            "admin:%s_%s_change" % (self._meta.app_label, self._meta.model_name),
            args=[self.id],
        )
        if absolute:
            url = settings.ADMIN_URL + url
        return url
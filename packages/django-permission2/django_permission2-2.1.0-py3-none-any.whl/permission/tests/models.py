from django.conf import settings
from django.db import models

AUTH_USER = getattr(settings, "AUTH_USER_MODEL", "auth.User")


class Article(models.Model):
    title = models.CharField("title", max_length=200)
    content = models.TextField("content")

    author = models.ForeignKey(
        AUTH_USER,
        null=True,
        related_name="permission_test_articles_author",
        on_delete=models.CASCADE,
    )
    editor = models.ForeignKey(
        AUTH_USER,
        null=True,
        related_name="permission_test_articles_editor",
        on_delete=models.CASCADE,
    )
    authors = models.ManyToManyField(
        AUTH_USER, related_name="permission_test_articles_authors"
    )
    editors = models.ManyToManyField(
        AUTH_USER, related_name="permission_test_articles_editors"
    )

    single_bridge = models.ForeignKey(
        "permission.Bridge",
        null=True,
        related_name="permission_test_single_bridge",
        on_delete=models.CASCADE,
    )
    multiple_bridge = models.ManyToManyField(
        "permission.Bridge", related_name="permission_test_multiple_bridge"
    )

    created_at = models.DateTimeField("created_at", auto_now_add=True)

    class Meta:
        app_label = "permission"

    def __str__(self):
        return self.title


class Bridge(models.Model):
    author = models.ForeignKey(
        AUTH_USER,
        null=True,
        related_name="permission_test_bridge_author",
        on_delete=models.CASCADE,
    )
    editors = models.ManyToManyField(
        AUTH_USER, related_name="permission_test_bridge_editors"
    )

    class Meta:
        app_label = "permission"

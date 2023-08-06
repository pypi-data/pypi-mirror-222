from django.conf import settings
from djongo import models


class OutstandingToken(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )

    jti = models.CharField(unique=True, max_length=255)
    token = models.TextField()

    created_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()

    class Meta:
        # Work around for a bug in Django:
        # https://code.djangoproject.com/ticket/19422
        #
        # Also see corresponding ticket:
        # https://github.com/encode/django-rest-framework/issues/705
        abstract = (
            "rest_framework_simplejwt.token_blacklist" not in settings.INSTALLED_APPS
        )
        ordering = ("user",)
        db_table = "outstanding_tokens"

    def __str__(self):
        return "Token for {} ({})".format(
            self.user,
            self.jti,
        )


class BlacklistedToken(models.Model):
    _id = models.ObjectIdField()
    token = models.OneToOneField(OutstandingToken, on_delete=models.CASCADE)

    blacklisted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Work around for a bug in Django:
        # https://code.djangoproject.com/ticket/19422
        #
        # Also see corresponding ticket:
        # https://github.com/encode/django-rest-framework/issues/705
        abstract = (
            "rest_framework_simplejwt.token_blacklist" not in settings.INSTALLED_APPS
        )
        db_table = "blacklisted_tokens"

    def __str__(self):
        return f"Blacklisted token for {self.token.user}"

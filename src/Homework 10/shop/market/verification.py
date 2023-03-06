#
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin


#
class Verification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=320)


#
class VerificationAdmin(admin.ModelAdmin):
    list_display = ("user_info", 'verification_code')
    search_fields = ("user__first_name", "user__last_name")

    #
    def user_info(self, obj):
        return "{}".format(
            " ".join([obj.user.first_name, obj.user.last_name])
        )

    user_info.short_description = "Verification"

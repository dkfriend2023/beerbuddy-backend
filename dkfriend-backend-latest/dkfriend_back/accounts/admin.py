from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.forms import CheckboxSelectMultiple
from django.db.models import ManyToManyField


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        ("기본 정보", {"fields": ("user_nickname",)},),
        ("유저 디테일", {"fields": (
                    "user_image",
                    "uni",
                    "email",
                    "phone_number",
                    )},),
        ("활동 정보", {"fields": ("like_restaurant",)},),
        ("권한", {"fields": (
            "is_active",
            "is_staff",
            "is_superuser",
        )},),
    ]

    list_display = [
        "id",
        "user_nickname",
        "uni",
        "kakao_id",
    ]

    list_display_links = ["user_nickname"]
    ordering = ("email",)

    formfield_overrides = {
        ManyToManyField: {"widget": CheckboxSelectMultiple},
    }

from django.contrib import admin

from demo.demo_project.models import Cars, Accessories, Profile


@admin.register(Cars)
class Cars(admin.ModelAdmin):
    pass


@admin.register(Accessories)
class Accessories(admin.ModelAdmin):
    pass


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    pass


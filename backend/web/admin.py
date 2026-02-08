from django.contrib import admin
from web.models.user import UserProfile
from web.models.character import Character

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)   #逗号不可删，代表变成列表，而不是单一元素

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    raw_id_fields = ('author',)
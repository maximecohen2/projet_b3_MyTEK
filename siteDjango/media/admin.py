from django.contrib import admin
from django.contrib.auth.models import User

from media.models.episode import Episode
from media.models.media import Media

# Register your models here.


class EpisodeInline(admin.TabularInline):
    model = Episode
    fk_name = 'media'


class MediaAdmin(admin.ModelAdmin):
    inlines = [EpisodeInline]


admin.site.register(Media, MediaAdmin)
admin.site.unregister(User)

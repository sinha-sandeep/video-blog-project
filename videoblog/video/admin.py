from django.contrib import admin
from video.models import Video
# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display=['id','title','auther','publish','videos']

    list_filter=('auther','publish')
    search_fields=('title',)
    raw_id_fields=('auther',)


admin.site.register(Video,VideoAdmin)

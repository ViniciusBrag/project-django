
from django.contrib.admin import ModelAdmin, register
from pythondjango.aperitivos.models import Video

@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'creation', 'vimeo_id' )
    orderimg = ('creation',)
    prepopulated_fields = {'slug':('titulo',)}
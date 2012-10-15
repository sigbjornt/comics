from django.contrib import admin

from comics.core import models


class ComicAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'language', 'url', 'rights', 'start_date',
        'end_date', 'active')
    list_filter = ['active', 'language']
    readonly_fields = ('name', 'slug', 'language', 'url', 'rights',
        'start_date', 'end_date', 'active')

    def has_add_permission(self, request):
        return False


class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'comic', 'pub_date', 'fetched')
    list_filter = ['pub_date', 'fetched', 'comic']
    date_hierarchy = 'pub_date'
    exclude = ('images',)

    def has_add_permission(self, request):
        return False


class ImageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'file', 'height', 'width', 'fetched', 'title', 'text')
    list_filter = ['fetched', 'comic']
    date_hierarchy = 'fetched'


admin.site.register(models.Comic, ComicAdmin)
admin.site.register(models.Release, ReleaseAdmin)
admin.site.register(models.Image, ImageAdmin)

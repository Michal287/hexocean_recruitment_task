from django.contrib import admin
from .models import Image, User, Tier, TierThumbnail, BinaryImage


class ImageAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):

        for image in queryset:
            if image.binary_image is not None:
                image.binary_image.delete()

        queryset.delete()


admin.site.register(User)
admin.site.register(Image, ImageAdmin)
admin.site.register(Tier)
admin.site.register(TierThumbnail)
admin.site.register(BinaryImage)



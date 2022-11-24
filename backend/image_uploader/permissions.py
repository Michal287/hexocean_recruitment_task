from rest_framework.permissions import BasePermission


class TierIsSet(BasePermission):
    message = 'This page is not allowed.'

    def has_permission(self, request, view):
        if request.user.tier:
            return True
        return False


class BinaryImageCreate(BasePermission):
    message = 'This page is not allowed.'

    def has_permission(self, request, view):
        if request.user.tier.download_binary_image_link:
            return True

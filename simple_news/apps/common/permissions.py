from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS


class IsOwnerOrReadOnly(IsAuthenticatedOrReadOnly):
    """ Permission to only allow owners of an object to edit it. """

    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return obj.author_name == request.user

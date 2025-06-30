from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSellerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # GET, HEAD, OPTIONS ke liye permission sabko milega
        if request.method in SAFE_METHODS:
            return True
        # Seller hi POST, PUT, DELETE kar sake
        return request.user.is_authenticated and request.user.role == 'seller'

    def has_object_permission(self, request, view, obj):
        # GET etc. sab dekh sakte
        if request.method in SAFE_METHODS:
            return True
        # Seller sirf apne product par action le sakta
        return obj.seller == request.user

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CartItem
from .serializers import CartItemSerializer

class CartItemListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        items = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartItemUpdateDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return CartItem.objects.get(pk=pk, user=user)
        except CartItem.DoesNotExist:
            return None

    def put(self, request, pk):
        item = self.get_object(pk, request.user)
        if not item:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CartItemSerializer(item, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk, request.user)
        if not item:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsSellerOrReadOnly

class ProductListCreateView(APIView):
    permission_classes = [IsSellerOrReadOnly]

    def get(self, request):
        products = Product.objects.all()

        # Search by name or category
        search = request.GET.get('search')
        if search:
            products = products.filter(Q(name__icontains=search) | Q(category__icontains=search))

        #  Filter by category
        category = request.GET.get('category')
        if category:
            products = products.filter(category__iexact=category)

        # Filter by price range
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)

        # Ordering (example: ?ordering=price or ?ordering=-price)
        ordering = request.GET.get('ordering')
        if ordering:
            products = products.order_by(ordering)

        #  Manual Pagination (10 per page)
        page = int(request.GET.get('page', 1))
        page_size = 10
        start = (page - 1) * page_size
        end = start + page_size
        paginated_products = products[start:end]

        serializer = ProductSerializer(paginated_products, many=True)
        return Response({
            "total": products.count(),
            "page": page,
            "results": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(seller=request.user)
            return Response({'message': 'Product created successfully', 'product': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsSellerOrReadOnly]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def get(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, product)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product updated successfully', 'product': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, product)
        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

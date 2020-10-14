from .models import Product   #import models
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response   
from rest_framework.views import APIView
from .serializers import ProductSerializer

class ProductView(APIView):
    def get(self, request, pk=None):
        if pk:
            product = get_object_or_404(Product.objects.all(), pk=pk)
            return Response({"product": ProductSerializer(product).data})
       	products = ProductSerializer(Product.objects.all(), many=True)
        return Response({"success":"true", "products": products.data})

    def post(self, request):
        p = request.data.get('product') #return in dict
        product = Product(title=p['title'], description=p['description'], price=p['price'])
        product.save()
        return Response({"success":"true", "message": "Product '{}' created successfully".format(p['title'])})

    def put(self, request, pk):
        p = request.data.get('product')
        product = Product.objects.filter(id=pk)
        product.update(title=p['title'], description=p['description'], price=p['price'])
        return Response({"success":"true", "message": "Product '{}' updated successfully".format(p['title'])})

    def delete(self, request, pk):
        # Get object with this pk
        product = get_object_or_404(Product.objects.all(), pk=pk)
        product.delete()
        return Response({"success":"true", "message": "Product with id `{}` has been deleted.".format(pk)})

from rest_framework import  serializers
from EcomerceA.models import Category , Product

class CatgeorySerializer(serializers.ModelSerializer):
    class Meta :
        fields = (
        '__all__'
        )
        model = Category


class  ProductSerializer(serializers.ModelSerializer):

    class Meta :
        fields = (
        '__all__'
        )
        model = Product
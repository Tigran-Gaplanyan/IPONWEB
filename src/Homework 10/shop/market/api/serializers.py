from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

#
from ..models import Customer, Item, Purchase, MyBag, StoreCategory, StoreOwner, Store, ItemCategory

#
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'avatar', 'registered_at']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'picture', 'category', 'price', 'quantity')


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ['name', 'picture']


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'owner', 'category')


class StoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreCategory
        fields = ['id', 'name', 'picture']


class StoreOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreOwner
        fields = ['id', 'user', 'avatar', 'registered_at']


class PurchaseSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Purchase
        fields = ('id', 'customer', 'items')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        customer_id = validated_data.pop('customer')
        customer = Customer.objects.get(id=customer_id)
        purchase = Purchase.objects.create(customer=customer)
        for item_data in items_data:
            item = Item.objects.get(id=item_data['id'])
            purchase.items.add(item)
        return purchase


class MyBagSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = MyBag
        fields = ('id', 'customer', 'items')


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
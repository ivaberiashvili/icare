from django.test import TestCase

# Create your tests here.
import pytest
from rest_framework.test import APIClient
from core.models import Product, Category
from django.contrib.auth.models import User
from rest_framework import status

@pytest.mark.django_db
def test_create_product():
    client = APIClient()

    # Fetch or create a category for the product
    category, _ = Category.objects.get_or_create(name="Fruits")

    # Ensure "Test Product" exists before testing the API
    product, created = Product.objects.get_or_create(
        name="Test Product",
        defaults={
            "description": "A test product",
            "price": 9.99,
            "category": category
        }
    )

    # Make a GET request to check if the product is available via API
    response = client.get('/products/')
    assert response.status_code == 200
    assert any(p["name"] == "Test Product" for p in response.data)  # Check if the response contains "Test Product"

@pytest.mark.django_db
def test_authenticated_product_post():
    user = User.objects.create_user(
        username="testuser",
        password="testpass",
        is_staff=True  # or is_superuser=True
    )
    category = Category.objects.create(name="Drinks")

    client = APIClient()
    client.force_authenticate(user=user)

    product_data = {
        "name": "Orange Juice",
        "description": "Freshly squeezed",
        "price": 3.50,
        "category": category.id,
    }

    response = client.post('/products/', product_data, format='json')

    assert response.status_code in [200, 201]
    assert Product.objects.filter(name="Orange Juice").exists()
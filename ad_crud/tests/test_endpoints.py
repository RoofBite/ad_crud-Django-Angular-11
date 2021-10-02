from django.http import response
from rest_framework.test import APITestCase
from ad_crud.models import Category, Offer

# from ad_crud.api_views import ListSchoolTeachers
from rest_framework.test import APIClient
import json
from django.urls import reverse


class TestOffersList(APITestCase):
    url = "/api/offers"

    def setUp(self):
        category1 = Category.objects.create(name="Category1", ordering=1)
        Offer.objects.create(title="Offer1", description="Offer1", price=10, category=category1)
        Offer.objects.create(title="Offer2", description="Offer2", price=20, category=category1)

    def test_offers_GET(self):
        response = self.client.get(self.url)
        
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["title"], "Offer1")


class TestOffer(APITestCase):
    def setUp(self):
        category1 = Category.objects.create(name="Category1", ordering=1)
        Offer.objects.create(title="Offer1", description="Offer1", price=10, category=category1)

    def test_offer_GET(self):
        response = self.client.get(
            reverse("view-offer", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, 200)

    def test_offer_POST(self):
        data = {"title": "Offer3", "description": "Offer3", "price":10, "category":1}
        response = self.client.post(
            reverse("list-offer"), data=data
        )

        self.assertEqual(response.status_code, 201)
    
    def test_offer_PUT(self):
        data = {"title": "Offer1Update", "description": "Offer2", "price":10, "category":1}
        response = self.client.put(
            reverse("view-offer", kwargs={"pk": 1}), data=data, format="json",
        )

        self.assertEqual(response.status_code, 200)
    
    def test_offer_DELETE(self):
        response = self.client.delete(
            reverse("view-offer", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, 204)



class TestCategoryList(APITestCase):
    url = "/api/category"

    def setUp(self):
        Category.objects.create(name="Category1", ordering=1)

    def test_category_GET(self):
        response = self.client.get(self.url)
        
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["name"], "Category1")


class TestCategory(APITestCase):
    def setUp(self):
        Category.objects.create(name="Category1", ordering=1)
        Category.objects.create(name="Category3", ordering=2)
        Category.objects.create(name="Category2", ordering=3)

    def test_category_GET(self):
        response = self.client.get(
            reverse("view-category", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, 200)

    def test_category_POST(self):
        data = {"name": "Category3", "ordering": 1}
        response = self.client.post(
            reverse("list-category"), data=data
        )

        self.assertEqual(response.status_code, 201)
    

    def test_category_PUT(self):
        data = {"name": "Category1Update", "ordering": 1}
        response = self.client.put(
            reverse("view-category", kwargs={"pk": 1}), data=data, format="json",
        )

        self.assertEqual(response.status_code, 200)
    
    def test_category_DELETE(self):
        response = self.client.delete(
            reverse("view-category", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, 204)




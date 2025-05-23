from django.test import TestCase
from .models import Category, Image
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Test Category")
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(str(category), "Test Category")

class ImageModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

    def test_image_creation(self):
        # Create a dummy file for the image field
        dummy_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        
        # Get today's date
        today = timezone.now().date()
        
        # Create the image instance
        image = Image.objects.create(
            title="Test Image",
            image=dummy_file,
            created_date=today,
            age_limit=18
        )
        
        # Add the category to the image
        image.categories.add(self.category)
        
        # Assertions to verify the image was created correctly
        self.assertEqual(image.title, "Test Image")
        self.assertEqual(image.created_date, today)
        self.assertEqual(image.age_limit, 18)
        self.assertIn(self.category, image.categories.all())
        self.assertEqual(str(image), "Test Image")
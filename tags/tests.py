from django.test import TestCase
from .models import Tag


class TagTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(tag_name='test_tag')
        self.tag.save()

    def tearDown(self):
        self.tag.delete()

    def test_create_tag(self):
        tag = Tag.objects.get(tag_name='test_tag')
        self.assertIsNotNone(obj=tag)

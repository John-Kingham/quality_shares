from http import HTTPStatus
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Category, Post


class TestPostViews(TestCase):

    def setUp(self):
        """
        Set up two posts, one published, one draft, each attached to a
        different category.
        """
        # Set up two categories
        self.category_with_published_post = Category(name="Category 1")
        self.category_with_published_post.save()
        self.category_no_published_post = Category(name="Category 2")
        self.category_no_published_post.save()

        # Set up a published post
        self.user = User.objects.create_superuser(
            username="test-username",
            password="test-password",
            email="text@example.com",
        )
        self.published_post = Post(
            author=self.user,
            published=True,
            category=self.category_with_published_post,
            title="Published Post Title",
            description="Published Post Description",
            content="Published Post Content",
            slug="published-post-slug",
        )
        self.published_post.save()

        # Set up a draft post
        self.draft_post = Post(
            author=self.user,
            title="Draft Post Title",
            category=self.category_no_published_post,
        )
        self.draft_post.save()

    def test_post_list_view(self):
        """Test that the post list page contains the correct information"""
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.published_post.title)
        self.assertContains(response, self.published_post.description)
        self.assertContains(response, self.published_post.slug)
        self.assertContains(response, self.published_post.category.name)
        self.assertNotContains(response, self.draft_post.title)
        self.assertNotContains(response, self.draft_post.category.name)

    def test_post_detail_view(self):
        """Test that the post detail page contains the correct information"""
        post_detail_url = reverse(
            "post_detail", args=[self.published_post.slug]
        )
        response = self.client.get(post_detail_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.published_post.title)
        self.assertContains(response, self.published_post.content)
        self.assertContains(response, self.published_post.category.name)

    def test_category_list_view(self):
        """Test that the category list (home) page is rendering correctly"""
        response = self.client.get(reverse("category_list"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.published_post.title)
        self.assertContains(response, self.published_post.category.name)
        self.assertNotContains(response, self.draft_post.title)
        self.assertNotContains(response, self.draft_post.category.name)

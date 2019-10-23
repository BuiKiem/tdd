"""Include test cases for the app"""

from django.test import TestCase


class HomePageTestCase(TestCase):
    """Homepage test cases."""

    def test_homepage_view_uses_home_tempate(self) -> None:
        """Test that the home_page view render the correct template"""
        response = self.client.get("/")

        self.assertTemplateUsed(response, "home.html")

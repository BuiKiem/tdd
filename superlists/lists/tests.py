"""Include test cases for the app"""

from django.test import TestCase

from lists.models import Item


class HomePageTestCase(TestCase):
    """Homepage view test cases."""

    def test_uses_home_template(self) -> None:
        """Test that the home_page view renders the correct template"""
        response = self.client.get("/")

        self.assertTemplateUsed(response, "home.html")

    def test_can_save_save_a_post_request(self) -> None:
        """Test that the home_page view handles the POST request with data."""
        self.client.post("/", data={"new_item": "A new list item"})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new list item")

    def test_redirects_after_post_request(self) -> None:
        """Test that home_page view will redirect to itself after the POST request."""
        response = self.client.post("/", data={"new_item": "A new list item"})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/")

    def test_only_saves_items_when_necessary(self) -> None:
        """Test that homepage does not save items when it receive the GET request"""
        self.client.get("/")
        self.assertEqual(Item.objects.count(), 0)

    def test_displays_all_list_items(self) -> None:
        """Test that homepage displays all the items in the database"""
        Item.objects.create(text="Item 1")
        Item.objects.create(text="Item 2")

        response = self.client.get("/")

        self.assertIn("Item 1", response.content.decode())
        self.assertIn("Item 2", response.content.decode())


class ItemModelTestCase(TestCase):
    """Test cases for the Item model"""

    def test_can_save_and_retrieve_items(self) -> None:
        """Test that multiple items can be saved and retrieved."""
        first_item = Item()
        first_item.text = "First item"
        first_item.save()

        second_item = Item()
        second_item.text = "Second item"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, "First item")
        self.assertEqual(second_saved_item.text, "Second item")

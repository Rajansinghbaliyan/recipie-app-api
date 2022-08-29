from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = "harrypotter@example.com"
        password = "password"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(raw_password=password))

    def test_email_with_normalization(self):
        sample_emails = [
            ['test3@Example.com', 'test3@example.com'],
            ['Test3@example.com', 'Test3@example.com'],
            ['test3@EXAmple.cOM', 'test3@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample1234')

            self.assertEqual(user.email, expected)

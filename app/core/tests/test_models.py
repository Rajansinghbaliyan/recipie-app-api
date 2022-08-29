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
            ['Test1@example.com', 'Test1@example.com'],
            ['test2@EXAmple.cOM', 'test2@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample1234')

            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raise_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sample123')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser("test@example.com", "sample123")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

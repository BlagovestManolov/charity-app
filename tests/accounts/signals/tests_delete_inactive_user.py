from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone

from tests.accounts.models.mixin import CreateProfileObjectsMixin

UserModel = get_user_model()


class TestUserSignal(CreateProfileObjectsMixin, TestCase):
    def setUp(self) -> None:
        self.user = self._create_user_with_valid_values()

    def test__user_last_login_date__expect_correct(self):
        last_login_before = self.user.last_login
        self.client.login(
            username='testuser',
            password='testpassword',
        )

        self.user.refresh_from_db()
        last_login_after = self.user.last_login

        self.assertNotEqual(last_login_after, last_login_before)

    def test__delete_user_automatically_if_inactive_more_than_365_days__expect_delete(self):
        self.user.last_login = timezone.now() - timezone.timedelta(days=400)
        self.user.save()
        self.assertFalse(UserModel.objects.filter(username='testuser').exists())

    def test__delete_user_automatically_if_active_small_than_365_days__expect_not_delete(self):
        self.user.last_login = timezone.now() - timezone.timedelta(days=100)
        self.user.save()
        self.assertTrue(UserModel.objects.filter(username='testuser').exists())
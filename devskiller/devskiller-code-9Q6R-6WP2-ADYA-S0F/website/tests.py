from django.conf import settings
from django.http.cookie import SimpleCookie
from django.shortcuts import resolve_url
from django.test import TestCase
from leave import factories


class AuthenticatedUserEnTestCase(TestCase):
    def setUp(self):
        self.user = factories.UserFactory(manager=factories.UserFactory())
        self.client.cookies = SimpleCookie({settings.LANGUAGE_COOKIE_NAME: "en"})
        self.client.force_login(self.user, settings.AUTHENTICATION_BACKENDS[0])


class AuthenticatedUserPlTestCase(TestCase):
    def setUp(self):
        self.user = factories.UserFactory(manager=factories.UserFactory())
        self.client.cookies = SimpleCookie({settings.LANGUAGE_COOKIE_NAME: "pl"})
        self.client.force_login(self.user, settings.AUTHENTICATION_BACKENDS[0])


class SuperUserEnTestCase(TestCase):
    def setUp(self):
        self.user = factories.UserFactory(
            email="foo@bar.com", is_superuser=True, is_staff=True, is_active=True
        )
        self.user.save()
        self.client.cookies = SimpleCookie({settings.LANGUAGE_COOKIE_NAME: "en"})
        self.client.force_login(self.user, settings.AUTHENTICATION_BACKENDS[0])


class SuperUserPlTestCase(TestCase):
    def setUp(self):
        self.user = factories.UserFactory(
            email="foo@bar.com", is_superuser=True, is_staff=True, is_active=True
        )
        self.user.save()
        self.client.cookies = SimpleCookie({settings.LANGUAGE_COOKIE_NAME: "pl"})
        self.client.force_login(self.user, settings.AUTHENTICATION_BACKENDS[0])


class TestAdminAvailable(TestCase):
    def setUp(self):
        self.user = factories.UserFactory(
            email="foo@bar.com", is_superuser=False, is_staff=True, is_active=True
        )
        self.user.save()
        self.client.force_login(self.user, settings.AUTHENTICATION_BACKENDS[0])

    def test_admin_get(self):
        url = resolve_url("admin:index")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

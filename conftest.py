import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


@pytest.fixture(scope='function')
def user(db, django_user_model):
    """
    User instance from default django user model
    """
    User = get_user_model()
    return User.objects.create_user(email='a@a.pl', fullname='Ala', password='testPassword1')
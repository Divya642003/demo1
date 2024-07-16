import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_homepage(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert "Hello, world!" in response.content.decode()

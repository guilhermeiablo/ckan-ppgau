import pytest


@pytest.fixture()
def data():
    DATE = "1990-01-01T00:00:00"
    return {
        "id": "123",
        "name": "123",
        "description": "some description",
        "title": "123",
        "type": "dataset",
        "state": "active",
        "private": False,
        "metadata_created": DATE,
        "metadata_modified": DATE,
        "num_resources": 1,
        "num_tags": 1,
        "resources": [{}],
        "creator_user_id": "123e4567-e89b-12d3-a456-426614174000",
        "owner_org": "123e4567-e89b-12d3-a456-426614174000",
    }

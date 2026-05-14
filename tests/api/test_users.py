import pytest

@pytest.mark.api
def test_get_users(
        api_client
):

    response = api_client.get(
        "https://jsonplaceholder.typicode.com/users", verify=False
    )

    assert response.status_code == 200

    body = response.json()

    assert len(body) > 0

    # Validate that each user has a name
    assert body[0]["name"] is not None

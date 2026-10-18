import requests


def test_get_post_1():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url, timeout=10)

    assert response.status_code == 200, f"期望状态码 200，实际 {response.status_code}"
    assert response.json()["id"] == 1, f"期望 id 为 1，实际 {response.json().get('id')}"

import pytest
import requests

pytestmark = pytest.mark.smoke


def test_posts_list_returns_200_and_list(base_url):
    """冒烟用例：列表接口可用，且返回结构是列表。"""
    response = requests.get(f"{base_url}/posts", timeout=10)

    assert response.status_code == 200, f"期望状态码 200，实际 {response.status_code}"

    payload = response.json()
    assert isinstance(payload, list), f"期望响应是列表，实际 {type(payload).__name__}"
    assert len(payload) > 0, "列表接口不应返回空列表"

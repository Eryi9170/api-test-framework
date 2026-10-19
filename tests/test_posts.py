import pytest
import requests


@pytest.mark.parametrize(
    "post_id, expected_status",
    [
        pytest.param(1, 200, id="existing-post"),
        pytest.param(99999, 404, id="missing-post"),
        pytest.param("abc", 404, id="invalid-id"),
    ],
)
def test_get_post_by_id(base_url, post_id, expected_status):
    """同一用例覆盖正常 / 不存在 / 非法 id 三种情况。"""
    response = requests.get(f"{base_url}/posts/{post_id}", timeout=10)

    assert response.status_code == expected_status, (
        f"post_id={post_id} 期望状态码 {expected_status}，实际 {response.status_code}"
    )

    if expected_status == 200:
        post = response.json()
        assert post["id"] == post_id, f"期望 id={post_id}，实际 {post.get('id')}"

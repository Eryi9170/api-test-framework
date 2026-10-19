import pytest
import requests

pytestmark = pytest.mark.regression

# 字段 -> 期望类型，既校验存在性也校验类型
EXPECTED_FIELDS = {
    "userId": int,
    "id": int,
    "title": str,
    "body": str,
}


def test_post_detail_has_complete_fields(base_url):
    """回归用例：单条详情字段完整且类型正确。"""
    response = requests.get(f"{base_url}/posts/1", timeout=10)
    assert response.status_code == 200, f"期望状态码 200，实际 {response.status_code}"

    post = response.json()

    for field, expected_type in EXPECTED_FIELDS.items():
        assert field in post, f"响应缺少字段 {field}"
        assert isinstance(post[field], expected_type), (
            f"字段 {field} 类型应为 {expected_type.__name__}，"
            f"实际 {type(post[field]).__name__}"
        )

    assert post["id"] == 1, f"期望 id=1，实际 {post['id']}"
    assert post["userId"] >= 1, "userId 应为正整数"
    assert post["title"].strip(), "title 不应为空字符串"

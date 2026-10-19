import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def base_url():
    """接口根地址，供各测试用例复用，避免在测试文件中硬编码。"""
    return BASE_URL

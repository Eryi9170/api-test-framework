# api-test-framework

基于 pytest + requests 的 Python 接口自动化测试项目。

## 环境准备

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 运行测试

```bash
pytest -v
```

## 目录结构

```
api-test-framework/
├── tests/
│   └── test_posts.py    # 接口测试用例
├── requirements.txt     # 项目依赖
└── .gitignore
```

## 当前用例

| 用例 | 接口 | 断言 |
| --- | --- | --- |
| `test_get_post_1` | `GET https://jsonplaceholder.typicode.com/posts/1` | 状态码 200；JSON `id` 为 1 |

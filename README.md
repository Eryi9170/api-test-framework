# api-test-framework

[![tests](https://github.com/Eryi9170/api-test-framework/actions/workflows/tests.yml/badge.svg)](https://github.com/Eryi9170/api-test-framework/actions/workflows/tests.yml)

基于 pytest + requests 的 Python 接口自动化测试项目，覆盖参数化、用例分层与 fixture 复用。

被测服务：[JSONPlaceholder](https://jsonplaceholder.typicode.com)

## 环境准备

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 运行测试

```bash
pytest -v                 # 全量
pytest -m smoke -v        # 只跑冒烟
pytest -m regression -v   # 只跑回归
```

## 目录结构

```
api-test-framework/
├── conftest.py                 # base_url fixture（session 级）
├── pytest.ini                  # testpaths + marker 注册
├── tests/
│   ├── test_posts.py           # 参数化用例：id = 1 / 99999 / abc
│   ├── smoke/
│   │   └── test_posts_list.py  # 冒烟：列表接口 200 且返回列表
│   └── regression/
│       └── test_post_detail.py # 回归：详情字段存在性 + 类型校验
├── requirements.txt
└── .gitignore
```

## 用例清单

| 用例 | 标记 | 接口 | 断言重点 |
| --- | --- | --- | --- |
| `test_get_post_by_id[existing-post]` | - | `GET /posts/1` | 状态码 200；`id == 1` |
| `test_get_post_by_id[missing-post]` | - | `GET /posts/99999` | 状态码 404 |
| `test_get_post_by_id[invalid-id]` | - | `GET /posts/abc` | 状态码 404 |
| `test_posts_list_returns_200_and_list` | `smoke` | `GET /posts` | 状态码 200；响应为列表且非空 |
| `test_post_detail_has_complete_fields` | `regression` | `GET /posts/1` | `userId`/`id`/`title`/`body` 存在且类型正确 |

## 设计说明

- **base_url 统一来源**：`conftest.py` 里定义 session 级 `base_url` fixture，测试文件只拼路径，不硬编码域名。
- **参数化**：三种 id 场景写在同一个测试函数里，用 `pytest.param(..., id=...)` 给用例起可读名字。
- **分层**：`smoke/` 只验证“服务活着、结构对”，`regression/` 负责字段级细节，两者用 marker 区分，可按需单独执行。
- **marker 注册**：`pytest.ini` 里注册了 `smoke` / `regression`，并通过 `filterwarnings = error::pytest.PytestUnknownMarkWarning` 让未注册的 marker 直接导致失败，避免警告被忽略。

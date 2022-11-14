from app.main import app
from fastapi.testclient import TestClient
import pytest


client = TestClient(app)


@pytest.mark.parametrize(
    "test_case",
    (
        {
            "case": "정상적으로 Info 로그가 남음",
            "given_body": {
                "log_level": "info",
                "log_msg": "test",
            },
            "expected_status_code": 201,
        },
        {
            "case": "정상적으로 warn 로그가 남음",
            "given_body": {
                "log_level": "warn",
                "log_msg": "test",
            },
            "expected_status_code": 201,
        },
        {
            "case": "정상적으로 error 로그가 남음",
            "given_body": {
                "log_level": "error",
                "log_msg": "test",
            },
            "expected_status_code": 201,
        },
        {
            "case": "의도치 않은 error level이 들어올경우 400 status code를 받음",
            "given_body": {
                "log_level": "unknown",
                "log_msg": "test",
            },
            "expected_status_code": 400,
        },
    ),
)
def test_post_log(test_case):
    response = client.post("/log", json=test_case["given_body"])
    assert response.status_code == test_case["expected_status_code"]

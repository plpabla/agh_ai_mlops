import os
from main import export_envs


def test_envs_are_loaded():
    export_envs("test")
    assert os.getenv("APP_NAME") == "mlops-lab"
    assert os.getenv("ENVIRONMENT") == "test"

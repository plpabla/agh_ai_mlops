import os
import argparse
import yaml as pyyaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev", secrets: str = "secrets.yaml") -> None:
    env_file = f".env.{environment}"

    if not os.path.exists(env_file):
        print(f"Warning: Environment file {env_file} does not exist.")
        return
    load_dotenv(env_file)

    # Load secrets from YAML file
    if os.path.exists(secrets):
        with open(secrets, "r") as file:
            secrets_data = pyyaml.safe_load(file)
            for key, value in secrets_data.items():
                os.environ[key] = str(value)
    else:
        print(f"Warning: Secrets file {secrets} does not exist.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("FASTAPI_SECRET: ", settings.FASTAPI_SECRET)

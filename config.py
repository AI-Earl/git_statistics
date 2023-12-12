import os
import yaml
import toml
from pathlib import Path

from config_schema import ConfigsSchema, PyprojectSchema


class BaseConfig:
    MODE = None
    DEBUG = False
    TESTING = False

    ENGINE_OPTIONS = {
        "pool_recycle": 3600,
        "pool_pre_ping": True
    }

    def __init__(self, configs: dict):
        print(f'System Run in {configs["app"]["app_mode"]} Mode.')

        # project info
        self.PROJEDCT_NAME = configs['name']
        self.VERSION = configs['version']
        self.DESCRIPTION = configs['description']

        # app info
        self.PORT = configs['app']['app_port']

        # database info
        mariadb_config = configs['database']['mariadb']
        self.MARIADB_URI = f"mysql+pymysql://{mariadb_config['db_user']}:{mariadb_config['db_password']}@" \
                           f"{mariadb_config['db_host']}:{mariadb_config['db_port']}/{mariadb_config['db_name']}"

        # line_bot info
        self.LINE_BOT_TOKEN = configs['line_bot']['access_token']
        self.LINE_BOT_USER_ID = configs['line_bot']['user_id']


class DevelopmentConfig(BaseConfig):
    MODE = "development"
    DEBUG = True


class TestingConfig(BaseConfig):
    MODE = "testing"
    TESTING = True


class ProductionConfig(BaseConfig):
    MODE = "production"
    pass


CONFIG_MAPPER = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "stage": ProductionConfig,
    "production": ProductionConfig
}


class ConfigManager:
    _instance = None

    # Singleton Pattern
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load(self):
        yaml_schemas = self.load_yaml()
        app_mode = yaml_schemas['app']['app_mode']
        toml_schemas = self.load_toml()
        schemas = {**yaml_schemas, **toml_schemas}

        return CONFIG_MAPPER[app_mode](schemas)

    def load_yaml(self) -> dict:
        yaml_file_absolute_path = self._verify_file_exist()
        with open(yaml_file_absolute_path, "r") as f:
            config_data = yaml.safe_load(f)

        return ConfigsSchema().load(config_data)

    def load_toml(self) -> dict:
        pyproject_path = "./pyproject.toml"
        pyproject_dict = {}

        if Path(pyproject_path).exists():
            # read pyproject.toml
            with open(pyproject_path, "r") as f:
                pyproject_dict = toml.load(f)['tool']['poetry']

        return PyprojectSchema().load(pyproject_dict)

    @staticmethod
    def _verify_file_exist():
        if (env_file := os.getenv("CONFIG_FILE")) is None:
            print("No CONFIG_FILE in environment variable, use default config_dev.yaml")
            env_file = "config_dev.yaml"

        yaml_file_absolute_path = Path(__file__).parent.absolute() / env_file
        if not yaml_file_absolute_path.exists():
            print(f"Cannot find config file: {yaml_file_absolute_path}")
            exit(4)

        return yaml_file_absolute_path


config = ConfigManager().load()

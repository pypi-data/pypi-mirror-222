import sys
import requests
import os
import re
class PythonClient:

    @staticmethod
    def hello_world():
        return "I am testing this code"

    @staticmethod
    def required_properties_func(configs, keyword):
        required_properties = {}
        for config in configs:
            if keyword in config["name"]:
                required_properties.update({k: v for k, v in config["source"].items() if k not in required_properties})
        return required_properties

    @staticmethod
    def resolve_placeholders(data):
        resolved_data = {}

        def resolve_value(value):
            if isinstance(value, str):
                placeholders = re.findall(r"\${(.*?)}", value)
                for placeholder in placeholders:
                    if placeholder in data:
                        value = value.replace(f"${{{placeholder}}}", str(resolve_value(data[placeholder])))
            return value

        for key, value in data.items():
            print(key)
            if isinstance(value, str) and  "${" in value and "}" in value:
                resolved_data[key] = resolve_value(value)
            else:
                if isinstance(value, dict):
                    resolved_data[key] = PythonClient.resolve_placeholders(value)
                else:
                    resolved_data[key] = value

        return resolved_data

    @staticmethod
    def init_config(config_url, service_name, profiles, commit_id):

        profiles_string = ','.join(profiles)
        required_properties = []
        if commit_id:
            api_url = f"{config_url}/{service_name}/{profiles_string}/{commit_id}"
        else:
            api_url = f"{config_url}/{service_name}/{profiles_string}"

        try:
            response = requests.get(api_url)
            configs = response.json()['propertySources']

            total_config = PythonClient.get_config_super_set(configs)
            PythonClient.add_namespace(total_config)

            required_properties = PythonClient.required_properties_func(configs, f'yamls/{service_name}')

            resolved_data = PythonClient.resolve_placeholders(total_config)

            for key in required_properties:
                required_properties[key] = resolved_data[key]

            return required_properties
        except Exception as error:
            raise Exception(f"Failed to fetch configuration: {error}")


    @staticmethod
    def startclient(config_server_url, service_name, profiles, commit_id):
        required_properties = PythonClient.init_config(config_server_url, service_name, profiles, commit_id)
        return required_properties


    @staticmethod
    def python_client(config_server_url, application_name, profiles, commit_id):
        try:
            j2_properties = PythonClient.startclient(config_server_url, application_name, profiles, commit_id)
            for key, value in j2_properties.items():
                os.environ[key] = str(value)
            print("Environment variables are set successfully")
        except Exception as error:
            raise Exception(f"Failed to set Environment variables: {error}")


    @staticmethod
    def get_config_super_set(configs):
        total_config = {}
        for config in configs:
            for key in config['source']:
                if key not in total_config:
                    total_config[key] = config['source'][key]
        return total_config

    @staticmethod
    def add_namespace(config):

        for key in config:
            if config[key] == "${ENV_NAMESPACE}":
                config[key] = os.environ.get("ENV_NAMESPACE", "loki")



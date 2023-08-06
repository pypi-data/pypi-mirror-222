import os
import sys
from Pythonclient import PythonClient

def main(config_server_url, application_name, profiles, commit_id):
    try:
        # Create a string to store all key-value pairs
        key_value_pairs = ""
        j2_properties=PythonClient.startclient(config_server_url, application_name, profiles, commit_id)
        for key, value in j2_properties.items():
            key_value_pairs += f'export {key}="{value}"\n'

        # Write the key-value pairs to the shell.sh file
        with open('/usr/src/app/scripts/shell.sh', 'a') as file:
            file.write(key_value_pairs)

        print("Environment variables are written successfully to shell.sh")
    except Exception as error:
        raise Exception(f"Failed to write Environment variables: {error}")


if __name__ == "__main__":

    config_server_url = os.environ.get("CONFIG_SERVER_URL")
    application_name = os.environ.get("APPLICATION_NAME")
    profiles = os.environ.get("PROFILES").strip('][').split(', ')
    commit_id = os.environ.get("COMMIT_ID")

    main(config_server_url, application_name, profiles, commit_id)

import os
import subprocess
import json
import argparse
from pyngrok import ngrok

def check_config(force_config=False):
    # Path of the configuration file
    config_path = os.path.join(os.path.expanduser('~'), '.codebot', 'config.json')

    # Default configuration
    default_config = {
        'openai': {
            'api_base': 'https://api.openai.com/v1',
            'api_key': '',  # This is required
            'model': 'gpt-3.5-turbo-16k',
            'max_tokens': '5000',
            'language': 'chinese',
        }
    }

    # Check if the configuration file exists
    if not os.path.exists(config_path):
        # If the configuration file does not exist, create a new one with default configuration
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w') as config_file:
            json.dump(default_config, config_file)

    # Read the configuration file
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)

    # If force_config is True or api_key is not set, ask for user input
    if force_config or not config['openai']['api_key']:
        # Update the configuration file with user input
        for key, default_value in default_config['openai'].items():
            user_input = input(f"Please enter {key} (default is '{default_value}'): ")
            if user_input:
                config['openai'][key] = user_input

        # Write the updated configuration back to the file
        with open(config_path, 'w') as config_file:
            json.dump(config, config_file)
            
            
def check_config_terminal(force_config=False):
    # Path of the configuration file
    config_path = os.path.join(os.path.expanduser('~'), '.codebot', 'config.json')

    # Default configuration
    default_config = {
        'openai': {
            'api_base': 'https://api.openai.com/v1',
            'api_key': '',  # This is required
            'model': 'gpt-3.5-turbo-16k',
            'max_tokens': '5000',
            'language': 'chinese',
            'password': '',
        }
    }

    # Check if the configuration file exists
    if not os.path.exists(config_path):
        # If the configuration file does not exist, create a new one with default configuration
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w') as config_file:
            json.dump(default_config, config_file)

    # Read the configuration file
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)

    # If force_config is True or api_key is not set, ask for user input
    if force_config or not config['openai']['api_key']:
        # Update the configuration file with user input
        for key, default_value in default_config['openai'].items():
            user_input = input(f"Please enter {key} (default is '{default_value}'): ")
            if key == 'password':
                while user_input == '':
                    user_input = input(f"Please enter {key} (default is '{default_value}'): ")
            if user_input:
                config['openai'][key] = user_input

        # Write the updated configuration back to the file
        with open(config_path, 'w') as config_file:
            json.dump(config, config_file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fix", action="store_true")
    parser.add_argument("--ngrok", type=str, help="Ngrok auth token")
    parser.add_argument("--config", action="store_true", help="Reset configuration")
    args = parser.parse_args()

    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Change the current working directory to your application's directory

    if args.config:
        # If the --config option is given, delete the existing configuration file and create a new one
        config_path = os.path.join(os.path.expanduser('~'), '.codebot', 'config.json')
        if os.path.exists(config_path):
            os.remove(config_path)
        check_config(force_config=True)  # Check and create the configuration file
    else:
        print("Checking configuration...")
        check_config()  # Check and create the configuration file if not exists

    if args.ngrok:
        try:
            ngrok.kill()
            # Set the ngrok auth token
            ngrok.set_auth_token(args.ngrok)
            # Create a ngrok tunnel to port 8000
            ngrok_tunnel = ngrok.connect(8000)
            print(f"Ngrok Tunnel Opened: {ngrok_tunnel.public_url}")
        except Exception as e:
            print(f"Failed to set up ngrok tunnel: {e}")

    if args.fix:
        subprocess.run(["chainlit", "run", "app_cn.py"])  # Run your application
    else:
        subprocess.run(["chainlit", "run", "app.py"])  # Run your application
        
        
def main_terminal():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", action="store_true", help="Reset configuration")
    parser.add_argument("--port", type=int, help="Port")
    parser.add_argument("--fix", action="store_true")
    args = parser.parse_args()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Change the current working directory to your application's directory
    if args.config:
        # If the --config option is given, delete the existing configuration file and create a new one
        config_path = os.path.join(os.path.expanduser('~'), '.codebot', 'config.json')
        if os.path.exists(config_path):
            os.remove(config_path)
        check_config(force_config=True)  # Check and create the configuration file
    else:
        print("Checking configuration...")
        check_config()  # Check and create the configuration file if not exists
    
   
            
    port = args.port if args.port else 10086
    if args.fix:
        subprocess.run(["chainlit", "run", "app_terminal_cn.py", "--port", str(port)])  # Run your application
    else:
        subprocess.run(["chainlit", "run", "app_terminal.py", "--port", str(port)])  # Run your application



if __name__ == "__main__":
    main()

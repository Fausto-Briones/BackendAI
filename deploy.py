import os
import requests
import subprocess

# PythonAnywhere API details
username = os.getenv("PYTHONANYWHERE_USERNAME")
api_token = os.getenv("PYTHONANYWHERE_API_TOKEN")
domain_name = f"{username}.pythonanywhere.com"

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        exit(result.returncode)

def deploy():
    # Step 1: Set up the virtual environment
    print("Setting up the virtual environment...")
    run_command(f"python3 -m venv /home/{username}/myenv")

    # Step 2: Activate the virtual environment and install dependencies
    print("Installing dependencies from requirements.txt...")
    run_command(f"/home/{username}/myenv/bin/pip install -r /home/{username}/BackendAI/requirements.txt")

    # Step 3: Run the Flask application
    print("Running the Flask application...")
    run_command(f"/home/{username}/myenv/bin/python /home/{username}/BackendAI/run.py")

    # Step 4: Reload the web application (if needed)
    response = requests.post(
        f"https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/",
        headers={"Authorization": f"Token {api_token}"},
    )
    if response.status_code == 200:
        print("Successfully deployed and reloaded!")
    else:
        print(f"Failed to reload the web app: {response.status_code} {response.text}")

if __name__ == "__main__":
    deploy()

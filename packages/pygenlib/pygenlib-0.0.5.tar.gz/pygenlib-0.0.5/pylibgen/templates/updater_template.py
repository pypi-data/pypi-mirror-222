import os
import shutil
import subprocess
import time

# List of folders to be deleted
folders_to_delete = ["build", "dist"]


def delete_folders():
    for folder in folders_to_delete:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"Deleted folder: {folder}")
        else:
            print(f"Folder not found: {folder}")


def increment_version():
    # Read the version from setup.py
    with open("setup.py", "r") as f:
        setup_lines = f.readlines()

    version = "0.1.0"  # Default version if not found in setup.py

    for line in setup_lines:
        if "version =" in line:
            version = line.split("=")[1].strip().strip('"').strip("'")
            break

    # Split the version number into major, minor, and patch parts
    major, minor, patch = map(int, version.split('.'))

    # Increment the patch part by 1
    patch += 1

    # Join the parts back into the updated version string
    version = f"{major}.{minor}.{patch}"

    # Update the version in setup.py
    with open("setup.py", "w") as f:
        for line in setup_lines:
            if "version =" in line:
                f.write(f'version = "{version}"\n')
            else:
                f.write(line)


def run_commands(username, api_token):
    increment_version()  # Increment the version before running commands

    # Command to install the package locally
    install_cmd = "pip install ."

    # Command to build the source distribution and wheel
    build_cmd = "python setup.py sdist bdist_wheel"

    # Command to upload the distribution to PyPI using twine
    # Use the API token here
    upload_cmd = f"twine upload dist/* --verbose --username {username} --password {api_token}"

    # Execute commands
    try:
        subprocess.run(install_cmd, check=True, shell=True)
        print("*****Installed the package locally.*****")
        subprocess.run(build_cmd, check=True, shell=True)
        print("*****Built the source distribution and wheel.*****")
        # Wait 5 seconds for the files to be generated
        time.sleep(5)
        subprocess.run(upload_cmd, check=True, shell=True)
        print("Uploaded the distribution to PyPI.")
    except subprocess.CalledProcessError as e:
        print("Error occurred while executing a command:", e)
        exit(1)


if __name__ == "__main__":
    delete_folders()

    # Replace 'your_pypi_username' and 'your_pypi_api_token' with your actual PyPI credentials
    pypi_username = "__token__"  # Use the "__token__" username
    pypi_api_token = "Use your actual API token here"

    # Use the API token for authentication
    run_commands(pypi_username, pypi_api_token)
    print("Congratulations! You have pushed the package to PyPI.")

import os
import argparse
import shutil


def create_library_template(library_name, target_folder="."):
    # Prepare the target folder path
    target_folder = os.path.abspath(target_folder)
    library_path = os.path.join(target_folder, library_name)

    # Create the main library directory
    os.makedirs(library_path, exist_ok=True)

    # make a virtual environment in the library folder and activate it (check for windows or linux and use the appropriate command)
    if os.name == 'nt':
        os.system(
            f"cd {library_path} && python -m venv venv && venv\\Scripts\\activate.bat")

    elif os.name == 'posix':
        os.system(
            f"cd {library_path} && python -m venv venv && source venv/bin/activate")

    # Create the '__init__.py' file to make it a Python package
    with open(os.path.join(library_path, '__init__.py'), 'w') as f:
        pass

    # Create a sample Python file for the library code
    main_module_file_path = os.path.join(library_path, f"{library_name}.py")
    with open(main_module_file_path, 'w') as f:
        f.write(f'def hello():\n    return "Hello from {library_name}"\n')

    # Create a sub-library directory and a sample sub-library module
    sub_lib_name = f"{library_name}_utils"
    sub_lib_path = os.path.join(library_path, sub_lib_name)
    os.makedirs(sub_lib_path, exist_ok=True)
    sub_lib_module_file_path = os.path.join(sub_lib_path, f"{sub_lib_name}.py")
    with open(sub_lib_module_file_path, 'w') as f:
        f.write(
            f'def some_utility():\n    return "This is a utility function from {sub_lib_name}"\n')

    # Copy additional template files
    templates_path = os.path.join(os.path.dirname(__file__), 'templates')
    shutil.copy(os.path.join(templates_path, 'readme_template.md'),
                os.path.join(library_path, 'README.md'))

    # Create setup.py using the template
    with open(os.path.join(templates_path, 'setup_template.py'), 'r') as f:
        setup_template = f.read()
    setup_content = setup_template.format(library_name=library_name)
    with open(os.path.join(library_path, 'setup.py'), 'w') as f:
        f.write(setup_content)

    # create something called updater.py
    with open(os.path.join(templates_path, 'updater_template.py'), 'r') as f:
        updater_template = f.read()
    with open(os.path.join(library_path, 'updater.py'), 'w') as f:
        f.write(updater_template)

    print(f"Successfully created the '{library_name}' library template.")


def main():
    parser = argparse.ArgumentParser(
        description="Create a template for a Python library.")
    parser.add_argument("library_name", help="Name of the library to create.")
    parser.add_argument("--target", "-t", default=".",
                        help="Target folder to create the library (default: current directory).")
    args = parser.parse_args()

    create_library_template(args.library_name, args.target)

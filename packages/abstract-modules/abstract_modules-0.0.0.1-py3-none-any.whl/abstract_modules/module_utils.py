import pkg_resources
import os
import ast
from abstract_gui import get_browser
import os
import ast


def scan_folder_for_required_modules(folder_path=None):
    """
    Scan the specified folder for Python files and create a list of necessary Python modules.
    :param folder_path: The path of the folder to scan. If None, a folder will be picked using a GUI window.
    :return: A list of required Python modules based on all Python files found in the folder.
    """
    if folder_path is None:
        folder_path = get_browser(initial_folder=os.getcwd())["output"]

    required_modules = set()

    def visit_file(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                tree = ast.parse(file.read())
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for name in node.names:
                            required_modules.add(name.name)
                    elif isinstance(node, ast.ImportFrom):
                        module_parts = node.module.split('.')
                        if node.level > 0:
                            module_parts = ['.'.join(module_parts[:node.level])] + module_parts[node.level:]
                        module_name = '.'.join(module_parts)
                        for name in node.names:
                            required_modules.add(f'{module_name}.{name.name}')
        except SyntaxError:
            # Skip files with syntax errors
            pass

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                visit_file(file_path)
    required_list = []
    for each in list(required_modules):
        each = each.split('.')[0]
        if each not in required_list:
            required_list.append(each)
    return required_list

def get_installed_versions(install_requires):
    """
    Get the version numbers of the installed Python modules listed in 'install_requires'.
    :param install_requires: A list of Python module names with optional version constraints.
    :return: A list of module names with their version numbers appended.
    """
    installed_versions = []
    for requirement in install_requires:
        module_name = requirement.split('>=')[0].split('==')[0].strip()
        try:
            version = pkg_resources.get_distribution(module_name).version
        except pkg_resources.DistributionNotFound:
            # Module not found, skip it and continue
            continue

        # Append the version number to the module name in the required format
        if '>=' in requirement:
            installed_versions.append(f'{module_name}>={version}')
        elif '==' in requirement:
            installed_versions.append(f'{module_name}=={version}')
        else:
            installed_versions.append(f'{module_name}>={version}')

    return installed_versions

install_requires=scan_folder_for_required_modules(folder_path=os.getcwd())
input(get_installed_versions(install_requires))

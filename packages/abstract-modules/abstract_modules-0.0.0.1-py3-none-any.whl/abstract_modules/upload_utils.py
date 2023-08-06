import os
import pexpect
from abstract_utilities.read_write_utils import read_from_file,write_to_file
from abstract_utilities.cmd_utils import get_sudo_password,get_env_value,get_sudo_password,cmd_run_sudo,cmd_run,pexpect_cmd_with_args
from abstract_gui import *
from .module_utils import get_installed_versions,scan_folder_for_required_modules
# Load environment variables from .env file
windows_mgr,bridge,script_name=create_window_manager(global_var=globals())
def get_parent_directory(directory:str=os.getcwd()):
    browser_values = None
    while browser_values == None:
        browser_values = get_browser(title="pick a module directory", type="folder", initial_folder=directory)
    # Now you can access the "Browse" key from browser_values dictionary
    if browser_values and "output" in browser_values:
        globals()['parent_dir'] = browser_values["output"]
        # Just for debugging purposes, you can remove this line once it's working correctly
# Call the function to test it

def get_output_txt():
    return os.path.join(parent_dir,'output.txt')
def get_sudo_password():
    return find_and_read_env_file(key="SUDO_PASSWORD")
def get_pypi_username():
    return find_and_read_env_file(key="PYPI_USERNAME")
def get_pypi_password():
    return find_and_read_env_file(key="PYPI_PASSWORD")
def get_src_dir():
    globals()['src_dir'] = os.path.join(parent_dir,project,"src")
def get_project_dirs():
    globals()['project_dirs'] = [name for name in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, name))]
def install_setup():
    return "sudo python3 setup.py sdist"
def install_twine():
    return "pip3 install build twine --break-system-packages"
def build_module():
    # Create the 'dist' directory if it doesn't exist
    if not os.path.exists("dist"):
        os.makedirs("dist")
    return "sudo python3 setup.py bdist_wheel"
def module_upload_cmd():
    return "python3 -m twine upload dist/*.whl --skip-existing"
def upload_module():
    return pexpect_cmd_with_args(command=module_upload_cmd(),child_runs=[{"prompt":"Enter your username: ","pass":None,"key":"PYPI_USERNAME"},{"prompt":"Enter your password: ","pass":None,"key":"PYPI_PASSWORD"}],output_txt=get_output_txt())
def save_new_setup(setup_file):
    with open('setup.py', 'w', encoding='utf-8') as fh:
        fh.write(setup_file)
        setup_file,version_current=read_setup()
def read_setup():
    with open('setup.py', 'r', encoding='utf-8') as fh:
        setup_file = fh.read()
    version_current = setup_file.split('version=')[-1].split(',')[0].strip(" '")
    return setup_file, version_current
def get_install_requires():
    setup_file, version_current = read_setup()
    install_requires = setup_file.split('install_requires=')[-1].split(',')[0]
    install_requires_new = get_installed_versions(scan_folder_for_required_modules())
    if install_requires != install_requires_new:
        permission = get_yes_no(text=f"would you like to change the install requires from {install_requires} to ?'")
        if permission == 'Yes':
            save_new_setup(setup_file.replace(install_requires,install_requires_new))
def get_distributions():
    dist_list = os.listdir('dist')
    version_numbers = []
    for each in dist_list:
        globals()["proj_name"] = each.split('-')[0]
        rest = each[len(proj_name+'-'):]
        version = ''
        while rest[0] in '0123456789.':
            version += rest[0]
            rest = rest[1:]
        if rest[-1] == '.':
            rest = rest[:-1]
        if rest not in version_numbers:
            version_numbers.append(version)
    setup_file, version_current = read_setup()
    while version_current[0] not in '0123456789.':
        version_current = version_current[1:]
    while version_current[-1] not in '0123456789.':
        version_current = version_current[:-1]
    while version_current in version_numbers:
        new_version = windows_mgr.while_basic(windows_mgr.get_new_window(title='version number', args={"layout": [
            [[get_gui_fun("T", {"text": "looks like the version number already exists, please change it"})],
            [get_gui_fun('Input', {"default_text": version_current, "key": "version_number"})],
            [sg.Button("OK")]]]},exit_events=["OK","Override"]))["version_number"]
        version_replace = setup_file.split('version=')[-1].split(',')[0].strip(" '")
        setup_file = setup_file.replace(version_current, new_version)
        version_current = new_version
        override = get_yes_no(text=f"would you like to oveeride the version number with {version_current}?'")
        if override == "Yes":
            break
    globals()["version_current"]= version_current
    # Save the updated version in setup.py
    save_new_setup(setup_file)
def install_module(event):
    if event == "install":
        cmd_run(f'pip install {proj_name}=={version_current} --break-system-packages')
def install_mods_layout():
    win=windows_mgr.get_new_window(title="install module",layout=[[get_gui_fun('Button',{'button_text':'install_module','key':'install'}),get_gui_fun('Button',{'button_text':'exit','key':'EXIT'})]],event_function='install_module')
    while True:
        events = windows_mgr.while_basic(window=win)
        if events == None:
            return 
def get_list_of_projects():
    win=windows_mgr.get_new_window(title="list_window",layout=[[get_gui_fun('Listbox',{"values":os.listdir(parent_dir),"size":(25,10),'key':'projects',"enable_events":True}),get_gui_fun('Button',{'button_text':'submit','key':'exit'})]])
    globals()['project'] = windows_mgr.while_basic(window=win)['projects'][0]
def run_setup_loop():
    cmd_run_sudo(cmd=install_twine(),key="SUDO_PASSWORD")
    get_list_of_projects()
    get_src_dir()
    get_project_dirs()
    globals()['project_dir'] = os.path.join(parent_dir,project)
    os.chdir(project_dir)
    get_distributions()
    get_install_requires()
    print(f"Running setup.py for project: {project_dir}")
    cmd_run_sudo(cmd=install_setup(),key="SUDO_PASSWORD")
    cmd_run_sudo(cmd=build_module(),key="SUDO_PASSWORD")
    upload_module()
    print(f"Completed setup.py for project: {project_dir}")
    install_mods_layout()
def upload_module(directory:str=os.getcwd()):
    get_parent_directory(directory)
    cmd_run(install_twine())
    run_setup_loop()

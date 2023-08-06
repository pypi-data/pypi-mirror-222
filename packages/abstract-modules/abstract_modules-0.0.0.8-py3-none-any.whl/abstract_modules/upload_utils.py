import os
import pexpect
from abstract_utilities.read_write_utils import read_from_file,write_to_file
from abstract_utilities.cmd_utils import get_sudo_password,get_env_value,get_sudo_password,cmd_run_sudo,cmd_run,pexpect_cmd_with_args
from abstract_utilities.string_clean import eatAll
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

def get_output_text():
    return os.path.join(parent_dir,'output.txt')
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
    return pexpect_cmd_with_args(command=module_upload_cmd(),child_runs=[{"prompt":"Enter your username: ","pass":None,"key":"PYPI_USERNAME"},{"prompt":"Enter your password: ","pass":None,"key":"PYPI_PASSWORD"}],output_text=get_output_text())
def save_new_setup(setup_file):
    with open('setup.py', 'w', encoding='utf-8') as fh:
        fh.write(setup_file)
def read_setup():
    with open('setup.py', 'r', encoding='utf-8') as fh:
        setup_file = fh.read()
    cleaner_ls =['',' ','\n','\t','"',"'"]
    version = eatAll(x=setup_file.split('version=')[-1].split(',')[0],ls=cleaner_ls)
    name= eatAll(x=setup_file.split('name=')[-1].split(',')[0],ls=cleaner_ls)
    url = eatAll(x=setup_file.split('url=')[-1].split(',')[0],ls=cleaner_ls)
    install_requires = eatAll(x=setup_file.split('install_requires=')[-1].split(']')[0]+']',ls=cleaner_ls)
    return {"file":setup_file,"version":version,"name":name,"url":url,"install_requires":install_requires}
def get_url(setup_js):
    if setup_js["url"].split('/')[-1] != setup_js["name"]:
        url_new = setup_js["url"][:-len(setup_js["url"].split('/')[-1])]+setup_js["name"]
        permission = get_yes_no(text=f"would you like to change the url requires from {setup_js['url']} to {url_new}?'")
        windows_mgr.while_quick(windows_mgr.get_new_window(title='version number', args={"layout": [
                [[get_gui_fun("T", {"text": "would you like to change the url requires from {setup_js['url']} to {url_new}?"})],
                [get_gui_fun('Input', {"default_text": url_new, "key": "output"})],
                [sg.Button("OK")]]]},exit_events=["OK","Override"]))["output"]
        if permission == 'Yes':
            save_new_setup(read_setup()["file"].replace(install_requires,install_requires_new))
def get_install_requires(setup_js):
    install_requires_new = get_installed_versions(scan_folder_for_required_modules())
    if setup_js['install_requires'] != install_requires_new:
        permission = get_yes_no(text=f"would you like to change the install requires from {setup_js['install_requires']} to {install_requires_new}?'")
        if permission == 'Yes':
            save_new_setup(read_setup()["file"].replace(str(setup_js['install_requires']),str(install_requires_new)))
def organize_versions_from_high_to_low(version_list):
    """
    Organize the list of version numbers from highest to lowest.
    :param version_list: A list of version numbers to organize.
    :return: A new list of version numbers sorted from highest to lowest.
    """
    sorted_versions = sorted(version_list, key=lambda x: list(map(int, x.split('.'))), reverse=True)
    return sorted_versions

def get_distributions_from_packages(setup_js,version_numbers):
    if os.path.isdir('dist'):
        dist_list = os.listdir('dist')
        for dist in dist_list:
            rest = dist[len(setup_js['name'] + '-'):]
            version = ''
            while len(rest) > 0 and rest[0] in '0123456789.':
                version += rest[0]
                rest = rest[1:]
            version = version.rstrip('.')
            if version not in version_numbers:
                version_numbers.append(version)
    return version_numbers
def get_version_text(current_version,version_numbers):
    text = ''
    version_number_exists = False
    version_number_highest = True
    if current_version not in version_numbers:
        version_numbers.append(current_version)
    else:
        version_number_exists = True
        text = f'Version number {current_version} already exists.'
    version_numbers = organize_versions_from_high_to_low(version_numbers)
    if version_numbers[0] != current_version:
        version_number_highest = False
        text = text + f" Your version number {current_version} is lower than the highest version number {version_numbers[0]}."
    return text,version_number_highest
def get_distributions(setup_js):
   
    version_numbers = get_distributions_from_packages(setup_js,[])
    installed_versions = get_installed_versions(setup_js['name'])
    for version in installed_versions:
        version_number = version.split('=')[-1]
        if version_number not in version_numbers:
            version_numbers.append(version_number)
    new_version = setup_js['version']
    
    while get_version_text(new_version,version_numbers)[1] !=True:
        text = get_version_text(new_version,version_numbers)[0] +' please enter a new version number'
        layout = [
            [get_gui_fun("T", {"text": text})],
            [get_gui_fun('Input', {"default_text": organize_versions_from_high_to_low(version_numbers)[0], "key": "version_number"})],
            [sg.Button("OK")]
        ]
        new_version = windows_mgr.while_basic(windows_mgr.get_new_window(title='Version number', args={"layout": layout},exit_events=["OK", "Override"]))["version_number"]
        setup_file = setup_file.replace(current_version, new_version)
        override_prompt = f"Would you like to override the version number with {new_version}?"
        override = get_yes_no(text=override_prompt)
        if override == "Yes":
            break

    globals()["version_current"] = new_version
    # Save the updated version in setup.py
    save_new_setup(setup_file = read_setup()['file'].replace(setup_js['version'], new_version))
def install_module(event):
    if event == "install":
        cmd_run(f'pip install {read_setup()["name"]}=={read_setup()["version"]} --break-system-packages')
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
    cmd_run_sudo(cmd=install_twine(),key="SUDO_PASSWORD",output_text="/home/john-putkey/Documents/python_projects/modules/abstract_essentials/output.txt")
    get_list_of_projects()
    get_src_dir()
    get_project_dirs()
    globals()['project_dir'] = os.path.join(parent_dir,project)
    os.chdir(project_dir)
    setup_js = read_setup()
    get_distributions(setup_js)
    get_install_requires(setup_js)
    get_url(setup_js)
    print(f"Running setup.py for project: {project_dir}")
    cmd_run_sudo(cmd=install_setup(),key="SUDO_PASSWORD",output_text="/home/john-putkey/Documents/python_projects/modules/abstract_essentials/output.txt")
    cmd_run_sudo(cmd=build_module(),key="SUDO_PASSWORD",output_text="/home/john-putkey/Documents/python_projects/modules/abstract_essentials/output.txt")
    upload_module()
    print(f"Completed setup.py for project: {project_dir}")
    install_mods_layout()
def upload_main(directory:str=os.getcwd()):
    get_parent_directory(directory)
    run_setup_loop()

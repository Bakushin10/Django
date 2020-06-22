import glob, os, shutil
import subprocess
import sys

def install_dependencies():
    """
    installing the dependencies from 'dst'
    """
    absolute_path_to_package = "/home/wasuser/.local/share/virtualenvs/api-veReZ-M2/lib/python3.7/site-packages/"
    
    whl_path = dst + "*.whl"
    tar_gz_path = dst + "*.gz"
    print("serching .whl and .gz file in {}".format(dst))
    whl_file_list, tar_gz_file_list = get_all_package(whl_path, tar_gz_path)

    # install whl files
    for whl_file in whl_file_list:
        whl_file = whl_file.replace(" ", "")
        if os.path.isfile(whl_file):
            # install the dependencies
            whl_file = whl_file.replace("\\", "/")
            print("--- installing {}".format(whl_file))
            subprocess.check_call([sys.executable, "-m", "pip", "install", whl_file, "--find-links", absolute_path_to_package, "--no-index"])

    # install tar_gz file
    for gz_file in tar_gz_file_list:
        gz_file = gz_file.replace(" ", "")
        if os.path.isfile(gz_file):
            # install the dependencies
            gz_file = gz_file.replace("\\\\", "/")
            print("--- installing {}".format(gz_file))
            install_command = f"install {gz_file} --find-links {absolute_path_to_package} "
            subprocess.check_call([sys.executable, "-m", "pip", "install", gz_file, "--find-links", absolute_path_to_package, "--no-index"])

def get_all_package(whl_path, tar_gz_path):
    whl_files = glob.iglob(os.path.join(source_dir, whl_path))
    tar_gz_files = glob.iglob(os.path.join(source_dir, tar_gz_path))

    file_str = str(list(whl_files)).replace("[","").replace("]","")
    whl_file_list= file_str.replace("'","").replace("'","").split(",")

    file_str = str(list(tar_gz_files)).replace("[","").replace("]","")
    tar_gz_file_list= file_str.replace("'","").replace("'","").split(",")

    return whl_file_list, tar_gz_file_list


if __name__ == "__main__":
    source_dir = '' #Path where your files are at the moment
    dst = '' #Path you want to move your files to

    install_dependencies()

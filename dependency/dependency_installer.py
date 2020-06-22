import glob, os, shutil
import subprocess
import sys

def install_dependencies():
    """
    installing the dependencies from 'dst'
    """
    whl_path = dst + "*.whl"
    tar_gz_path = dst + "*.gz"
    print("serching .whl and .gz file in {}".format(dst))
    whl_file_list, tar_gz_file_list = get_all_package(whl_path, tar_gz_path)

    # whl files
    for whl_file in whl_file_list:
        whl_file = whl_file.replace(" ", "")
        if os.path.isfile(whl_file):
            # install the dependencies
            whl_file = whl_file.replace("\\", "/")
            print("--- installing {}".format(whl_file))
            install_command = f"{whl_file}  --no-index --find-links {whl_file}"
            subprocess.check_call([sys.executable, "-m", "pip", "install",install_command])
            #subprocess.check_call([sys.executable, "-m", "pip", install_command, whl_file])

    # tar_gz file
    for gz_file in tar_gz_file_list:
        gz_file = gz_file.replace(" ", "")
        if os.path.isfile(gz_file):
            # install the dependencies
            gz_file = gz_file.replace("\\\\", "/")
            print("--- installing {}".format(gz_file))
            install_command = f"install {gz_file}  --no-index --find-links {gz_file}"
            subprocess.check_call([sys.executable, "-m", "pip", "install",install_command])

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

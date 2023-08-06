import os


class FactorySetting:
    @staticmethod
    def check_file_or_folder_exists(path):
        return os.path.exists(path)

    @staticmethod
    def delete_config_folder():
        path = f"{config_path()}"
        cmd = f"rmdir /s /q {path}"
        if not inside_windows():
            path = path.replace("\\", "/")
            cmd = f"rm -rf {path}"
        os.popen(cmd).read()

    @staticmethod
    def make_config_folder_ready(folder_path):
        ################################temporary remove all subscriptions

        if not inside_windows():
            folder_path = folder_path.replace("\\", "/")
        cmd = f"mkdir {folder_path}"
        if not inside_windows():
            cmd = f"mkdir -p {folder_path}"
        os.popen(cmd).read()

    gui_config = """
{
    "local_port": "8080",
    "selected_profile_name": "",
    "selected_profile_number": 0,
    "use_fragmentation": false,
    "keep_top": false,
    "close_to_tray": false,
    "auto_connect": false,
    "start_minimized": false,
    "cloudflare_address": "bruce.ns.cloudflare.com",
    "segmentation_timeout": "5",
    "num_of_fragments": "77",
    "subscription": ""
}"""


def inside_windows():
    inside_window = False
    if os.name == "nt":
        inside_window = True
    return inside_window


def config_path():
    inside_window = False
    if os.name == "nt":
        inside_window = True

    if inside_window:
        config_path = f"{os.getenv('USERPROFILE')}\\appdata\\roaming\\v2rayp\\configs"
    else:
        config_path = f'{os.popen("cd ~;pwd").read().strip()}/Documents/v2rayp/configs'
    return config_path


if __name__ == "__main__":
    print(config_path())

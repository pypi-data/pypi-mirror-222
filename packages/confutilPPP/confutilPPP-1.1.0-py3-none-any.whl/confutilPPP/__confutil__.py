import argparse
import os

import logPPP
import yaml

LOG_IS_COLOR = True


class confutil:
    def __init__(self):
        pass

    # 获取参数
    @staticmethod
    def _parse_arguments():
        parser = argparse.ArgumentParser()
        default_config_path = os.path.join(os.getcwd(), 'config.yaml')
        parser.add_argument("--configpath", "-c", default=default_config_path, nargs=1, help="配置文件")
        return parser.parse_args()

    # 检查解析参数
    @staticmethod
    def check_config(_object=None, _filename='config'):
        try:
            # 解析参数
            config_path = confutil._parse_arguments().configpath
            # 如果*.yaml文件不存在或者为空
            if not os.path.isfile(config_path) or os.path.getsize(config_path) == 0:
                # 使用os.path模块获取文件名和文件路径
                file_name = os.path.basename(config_path)
                file_path = os.path.dirname(config_path)
                # 检查文件名是否以.yaml结尾
                if file_name.endswith('.yaml'):
                    # 生成新的文件路径
                    config_path = os.path.join(file_path, file_name[:-5] + '.yml')
        except Exception:
            logPPP.error('构建配置文件路径失败！', is_color=LOG_IS_COLOR)
            return None

        # 如果文件不存在或者为空，创建文件并写入
        try:
            if not os.path.isfile(config_path) or os.path.getsize(config_path) == 0:
                with open(config_path, 'w', encoding='utf_8') as f:
                    f.write(yaml.dump(_object, allow_unicode=True, sort_keys=False, default_flow_style=False))
        except Exception:
            logPPP.error('创建配置文件失败！', is_color=LOG_IS_COLOR)
            return None

        # 读取YAML文件
        try:
            with open(config_path, 'r', encoding='utf_8') as f:
                logPPP.info("配置文件:", config_path, is_color=LOG_IS_COLOR)
                return yaml.safe_load(f)
        except Exception:
            logPPP.error("读取配置文件失败,检查配置文件格式是否正确！", is_color=LOG_IS_COLOR)
            return None

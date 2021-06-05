from airtest.core.api import *
from conf.default import DefaultConfig, BASE_PROJECT


class BasePage:
    def __init__(self, poco):
        self._poco = poco

    def check_env_message(self):
        """检查是否有环境弹窗，有就点掉"""
        env_message = self.poco(text="取消")
        if env_message:
            env_message.click()

    def poco(self, *args, **kwargs):
        return self.wait_for(self._poco(*args, **kwargs))

    def up(self):
        """"向上滑动"""
        self._poco.swipe([0.5, 0.8], [0.5, 0.2])

    def down(self):
        """向下滑动"""
        self._poco.swipe([0.5, 0.1], [0.5, 0.9])

    def left(self):
        """向左滑动"""
        self._poco.swipe([0.1, 0.5], [0.9, 0.5])

    def right(self):
        """向右滑动"""
        self._poco.swipe([0.9, 0.5], [0.1, 0.5])

    def exists(self, *args, **kwargs):
        """判断某个元素是否存在"""
        exists(self._poco(*args, **kwargs))

    @staticmethod
    def get_image_element(page_name, file_name, *args, **kwargs):
        """根据页面名称和文件名查找图片对象"""
        file_path = os.path.join(os.path.join(BASE_PROJECT, "files"), page_name)
        file_name = file_name if file_name.endswith("png") or file_name.endswith("jpg") else f"{file_name}.png"
        return Template(os.path.join(file_path, file_name), *args, **kwargs)

    @staticmethod
    def input(message):
        """输入"""
        text(message)

    @staticmethod
    def stop():
        """关闭APP"""
        stop_app(DefaultConfig.app_package_name)

    @staticmethod
    def start():
        """开启APP"""
        start_app(DefaultConfig.app_package_name)

    @staticmethod
    def wait_for(poco, times=20):
        sleep(0.5)
        for x in range(times):
            print(f"当前第{x}次查找{poco}")
            if poco.exists():
                sleep(0.2)
                return poco
            else:
                sleep(0.5)
                continue
        return None

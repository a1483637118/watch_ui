from utils.session import PocoSession


class BaseTest:
    _poco = PocoSession().get_poco()



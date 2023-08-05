from .__confutil__ import confutil, LOG_IS_COLOR

__all__ = ['__version__', 'check_config', 'LOG_IS_COLOR']
__version__ = '1.1.0'


def check_config(_object=None, _filename='config'):
    return confutil.check_config(_object, _filename)

from importlib import import_module
import time
import logging
import glob
import os
import sys

logger = logging.getLogger('lnxlink')


def autoload_modules(auto_exclude):
    modules = []
    modules_path = f"{os.path.dirname(__file__)}/*.py"
    for module_path in glob.glob(modules_path):
        module = os.path.basename(module_path)
        if '__' not in module and '.py' in module:
            module = module.replace('.py', '')
            if module not in auto_exclude:
                modules.append(module)

    return modules


def parse_modules(list_modules=None, auto_exclude=[]):
    os.environ["DISPLAY"] = ':0'
    if list_modules is None:
        list_modules = autoload_modules(auto_exclude)
    modules = {}
    for module_name in list_modules:
        retries = 10
        while retries >= 0:
            try:
                if '.py' in module_name:
                    module_path = os.path.dirname(module_name)
                    module_basename = os.path.basename(module_name)
                    module_name = os.path.splitext(module_basename)[0]
                    sys.path.append(module_path)
                    addon = getattr(import_module(f"{module_name}"), 'Addon')
                else:
                    addon = getattr(import_module(f"{__name__}.{module_name}"), 'Addon')
                addon.service = module_name
                modules[module_name] = addon
                retries = -1
            except ModuleNotFoundError as e:
                logger.error(f"Addon {module_name} is not supported, please remove it from your config: {e}")
                retries = -1
            except Exception as e:
                logger.error(f"Error with module {module_name}: {e}")
                time.sleep(2)
                retries -= 1
    logger.info(f"Loaded addons: {', '.join(modules)}")
    return modules

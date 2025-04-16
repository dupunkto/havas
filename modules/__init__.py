import os
import importlib

def load_modules():
    modules = []
    base_path = os.path.dirname(__file__)

    for file_item in os.scandir(base_path):
        if file_item.is_dir():
            routes_path = os.path.join(file_item.path, "routes.py")
            if os.path.isfile(routes_path):
                module_path = f"modules.{file_item.name}.routes"
                try:
                    module = importlib.import_module(module_path)
                    
                    for attr in dir(module):
                        if attr.endswith("_module"):
                            module_name = getattr(module, attr)
                            modules.append((module_name, f"/{file_item.name}"))
                except Exception as e:
                    print(f"An error occured while trying to load {module_path}: {e}")

    return modules

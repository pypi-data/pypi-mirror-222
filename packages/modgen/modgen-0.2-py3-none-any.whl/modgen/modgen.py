def create(module_name, module_location):
    import sys
    import types
    import importlib.machinery
    loader = importlib.machinery.SourceFileLoader(module_name, module_location)
    code = loader.get_code(module_name)
    new_module = types.ModuleType(loader.name)
    exec(code, new_module.__dict__)
    sys.modules[loader.name] = new_module
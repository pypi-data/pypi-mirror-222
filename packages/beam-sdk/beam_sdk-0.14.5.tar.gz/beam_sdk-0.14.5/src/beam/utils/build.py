import importlib
import json
import sys
import os
import inspect
import unittest.mock
import sys

from typing import TextIO
from beam import App
from typing import Optional
from types import ModuleType


BLACKLISTED_MODULES = ["_winapi", "chardet", "packaging"]
imported_paths = []


class MockModuleLoader:
    def __init__(self, name):
        self.name = name

    def load_module(self, name):
        if name in sys.modules:
            return sys.modules[name]

        for finder in sys.meta_path[1:]:
            try:
                spec = finder.find_spec(name, None)
                if spec is not None:
                    if spec.loader is not self:
                        module = importlib.util.module_from_spec(spec)
                        sys.modules[name] = module
                        spec.loader.exec_module(module)
                        return module
            except ImportError:
                pass

        module = unittest.mock.MagicMock(name=name)
        sys.modules[name] = module
        return module

    def exec_module(self, module):
        pass

    def create_module(self, spec):
        if spec is None:
            return None
        elif spec.loader is not self:
            module = importlib.util.module_from_spec(spec)
            return module
        else:
            return unittest.mock.MagicMock(name=spec.name)


class FallbackImport:
    def find_spec(self, fullname, path=None, target=None):
        spec = None

        if fullname in BLACKLISTED_MODULES:
            return None

        try:
            # Try all other importers first, skipping FallbackImport
            for importer in list(sys.meta_path):  # First make a copy of sys.meta_path
                if importer is self:
                    continue
                try:
                    spec = importer.find_spec(fullname, path, target)
                    if spec is not None:
                        break
                except AttributeError:
                    pass

            # If no other importer can handle the module, and spec is still None
            if spec is None:
                raise ModuleNotFoundError

            imported_paths.append(path)
        except:
            if path in imported_paths:
                return None

            # If the standard import fails, engage the fallback logic
            loader = MockModuleLoader(fullname)
            spec = importlib.util.spec_from_loader(fullname, loader, is_package=True)

        return spec


class AppBuilder:
    @staticmethod
    def _setup():
        if os.getenv("BEAM_IGNORE_IMPORTS_OFF", None) is None:
            sys.meta_path.insert(0, FallbackImport())

    @staticmethod
    def _find_app_in_module(app_module: ModuleType) -> str:
        app = None
        for member in inspect.getmembers(app_module):
            member_value = member[1]
            if isinstance(member_value, App):
                app = member_value
                break

        if app is not None:
            return json.dumps(app())

        raise RuntimeError("Beam app not found")

    @staticmethod
    def build(*, module_name: str, func_or_app_name: Optional[str]) -> str:
        AppBuilder._setup()

        if not os.path.exists(module_name):
            raise FileNotFoundError

        # Override stdout
        stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

        # Load module
        spec = importlib.util.spec_from_file_location(module_name, module_name)
        app_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(app_module)

        sys.meta_path.pop(0)
        if func_or_app_name is None:
            config = AppBuilder._find_app_in_module(app_module)
            return AppBuilder._print_config(stdout, config)

        try:
            _callable = getattr(app_module, func_or_app_name)
            config = json.dumps(_callable())
            return AppBuilder._print_config(stdout, config)
        except AttributeError:
            raise

    @staticmethod
    def _print_config(stdout: TextIO, config: str) -> None:
        stdout.write(str(config))
        stdout.flush()
        sys.stdout = stdout


if __name__ == "__main__":
    """
    Usage:
        python3 -m beam.build <module_name.py>:<func_name>
            or
        python3 -m beam.build <module_name.py:<app_name>
    """

    app_handler = sys.argv[1]
    module_name = app_handler
    func_or_app_name = None
    try:
        module_name, func_or_app_name = app_handler.split(":")
    except ValueError:
        pass

    AppBuilder.build(module_name=module_name, func_or_app_name=func_or_app_name)

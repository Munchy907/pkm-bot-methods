import importlib
import os

from discord import NoEntryPointError
from discord.ext.commands import Bot


def has_method(module_name, package=None, method_name='setup'):
    try:
        module = importlib.import_module(f".{module_name}", package)
        return hasattr(module, method_name)
    except ImportError:
        print('import error why?')
        return False


def load_cog_files(bot: Bot, dirs: list[str]):
    for cog_dir in dirs:
        files = os.listdir(cog_dir)

        package = cog_dir.replace('./', '')
        package = package.replace('/', '.')

        for file in files:
            if '__' in file or not ('.py' in file):
                continue

            file = file.replace('.py', '')
            print(f"{package}.{file}")
            try:
                bot.load_extension(f"{package}.{file}")
            except NoEntryPointError:
                print(f"Error {file}.py missing setup function")

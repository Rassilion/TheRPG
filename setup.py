from cx_Freeze import setup, Executable

setup(name="rpg",
      version="0.1",
      description="My rpg",
      executables=[Executable("rpg.py")])

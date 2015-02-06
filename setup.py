import cx_Freeze
 
executables = [cx_Freeze.Executable("main.py")]
 
cx_Freeze.setup(
    name="Mage Knight",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["data/", "assets/", "fonts/"]}},
    executables = executables
 
    )
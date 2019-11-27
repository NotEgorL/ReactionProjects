import cx_Freeze

executables = [cx_Freeze.Executable("roadcaster (straight).py")]

cx_Freeze.setup(
    name="VAPORWAVE",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["player_car.png","stripes.png","road3.png","1.jpg"]}},
    executables = executables

    )

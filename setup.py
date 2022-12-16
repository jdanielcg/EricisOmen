
import cx_Freeze

executables = [cx_Freeze.Executable('main.py',icon='omenicon4.ico')]

cx_Freeze.setup(
    name="OMEN",
    options={'build_exe': {'packages':['pygame', 'numpy'],
                           'include_files':['assets', 'world.tmj', 'edit_terrain.png']}},

    executables = executables
    
)
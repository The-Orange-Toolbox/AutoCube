# AutoCube

Automates cubemap generation for Source Engine games during compile-time.

Download: [see the release page](https://github.com/The-Orange-Toolbox/AutoCube/releases)

## Installation

### Using with CompilePal
AutoCube is packaged as ready to be used in CompilePal. Follow these quick steps to install it:
- Copy the AutoCube folder into "Compile Pal 02x.xx/Parameters"
- Restart CompilePal.
- From the CompilePal UI, use the "Add..." button to add AutoCube to your list of executables.
- Tick the checkmark to have it run on your next compile.

### Using with Hammer (expert compile)
The executable can be used standalone without any of the other files it is bundled with. Follow these quick steps to add it to your Hammer compile:
- Copy the AutoCube.exe from AutoCube/ to your bin folder (e.g. steamapps/common/Team Fortress 2/bin, or any prefered folder).
- In Hammer's expert compile window, use the "New" button to add a new command.
- For the command, click the "Cmds" button, select "executable", select the location of the AutoCube.exe.
- For the parameters, add `$file --exe $game_exe --game $gamedir` into the text field.
- Use the "Move Up"/"Move Down" buttons to order the command properly (recommended to be placed after the copy command).
- Hit "Go!" and compile away!

### Using with command line
Run the executable with `AutoCube --help` for complete information about its usage.

## CS:GO Caveats
CSGO requires additional arguments in order to work. Make sure you include the --steamexe and --appid arguments with their appropriate values

# VolumeVoyager

## Overview
VolumeVoyager is a Python program designed to manage and customize audio settings for different environments on Windows devices. It allows users to easily switch between predefined audio profiles for activities like working, gaming, listening to music, and watching movies.

## Features
- **Environment Management**: Define custom volume levels for different environments.
- **Easy Switching**: Quickly change audio settings based on your current activity.
- **Customizable**: Add, remove, or modify environments and their volume levels.

## Requirements
- Python 3.x
- `nircmd.exe` (A small command-line utility for Windows to control the system volume)

## Installation
1. Ensure Python 3.x is installed on your Windows machine.
2. Download `nircmd.exe` from [NirSoft](https://www.nirsoft.net/utils/nircmd.html) and place it in the same directory as `VolumeVoyager.py`.
3. Clone the repository or download the `VolumeVoyager.py` file.

## Usage
1. Run the script using Python:
   ```bash
   python VolumeVoyager.py
   ```
2. The program will display available environments and their volume levels.
3. Use the provided functions to manage environments:
   - `change_environment(environment)`: Change the volume to the specified environment's settings.
   - `add_environment(environment, volume_level)`: Add a new environment with a specified volume level.
   - `remove_environment(environment)`: Remove an existing environment.
   - `list_environments()`: List all available environments and their volume levels.

## Customization
To customize the default environments and volume settings, edit the `volume_settings.json` file generated after the first run of the program. You can add new environments or adjust volume levels as needed.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
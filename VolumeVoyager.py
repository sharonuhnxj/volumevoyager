import os
import subprocess
import json

class VolumeVoyager:
    def __init__(self):
        self.settings_file = "volume_settings.json"
        self.default_settings = {
            "work": 50,
            "gaming": 70,
            "music": 80,
            "movie": 60
        }
        self.load_settings()

    def load_settings(self):
        if not os.path.exists(self.settings_file):
            with open(self.settings_file, 'w') as file:
                json.dump(self.default_settings, file, indent=4)
        with open(self.settings_file, 'r') as file:
            self.settings = json.load(file)

    def save_settings(self):
        with open(self.settings_file, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def set_volume(self, level):
        # Windows command to set the volume
        command = f"nircmd.exe setsysvolume {level * 655.35}"
        subprocess.run(command, shell=True)

    def change_environment(self, environment):
        if environment in self.settings:
            volume_level = self.settings[environment]
            self.set_volume(volume_level)
            print(f"Volume set to {volume_level}% for {environment} environment.")
        else:
            print(f"Environment '{environment}' not found. Available environments: {list(self.settings.keys())}")

    def add_environment(self, environment, volume_level):
        self.settings[environment] = volume_level
        self.save_settings()
        print(f"Environment '{environment}' added with volume level {volume_level}%.")

    def remove_environment(self, environment):
        if environment in self.settings:
            del self.settings[environment]
            self.save_settings()
            print(f"Environment '{environment}' has been removed.")
        else:
            print(f"Environment '{environment}' does not exist.")

    def list_environments(self):
        print("Available environments and their volume levels:")
        for env, level in self.settings.items():
            print(f"{env}: {level}%")

if __name__ == "__main__":
    voyager = VolumeVoyager()
    voyager.list_environments()
    voyager.change_environment("work")
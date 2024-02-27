import json

def load_preferences(file_path):
    try:
        with open(file_path, 'r') as f:
            preferences = json.load(f)
    except FileNotFoundError:
        preferences = create_default_preferences(file_path)
    return preferences

def save_preferences(preferences, file_path):
    with open(file_path, 'w') as f:
        json.dump(preferences, f, indent=4)

def create_default_preferences(file_path):
    default_preferences = {
        "d2r_file_path": "path/to/file.txt",
        "d2nd_file_path": "path/to/file.txt",
        "char_file_path": "path/to/file.txt",
        "char_backup_file_path": "path/to/file.txt",
        "backup_on_startup": True,
        "update_on_startup": True,
        "enable_beta_updates": True,
        
        "mon_den_normal": 1,
        "mon_den_nightmare": 1,
        "mon_den_hell": 1,
        "cmon_spawn_normal": 1,
        "cmon_spawn_nightmare": 1,
        "cmon_spawn_hell": 1,
        "umon_spawn_normal": 1,
        "umon_spawn_nightmare": 1,
        "umon_spawn_hell": 1,

        "inventory_tab1": "Personal",
        "inventory_tab2": "Shared",
        "inventory_tab3": "Shared",
        "inventory_tab4": "Shared",
        "inventory_tab5": "Shared",
        "inventory_tab6": "Shared",
        "inventory_tab7": "Shared",
        "inventory_tab8": "Shared",

        "enable_free_respec": False
        }

    save_preferences(default_preferences, file_path)
    return default_preferences

# Example usage:
preferences_file = 'preferences.json'
preferences = load_preferences(preferences_file)

# Modify preferences as needed
preferences['umon_spawn_hell'] = 8
# preferences['boolean_value'] = True
# preferences['file_path'] = "new/path/to/file.txt"

# Save preferences
save_preferences(preferences, preferences_file)
print("Preferences saved.")

# Downloads-Organizer
A small application to organize your downloads into manageable folders.

# How it works
It's a simple implementation of iterating through dicts containing a parent folder path and an array of file extentions that will be put into that parent folder. This is configurable in the `config.toml` file.

# Current Features
- Organize files into user specified folders.
- Configurable in a TOML file.

# Planned Features
- Duplicate folder handling
- Duplicate file handling

# How to configure
1. Open `config.toml`
2. Look for the table `[downloads]` and specify your downloads folder path within the double quotes.
3. To specify a folder to put files into, create a new table following this format:
```
[[folders]]
folder_path ="path_to_the_folder"
extentions = [
".your_extention1", ".your_extention2", ".yourextention3"
]
```
4. Save the `config.toml` file.

You can have as many folders and extentions as you like, provided the folders and extentions are not duplicates of one another.

# How to run
In the terminal, run it as follows: `python main.py`

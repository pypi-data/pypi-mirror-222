import configparser
import hashlib
from pathlib import Path


# Global constant for the .subsys folder
SUBSYS_FOLDER = Path(".subsys")

# Function to generate a unique ID based on content (SHA-1 hash)
def generate_id(content):
    sha1 = hashlib.sha1()
    sha1.update(content)
    return sha1.hexdigest()

# Function to check if the repository has been initialized
def is_initialized():
    current_directory = Path.cwd()
    while current_directory != Path("/"):
        subsys_folder = current_directory / SUBSYS_FOLDER
        if subsys_folder.exists():
            return True
        
        current_directory = current_directory.parent

    return False

# Function to write the configuration to the config file inside the .subsys folder
def write_config(code, student_id):
    config = configparser.ConfigParser()
    config["DEFAULT"] = {"Code": code, "StudentID": student_id}
    config_folder = SUBSYS_FOLDER
    config_folder.mkdir(parents=True, exist_ok=True)
    config_path = config_folder / ".subsysconfig"
    with open(config_path, "w") as configfile:
        config.write(configfile)

# Function to read the configuration from the config file inside the .subsys folder
def read_config():
    config = configparser.ConfigParser()
    config_file = SUBSYS_FOLDER / ".subsysconfig"
    if config_file.exists():
        config.read(config_file)
    return config

# Function to update the configuration with the submission ID
def update_submission_id(submission_id):
    config = read_config()
    config.set("DEFAULT", "SubmissionID", submission_id)

    config_file = SUBSYS_FOLDER / ".subsysconfig"
    with open(config_file, "w") as configfile:
        config.write(configfile)

# Function to recursively list all files in a directory, excluding the .subsys directory and files in .subsysignore
def list_all_files(directory, ignore_list):
    all_files = []
    for path in directory.rglob("*"):
        if path.is_file() and not str(path).startswith(".subsys") and path.name not in ignore_list:
            ignore_file = any(ignore_pattern in str(path) for ignore_pattern in ignore_list)
            if not ignore_file:
                all_files.append(path)
    return all_files

# Function to read the contents of .subsysignore file
def read_ignore_file():
    ignore_list = []
    ignore_file = SUBSYS_FOLDER / ".subsysignore"
    if ignore_file.exists():
        with ignore_file.open() as f:
            ignore_list = f.read().splitlines()
    return ignore_list

# Function to read the list of unique slugs from the SLUGS file
def read_unique_slugs():
    slugs_file = SUBSYS_FOLDER / "SLUGS"
    unique_slugs = []
    if slugs_file.exists():
        with slugs_file.open() as f:
            unique_slugs = f.read().splitlines()
    return unique_slugs

# Function to save the provided slug to the SLUGS file
def save_slug(slug, snap_id):
    slugs_file = SUBSYS_FOLDER / "SLUGS"
    with slugs_file.open("a") as f:
        f.write(f"{slug} {snap_id}\n")

# Function to read the slugs and their corresponding snap IDs from the SLUGS file
def read_slug_file():
    slugs_file = SUBSYS_FOLDER / "SLUGS"
    slugs = {}

    if slugs_file.exists():
        with slugs_file.open() as f:
            for line in f:
                slug, snap_id = line.strip().split(" ")
                slugs[slug] = snap_id

    return slugs

from pathlib import Path

import click

from utils.misc import generate_id, list_all_files, read_ignore_file
from utils.snap import get_last_snap_files


# Function to get unchanged files
def get_unchanged_files(files, ignore_list):
    unchanged_files = []

    last_snap_files = get_last_snap_files()

    if not last_snap_files:
        last_snap_files_dict = {}
    else:
        last_snap_files_dict = dict(last_snap_files)

    for file in files:
        if file not in ignore_list:
            file_hash = generate_id(file.read_bytes())
            last_snap_hash = last_snap_files_dict.get(str(file), None)
            if last_snap_hash is not None and file_hash == last_snap_hash:
                unchanged_files.append(file)

    return unchanged_files

# Function to stage changes by adding files to the index
def stage_changes(files, ignore_list):
    index_file = Path(".subsys") / "index"
    staged_files = set()

    # Read the existing index content and store the files that are already staged
    if index_file.exists():
        with index_file.open() as index:
            for line in index:
                file_hash, file_path = line.strip().split(" ", 1)
                staged_files.add(file_path)

    # Get file hashes and paths from the last snap and its parent snaps
    all_snap_files = []
    deleted_paths = set()
    head_file = Path(".subsys") / "HEAD"
    main_branch_file = Path(".subsys") / head_file.read_text().strip()

    current_snap_id = main_branch_file.read_text().strip()
    while current_snap_id:
        current_snap_object = Path(".subsys") / "objects" / f"sn_{current_snap_id}"
        with current_snap_object.open() as snap_file:
            snap_content = snap_file.read()
            snap_lines = snap_content.strip().split("\n")
            for line in snap_lines:
                if not line.startswith("snap") and not line.startswith("Date:") and not line.startswith("Slug:") and not line.startswith("Parent:"):
                    file_hash, file_path = line.split(" ", 1)
                    if file_hash == "DELETED":
                        deleted_paths.add(Path(file_path.strip()))
                    all_snap_files.append((file_hash, file_path.strip()))        
        # Get the parent snap ID from the current snap content, if available
        parent_snap_id = None
        for line in snap_lines:
            if line.startswith("Parent:"):
                parent_snap_id = line.split(":", 1)[1].strip()
                break

        current_snap_id = parent_snap_id

    # Create a set of ignored files or directories based on the ignore list
    ignored_paths = set()
    for ignore_pattern in ignore_list:
        ignored_paths.update(Path(".").rglob(ignore_pattern))

    # Determine the changes for each file in the working directory
    for file in files:
        if file not in ignored_paths:
            file_hash = generate_id(file.read_bytes())

            # Check if the file has changed, is newly added, or deleted
            last_snap_hash = next((hash for hash, path in all_snap_files if path == str(file)), None)
            if last_snap_hash == "DELETED":
                # print(file)
                continue
            elif last_snap_hash is None:
                # File is newly added, stage it for addition
                with index_file.open("a") as index:
                    index.write(f"{file_hash} {file}\n")
                    staged_files.add(file_hash)
            elif file_hash != last_snap_hash and last_snap_hash != "DELETED":
                # File has changed, stage it for modification
                with index_file.open("a") as index:
                    index.write(f"{file_hash} {file}\n")
                    staged_files.add(file_hash)

    # Check for deleted files
    for hash, path in all_snap_files:
        file_path = Path(path)
        if file_path not in files and file_path not in ignored_paths and file_path not in deleted_paths:
            # File is deleted, stage it for deletion
            with index_file.open("a") as index:
                index.write(f"DELETED {path}\n")
                staged_files.add("DELETED")

    if not staged_files:
        click.echo("No changes found to stage.")
    else:
        click.echo("Staged changes successfully.")

# Stage all changed files to index 
def add():
    # Read the ignore list from .subsysignore file
    ignore_list = read_ignore_file()

    # Add all files in the working directory and subdirectories
    root_dir = Path(".")
    files = list_all_files(root_dir, ignore_list)

    # Get unchanged files
    unchanged_files = get_unchanged_files([Path(file) for file in files], ignore_list)

    # Stage changes by adding files to the index, ignoring unchanged files
    stage_changes([file for file in files if file not in unchanged_files], ignore_list)

import datetime
import gzip
from pathlib import Path
import click

from utils.misc import generate_id, read_slug_file, save_slug


# Function to save staged files to a snapshot
def snap_changes(slug):
    index_file = Path(".subsys") / "index"
    
    with index_file.open() as index:
        index_content = index.read()

    if not index_content.strip():
        click.echo("Skipping snap command.")
        return

    head_file = Path(".subsys") / "HEAD"
    main_branch_file = Path(".subsys") / head_file.read_text().strip()
    prev_snap_id = main_branch_file.read_text().strip()

    snap_id = generate_id(index_content.encode())
    snap_timestamp = datetime.datetime.now().isoformat()

    # Create the snap object
    snap_content = f"snap {snap_id}\n"
    if prev_snap_id:
        snap_content += f"Parent: {prev_snap_id}\n"  # Include the previous snap ID
    snap_content += f"Date: {snap_timestamp}\n"
    snap_content += f"Slug: {slug}\n"  # Include the slug

    # Read the existing index content and store the files that are already staged
    with index_file.open() as index:
        for line in index:
            file_hash, file_path = line.strip().split(" ", 1)
            snap_content += f"{file_hash} {file_path}\n"

    # Save the snap object to the objects directory
    snap_object = Path(".subsys") / "objects" / f"sn_{snap_id}"
    snap_object.write_text(snap_content)

    # Compress the contents of the files and save them to the objects directory
    for line in index_content.strip().split("\n"):
        file_hash, file_path = line.strip().split(" ", 1)

        if file_hash == "DELETED":
            continue
        
        file_path = Path(file_path)
        with file_path.open("rb") as file:
            compressed_content = gzip.compress(file.read())
            file_content_path = Path(".subsys") / "objects" / file_hash
            file_content_path.write_bytes(compressed_content)

    # Update the main branch reference to point to the new snap.
    main_branch_file.write_text(snap_id)

    # Clear the index file after snapping.
    index_file.write_text("")

    # Save the new slug to the SLUGS file
    save_slug(slug, snap_id)
    click.echo(f"Snapshot saved successfully.")

# Function to get the list of snaps to be submitted
def get_snaps(slug=None):
    snaps_to_submit = []
    objects_dir = Path(".subsys") / "objects"

    # List all files in the objects directory
    for snap_file in objects_dir.iterdir():
        if snap_file.name.startswith("sn_"):  # Update to handle snaps with the prefix "sn_"
            with snap_file.open() as snap:
                snap_hash = snap.readline().strip().split(" ")[1]

                # Check if the provided slug matches the snap's Slug, if provided
                if slug and not any(line.strip().startswith("Slug:") and line.strip().endswith(slug) for line in snap):
                    continue

                # Read the rest of the snap content to get file hashes and paths
                snap_content = snap.read()
                file_hashes_and_paths = [line.strip().split(" ", 1) for line in snap_content.splitlines()]

                snaps_to_submit.append((snap_hash, file_hashes_and_paths))

    return snaps_to_submit

# Function to show files from the previous snap, if any
def show_previous_snap_files():
    last_snap_files = get_last_snap_files()

    if not last_snap_files:
        click.echo("No previous snap found.")
        return

    click.echo("Files from the previous snap:")
    for snap_hash, file_path in last_snap_files:
        click.echo(f"{snap_hash} {file_path}")

# Function to get file hashes and paths from the last snap
def get_last_snap_files():
    head_file = Path(".subsys") / "HEAD"
    main_branch_file = Path(".subsys") / head_file.read_text().strip()

    if not main_branch_file.exists() or not main_branch_file.read_text():
        return []

    snap_id = main_branch_file.read_text().strip()
    snap_object = Path(".subsys") / "objects" / f"sn_{snap_id}" 

    if not snap_object.exists():
        return []

    with snap_object.open() as snap_file:
        snap_content = snap_file.read()

    snap_lines = snap_content.strip().split("\n")

    last_snap_files = []

    # Iterate through the snap_lines to extract the file hashes and paths
    for line in snap_lines:
        if line.startswith("snap") or line.startswith("Date:") or line.startswith("Slug:"):
            continue
        else:
            file_hash, file_path = line.split(" ", 1)
            last_snap_files.append((file_hash, file_path.strip()))

    return last_snap_files

# Function to get the content of files from a snap, excluding large files
def get_snap_files_content(snap_id, exclude_large_files=True, max_file_size=1048576):
    snap_object = Path(".subsys") / "objects" / f"sn_{snap_id}"
    if not snap_object.exists():
        raise ValueError(f"Snap with ID '{snap_id}' does not exist.")

    with snap_object.open() as snap_file:
        snap_content = snap_file.read()

    lines = snap_content.splitlines()[1:]
    files_content = {}

    # Read the content of each file and store it in the dictionary
    for line in lines:
        if line.startswith("Parent:") or line.startswith("Date:") or line.startswith("Slug:"):
            continue

        file_hash, file_path = line.strip().split(" ", 1)

        if file_hash == "DELETED":
            continue

        file_path = Path(file_path)
        file_content_path = Path(".subsys") / "objects" / file_hash

        # Exclude large files if specified
        if exclude_large_files and file_content_path.stat().st_size > max_file_size:
            continue

        file_content = file_content_path.read_bytes()
        files_content[file_path] = file_content

    # Get the parent snap ID from the current snap content, if available
    parent_snap_id = None
    for line in lines:
        if line.startswith("Parent:"):
            parent_snap_id = line.split(":", 1)[1].strip()
            break

    if parent_snap_id:
        parent_files_content = get_snap_files_content(parent_snap_id)
        files_content.update(parent_files_content)

    return files_content

#Function to get all snaps from the objects folder
def get_all_snaps():
    objects_dir = Path(".subsys") / "objects"
    snap_files = []

    for snap_file in objects_dir.iterdir():
        if snap_file.name.startswith("sn_"):
            snap_files.append(snap_file)

    return snap_files

# Function to get specific snap_file
def get_snap_by_slug(slug):
    slugs = read_slug_file()

    snap_id = slugs.get(slug)
    if not snap_id:
        click.echo("Snapshot not found.")
        return None

    # Check if the snap file exists in the "objects" directory
    snap_file = Path(".subsys") / "objects" / f"sn_{snap_id}"
    if not snap_file.exists():
        return None

    return snap_file

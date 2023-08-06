import os
from pathlib import Path

import click


# Function to create a new "subsys" repository
def create_repository():
    # Create the necessary directory structure
    root_dir = Path(".subsys")
    root_dir.mkdir(parents=True, exist_ok=True)

    objects_dir = root_dir / "objects"
    objects_dir.mkdir(exist_ok=True)

    refs_dir = root_dir / "refs" / "heads"
    refs_dir.mkdir(parents=True, exist_ok=True)

    # Create the HEAD file and initialize it with the reference to the main branch
    head_file = root_dir / "HEAD"
    head_file.write_text("refs/heads/main")

    # Create the main branch file and initialize it with an empty snap
    main_branch_file = refs_dir / "main"
    main_branch_file.write_text("")

    # Set the hidden attribute for the .subsys folder on Windows
    if os.name == 'nt':
        try:
            os.system(f"attrib +h {str(root_dir)}")
        except Exception:
            pass

    click.echo("Initialized empty subsys repository.")
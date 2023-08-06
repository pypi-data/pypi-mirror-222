import click
import slugify

from utils.misc import is_initialized, read_unique_slugs
from utils.snap import snap_changes
from utils.stage import add


# Snap command to save sanpshots of the working directory
@click.command()
@click.option("--name", required=True, help="Unique slug to identify each snap.")
def snap(name):
    if not is_initialized():
        click.echo("Please initialize a repository.\nRun subsys init.")
        return
    # Validate the slug using slugify
    valid_slug = slugify.slugify(str(name))

    if name != valid_slug:
        click.echo("Error: Invalid slug provided. Please use only alphanumeric characters and hyphens.")
        return

    # Read the list of unique slugs
    unique_slugs = read_unique_slugs()

    if valid_slug in unique_slugs:
        click.echo("Error: Snapshot {name} already exists. Please enter a different name.")
        return
    
    # Stage all changes
    add()

    # Snap changes and create a new snap
    snap_changes(valid_slug)
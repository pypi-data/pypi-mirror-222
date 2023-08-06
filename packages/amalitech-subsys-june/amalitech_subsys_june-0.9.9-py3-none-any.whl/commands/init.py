from pathlib import Path
import click

from utils.repository import create_repository


# Initialize the "subsys" repository
@click.command()
def init():
    root_dir = Path(".subsys")
    if root_dir.exists():
        click.echo("Error: subsys repository already initialized.")
    else:
        create_repository()
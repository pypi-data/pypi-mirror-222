import click
from commands.init import init
from commands.config import config
from commands.snap import snap
from commands.submit import submit


@click.group()
def cli():
    pass


cli.add_command(init)
cli.add_command(config)
cli.add_command(snap)
cli.add_command(submit)

if __name__ == "__main__":
    cli()

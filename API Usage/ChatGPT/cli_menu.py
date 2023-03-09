import click

@click.group()
def cli():
    pass

@cli.command()
def option1():
    click.echo("Option 1 selected")

@cli.command()
def option2():
    click.echo("Option 2 selected")

if __name__ == '__main__':
    cli()
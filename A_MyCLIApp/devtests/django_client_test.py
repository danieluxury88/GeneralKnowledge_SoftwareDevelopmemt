import djclick as click

@click.command()
@click.argument('name')
def command(name):
    click.secho('Hello, {}'.format(name), fg='red')
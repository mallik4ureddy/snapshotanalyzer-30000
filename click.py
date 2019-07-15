import click

@click.command()
@click.option('--name', default=None, help="enter your name")
def prtnames():
    print("Hello World")

if __name__=='__main__':
    prtnames()

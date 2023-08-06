from typing import Optional

import typer
app = typer.Typer()

@app.command()
def platform(name: Optional[str]):
    print(f"Hello {name}")

@app.command("platform:start")
def platform_start():
    """ Start the Pliny platform services. """
    pass

@app.command("platform:stop")
def platform_stop():
    """ Stop the Pliny platform services. """
    pass

@app.command("platform:setup")
def platform_setup():
    """ Install and configure the Pliny run-time platform services."""
    pass

if __name__ == "__main__":
    app()


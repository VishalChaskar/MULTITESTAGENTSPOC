import typer
from main import run_test

app = typer.Typer()

@app.command()
def main(url: str = None):
    run_test(url)

if __name__ == "__main__":
    app()
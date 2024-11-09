from typer import Typer

from design_patterns.strategy.behaviors import FlyRocketPowered
from design_patterns.strategy.ducks import MallardDuck, RubberDuck, ModelDuck

app = Typer()

@app.command("mallard")
def run_mallard():
    mallard = MallardDuck()
    mallard.display()
    mallard.perform_quack()
    mallard.perform_fly()
    mallard.swim()

@app.command("rubber")
def run_rubber():
    rubber = RubberDuck()
    rubber.display()
    rubber.perform_quack()
    rubber.perform_fly()
    rubber.swim()

@app.command("model")
def run_model():
    model = ModelDuck()
    model.display()
    model.perform_quack()
    model.perform_fly()
    model.swim()

    # change the fly behavior dynamically to use a rocket
    model.fly_behavior = FlyRocketPowered()
    model.perform_fly()


if __name__ == "__main__":
    app()

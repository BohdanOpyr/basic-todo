import yaml
import click


class ToDo:
    def __init__(self, file="todo.yaml"):
        self.file = file
        self.load()

    def load(self):
        try:
            self.data = yaml.safe_load(open(self.file, "r"))
        except FileNotFoundError:
            self.data = []

    def save(self):
        yaml.dump(self.data, open(self.file, "w"))

    def append(self, description, name=None):
        self.load()
        if name is None:
            name = "Task %d" % (len(self.data) + 1)
        self.data.append({"name": name, "description": description})
        self.save()

    def __getitem__(self, i):
        self.load()
        return self.data[i]

    def __delitem__(self, i):
        self.load()
        del self.data[i]
        self.save()

    def __list__(self):
        self.load()
        return self.data

    def __setitem__(self, i, value):
        self.load()
        original = self.data[i]
        assert isinstance(value.get("description", None), str)
        if value.get("name", None) is None:
            value["name"] = original["name"]
        self.data[i] = value
        self.save()

    def clear(self):
        self.data = []
        self.save()

    def delete_item(self, idt):
        if isinstance(idt, int):
            del self[idt]
        elif isinstance(idt, str):
            self.load()
            for i, item in enumerate(self.data):
                if item["name"] == idt:
                    del self[i]
                    return
            click.echo("item not found")


@click.group()
@click.option("--file", default="todo.yaml", help="Todo list file path")
@click.pass_context
def main(ctx, file):
    """Simple todo list cli program"""
    ctx.ensure_object(dict)
    ctx.obj["file"] = file


@main.command()
@click.pass_context
def list(ctx):
    """list all todo items"""
    todo = ToDo(ctx.obj["file"])
    for i, item in enumerate(todo):
        click.echo(f'{i}: {item["name"]}:\t{item["description"]}')


@main.command()
@click.argument("description")
@click.option("--name", default=None, help="Todo item name")
@click.pass_context
def add(ctx, description, name):
    """add a todo item"""
    todo = ToDo(ctx.obj["file"])
    todo.append(description, name)


@main.command()
@click.argument("id")
@click.pass_context
def remove(ctx, id):
    """remove a todo item, by id (the first one has the id of 0) or by name"""
    todo = ToDo(ctx.obj["file"])
    try:
        id = int(id)
    except ValueError:
        pass
    todo.delete_item(id)


@main.command()
@click.argument("id", type=int)
@click.argument("description")
@click.option("--name", default=None, help="Todo item name")
@click.pass_context
def set(ctx, id, description, name):
    """modify an existing todo item"""
    todo = ToDo(ctx.obj["file"])
    data = {"description": description}
    if name is not None:
        data["name"] = name
    todo[id] = data


@main.command()
@click.pass_context
def clear(ctx):
    """delete all todo items"""
    todo = ToDo(ctx.obj["file"])
    todo.clear()


if __name__ == "__main__":
    main()

import pathlib
import sys

import jinja2
import pkg_resources


def render_template():
    package = __name__.split(".")[0]
    TEMPLATES_PATH = pathlib.Path(
        pkg_resources.resource_filename(package, "templates/")
    )
    path = TEMPLATES_PATH / "main.go.tmpl"

    with open(path, "r") as file:
        template_content = file.read()

    env = jinja2.Environment(loader=jinja2.BaseLoader())
    template = env.from_string(template_content)
    rendered_template = template.render()
    sys.stdout.write(rendered_template)


def main() -> int:
    render_template()
    return 0

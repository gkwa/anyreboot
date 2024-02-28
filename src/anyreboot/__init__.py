import pathlib
import sys

import jinja2
import pkg_resources


def load_template(template_name):
    package = __name__.split(".")[0]
    TEMPLATES_PATH = pathlib.Path(
        pkg_resources.resource_filename(package, "templates/")
    )
    path = TEMPLATES_PATH / template_name
    with open(path, "r") as file:
        return file.read()


def render_template(template_content):
    env = jinja2.Environment(loader=jinja2.BaseLoader())
    template = env.from_string(template_content)
    rendered_template = template.render()
    sys.stdout.write(rendered_template)


def main() -> int:
    template_content = load_template("mymain.tmpl")
    render_template(template_content)
    return 0

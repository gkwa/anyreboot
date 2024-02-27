import sys

import jinja2


def render_template():
    with open("main.txt", "r") as file:
        template_content = file.read()

    env = jinja2.Environment(loader=jinja2.BaseLoader())
    template = env.from_string(template_content)
    rendered_template = template.render()
    sys.stdout.write(rendered_template)


def main() -> int:
    render_template()
    return 0

"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class ColorState(pc.State):
    colors = ["black", "red", "green", "blue", "purple"]
    colors_hex = ["#333333", "#de362a", "#4bde2a", "#2a4bde", "#a82ade"]

    color_index = 0

    def nextColor(self):
        self.color_index += 1

    @pc.var
    def color(self):
        return self.colors[self.color_index % len(self.colors)]

    @pc.var
    def hex_color(self):
        return self.colors_hex[self.color_index % len(self.colors)]


def index():
    return pc.center(
        pc.vstack(
            pc.icon(tag="MoonIcon"),
            pc.button("test_button", font_size="1em",
                      on_click=ColorState.nextColor, color=ColorState.color),
            pc.heading("Welcome to Pynecone!", font_size="2em"),
            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%"
    )


style = {
    "background_color": ColorState.hex_color
}
# Add state and page to the app.
app = pc.App(state=ColorState, style=style)
app.add_page(index)
app.compile()

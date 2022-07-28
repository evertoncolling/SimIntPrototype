import dash_mantine_components as dmc
from dash import html, dcc, page_container
from dash_iconify import DashIconify


def create_header():
    return dmc.Header(
        [
            dmc.Container(
                [
                    dmc.Group(
                        [
                            # Logo/Page Name
                            dmc.Center(
                                [
                                    dcc.Link(
                                        [
                                            # Hide long text on small viewports
                                            dmc.MediaQuery(
                                                [
                                                    dmc.Group(
                                                        [
                                                            dmc.Image(
                                                                src="./assets/cognite_logo.svg",
                                                                width=32,
                                                            ),
                                                            dmc.Text(
                                                                "SimExplorer",
                                                                size="xl",
                                                                color="#fafafa",
                                                                weight=600,
                                                            ),
                                                        ],
                                                        spacing="xs",
                                                    )
                                                ],
                                                smallerThan="sm",
                                                styles={"display": "none"},
                                            ),
                                            # Hide short text on large viewports
                                            dmc.MediaQuery(
                                                [
                                                    dmc.Group(
                                                        [
                                                            dmc.Image(
                                                                src="./assets/cognite_logo.svg",
                                                                width=32,
                                                            ),
                                                            dmc.Text(
                                                                "",
                                                                size="xl",
                                                                color="gray",
                                                            ),
                                                        ]
                                                    )
                                                ],
                                                largerThan="sm",
                                                styles={"display": "none"},
                                            ),
                                        ],
                                        href="/",
                                        style={"textDecoration": "none"},
                                    ),
                                ]
                            ),
                            # Icons
                            dmc.Group(
                                [
                                    html.A(
                                        dmc.Tooltip(
                                            dmc.ThemeIcon(
                                                DashIconify(
                                                    icon="radix-icons:github-logo",
                                                    width=20,
                                                ),
                                                radius=28,
                                                size=32,
                                                variant="outline",
                                                color="gray",
                                            ),
                                            label="Source Code",
                                            position="bottom",
                                        ),
                                        href="https://github.com/evertoncolling/SimIntPrototype",
                                        target="_blank",
                                    )
                                ],
                                position="right",
                                align="center",
                                spacing="xl",
                            ),
                        ],
                        position="apart",
                        align="flex-start",
                    ),
                ],
                fluid=True,
            )
        ],
        height=56,
        fixed=True,
        p="sm",
    )


def create_appshell():
    return dmc.MantineProvider(
        [
            create_header(),
            # create_navbar(),
            html.Div(
                [
                    dmc.Container(page_container, pt=90, pl=5, pr=5),
                ],
                id="wrapper",
            ),
        ],
        theme={
            "fontFamily": "Inter, sans-serif",
            "breakpoints": {"xs": 0, "sm": 576, "md": 768, "lg": 992, "xl": 1200},
            "colorScheme": "dark",
        },
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )

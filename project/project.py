"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from reflex.components.component import NoSSRComponent

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass

class EconomicCalendar(NoSSRComponent):
    library = "react-ts-tradingview-widgets"
    tag = "EconomicCalendar"

    locale: rx.Var[str]

    height: rx.Var[str]

    width: rx.Var[str]

class MarketOverview(NoSSRComponent):
    library = "react-ts-tradingview-widgets"
    tag = "MarketOverview"



def index() -> rx.Component:
    return rx.hstack(
        rx.container(
        EconomicCalendar(
            height="500",
            width="400"
            # locale="en"
        )),
        rx.container(
        MarketOverview()
        )
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
# test

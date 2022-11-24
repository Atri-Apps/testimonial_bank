from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """

    at.Table1.custom.cols = [
    { "field": "id", "headerName": "Tag", "width": 100},
    { "field": "Quote", "headerName": "Quote", "width": 400},
    { "field": "Author", "headerName": "Author", "width": 200 },
    { "field": "Designation", "headerName": "Designation", "width": 300 },
    { "field": "Persona", "headerName": "Persona", "width": 300 },
    ]

    # add rows
    at.Table1.custom.rows = [
        { "id": "dev-time", 
        "Quote": "Cut development time from months to hours",
        "Author": "Johaness Vermeer", 
        "Designation": "Head of Art Restoration, Rijksmuseum",
        "Persona": "Web developer with 5+ YoE",
        },
        { "id": "cost", 
        "Quote": "Cut cost by 50%",
        "Author": "Rembrandt", 
        "Designation": "Head of Art Development, Rijksmuseum",
        "Persona": "Web developer with 10+ YoE",
        },
    ]


def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    pass
"""
File: landingPage.py
Author: Mihir Bhaskar

Desc: This file returns an HTML Div with the content of the landing or welcome page

Output: 
    - HTML Div with the main welcome page content. This is called directly in the app.py file
"""
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc


def makeLandingPage():

    return html.Div(className='landing', children=[
        html.H1('Welcome to AssetMappr!', style={
                'color': '#2C3E50'}, id="Welcome"),
        html.Br(),
        html.H4('''We are a group of students that believe in the power of community participation. 
                    We hope that our app will make it easier for you to share your thoughts about the assets in your community,
                    helping planners make better investments for the future.''', id="WelWords"),
        html.Br(),

        # Link to take users to the main home page of the app
        dbc.Button('Enter the APP',
                   href='/home', id="enterButton")
    ])

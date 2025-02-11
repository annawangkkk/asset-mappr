"""
File: readDB.py
Author: Mihir Bhaskar

Desc: This file interacts with the postgreSQL database to read in the initial datasets when we initialise the app session
    
TODOs:
    - Connect to SQL centrally once, instead of starting many different connections
    - Make the input dependent on community_geo_id
    
Inputs:
    - app: an initialized Dash app
    - community_geo_id (pending implementation)
   
Outputs: (see the database documentation for more info on these tables)
    - df: data frame of the main assets table
    - asset_categories: data frame of the asset-categories table
    - master_categories: a list of the unique master category values
    - master_value_tags: a list of the unique master value tags (for use in the ratings function)

"""
import dash
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

def readDB(app, community_geo_id=False):
    
    # con_string = 'postgresql://assetmappr_database_user:5uhs74LFYP5G2rsk6EGzPAptaStOb9T8@dpg-c9rifejru51klv494hag-a/assetmappr_database'
    
    # If running the app externally (e.g. outside render/locally), use this connection string instead:
    con_string = 'postgresql://assetmappr_database_user:5uhs74LFYP5G2rsk6EGzPAptaStOb9T8@dpg-c9rifejru51klv494hag-a.ohio-postgres.render.com/assetmappr_database'
    
    # Load the categories master list
    master_categories = pd.read_sql_table('categories_master', con=con_string)
    master_categories = master_categories.values.tolist()
    master_categories = [item for sublist in master_categories for item in sublist]
    
    # Load the values master list 
    master_value_tags = pd.read_sql_table('values_master', con=con_string)
    master_value_tags = master_value_tags.values.tolist()
    master_value_tags = [item for sublist in master_value_tags for item in sublist]
    
    # Load the main assets database
    df = pd.read_sql_table('assets', con=con_string)

    # Load the asset-categories mapping database
    asset_categories = pd.read_sql_table('asset_categories', con=con_string)
    
    return df, asset_categories, master_categories, master_value_tags

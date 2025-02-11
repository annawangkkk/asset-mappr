"""
File: suggestMissingAsset_db.py
Author: Mihir Bhaskar

Desc: Interacts with the database to write user-submitted missing asset suggestions to the missing assets table

TODOs:
    - Generalise community_geo_id
    - Standardise the database connection so I don't keep starting new connections

Input:
    - (str) User's IP address
    - (str) Name of the user submitting the suggestion
    - (str) Role of the user in the community
    - (str) Name of the missing asset 
    - (str) category associated with that missing asset
    - (str) Desc: description of the missing asset
    - (tuple) click_lat_lng: desired latitude and longitude of the missing asset
    - (int) community_geo_id: geo_id of the relevant community
   
Output: 
    - None: this function only writes to the SQL database directly
    
"""
import psycopg2
import uuid
from datetime import datetime

def suggestMissingAsset_db(ip, user_name, user_role, name, categories, desc, click_lat_lng, community_geo_id):

    # When deploying on Render, use this string
    # con_string = 'postgresql://assetmappr_database_user:5uhs74LFYP5G2rsk6EGzPAptaStOb9T8@dpg-c9rifejru51klv494hag-a/assetmappr_database'
    
    # If running the app externally (e.g. outside render/locally), use this connection string instead:
    con_string = 'postgresql://assetmappr_database_user:5uhs74LFYP5G2rsk6EGzPAptaStOb9T8@dpg-c9rifejru51klv494hag-a.ohio-postgres.render.com/assetmappr_database'

    # Establish connection with database (details found in Heroku dashboard after login)
    conn = psycopg2.connect(con_string)
    # Create cursor object
    cursor = conn.cursor()
    
    # Process the info into a suitable format for the staging asset table
    suggestion_id = str(uuid.uuid4()) 
    asset_name = name
    community_geo_id = community_geo_id
    primary_category = categories
    description = desc
    latitude = click_lat_lng[0]
    longitude = click_lat_lng[1]
    user_name = user_name
    user_role = user_role
    user_upload_ip = ip
    
    generated_timestamp = datetime.now()
    
    # Write the info into missing assets table
    # Refer to the createDBstructure.py script to see the variable types and DB structure
    cursor.execute('''INSERT INTO missing_assets (suggestion_id, missing_asset_name, primary_category, user_community, 
                               latitude, longitude, generated_timestamp, user_name, user_role, user_upload_ip, description)
                      VALUES ('{}','{}','{}', {},{},{},TIMESTAMP '{}', '{}', '{}', '{}', '{}');'''.format(suggestion_id, asset_name, 
                      primary_category,community_geo_id, latitude, longitude, generated_timestamp, user_name, 
                      user_role, user_upload_ip, description))
    
    conn.commit()
    conn.close()
    
    return None

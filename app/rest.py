import pymysql
from app import app
from db import mysql
from flask import Flask, jsonify, request
from shapely.geometry import Point, Polygon
from datetime import datetime, timedelta
import sys

# Endpoint to ingest a new trip
@app.route('/trips', methods=['POST'])
def ingest_trip():
    db = mysql.connect()
    data = request.json
    region = data['region']
    origin_coord = data['origin_coord']
    destination_coord = data['destination_coord']
    datetime = data['datetime']
    datasource = data['datasource']

    with db.cursor() as cursor:
        # Insert the new trip into the database
        sql = "INSERT INTO trips (region, origin_coord, destination_coord, datetime, datasource) VALUES (%s, ST_PointFromText(%s), ST_PointFromText(%s), %s, %s)"
        cursor.execute(sql, (region, origin_coord, destination_coord, datetime, datasource))
        db.commit()

    return jsonify({'message': 'Trip ingested successfully'}), 201

# Endpoint to call all  trips
@app.route('/')
def trips():
    db = mysql.connect()

    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM trips")
    
    rows = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description]
    
    # Convert results to JSON
    data = []
    for row in rows:
        
        data.append({
            'trip_id': row['trip_id'],
            'region': row['region'],
            #'origin_coord': row['origin_coord'],
            #'destination_coord': row['destination_coord'],
            'datetime': row['datetime'].strftime('%Y-%m-%d %H:%M:%S'),
            'datasource': row['datasource']
        })
@app.route('/weekly_average_trips', methods=['GET'])
def get_weekly_average_trips():
    db = mysql.connect()
    # Get parameters from request
    region = request.args.get('region')
    bbox = request.args.get('bbox')  # assume format is 'xmin,ymin,xmax,ymax'

    # Define SQL query to get weekly trip totals for the specified area
    if region:
        query = f"""
            SELECT WEEK(datetime) as week, COUNT(*) as num_trips
            FROM trips
            WHERE region = '{region}'
            GROUP BY week 
        """
        print(query, file=sys.stderr)
    elif bbox:
        xmin, ymin, xmax, ymax = bbox.split(',')
        query = f"""
        SELECT WEEK(datetime) AS week, COUNT(*) AS num_trips, AsText(origin_coord),AsText(origin_coord) FROM trips 
        WHERE Contains(GeomFromText('POLYGON(({xmin} {ymin}, {xmax} {ymin}, {xmax} {ymax}, {xmin} {ymax}, {xmin} {ymin}))'),origin_coord) 
        OR Contains(GeomFromText('POLYGON(({xmin} {ymin}, {xmax} {ymin}, {xmax} {ymax}, {xmin} {ymax}, {xmin} {ymin}))'), destination_coord)
        GROUP BY week
        """
        print(query, file=sys.stderr)
    else:
        return jsonify(error='Must provide either "region" or "bbox" parameter'), 400

    # Execute SQL query and get weekly trip totals
    with db.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()

    # Calculate weekly averages
    t_weekly_trips=0
    n_week=0
    for week,count in results:
        t_weekly_trips += count
        n_week += 1 

    weekly_average=t_weekly_trips/n_week


    # Return weekly averages as JSON response
    name='weekly_average in '+region
    return jsonify({name: weekly_average}), 200

    resp = jsonify(data)
    resp.status_code = 200

    return resp

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
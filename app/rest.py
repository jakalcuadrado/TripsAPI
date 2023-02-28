import pymysql
from app import app
from db import mysql
from flask import Flask, jsonify, request
from shapely.geometry import Point, Polygon
from datetime import datetime, timedelta

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
    

    resp = jsonify(data)
    resp.status_code = 200

    return resp

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
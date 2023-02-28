import pymysql
from app import app
from db import mysql
from flask import jsonify

@app.route('/')
def trips():
    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)
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
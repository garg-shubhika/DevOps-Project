from flask import Flask, request, jsonify, send_from_directory
import os
from flask_cors import CORS  # Import CORS
import psycopg2

app = Flask(__name__)
# Allow all the domains to make requests to the backend
CORS(app)

# Connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname='fleet_db', user='fleet_user', password='fleet_pwd', host='my_postgres_container'
    )
    return conn
@app.route('/')
def serve_index():
    # Serve the index.html file from the frontend folder
    return send_from_directory(os.path.join(os.getcwd(), 'frontend'), 'index.html')

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM vehicles;')
    vehicles = cur.fetchall()
    cur.close()
    conn.close()
    
    return jsonify(vehicles)

@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    data = request.get_json()
    id = data['id']
    name = data['name']
    location = data['location']
    status = data['status']
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO vehicles (id, name, location, status) VALUES (%s, %s, %s, %s);', (id, name, location, status))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Vehicle added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

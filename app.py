from flask import Flask, render_template, jsonify
from pymongo import MongoClient
import os
import time
from datetime import datetime

app = Flask(__name__)
start_time = time.time()

def get_mongodb_connection():
    """Get MongoDB connection with error handling"""
    try:
        mongodb_host = os.getenv('MONGODB_HOST', 'localhost')
        mongodb_port = int(os.getenv('MONGODB_PORT', 27017))
        mongodb_db = os.getenv('MONGODB_DB', 'visitor_counter')
        
        client = MongoClient(
            host=mongodb_host,
            port=mongodb_port,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=5000
        )
        
        # Test connection
        client.admin.command('ping')
        db = client[mongodb_db]
        return db
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        return None

@app.route('/')
def home():
    """Main application route with visitor counter"""
    try:
        db = get_mongodb_connection()
        
        if db is not None:
            # Increment visitor counter
            result = db.visitors.find_one_and_update(
                {'_id': 'counter'},
                {'$inc': {'count': 1}, '$set': {'last_visit': datetime.now()}},
                upsert=True,
                return_document=True
            )
            visitor_count = result['count']
            
            # Store visit record
            db.visits.insert_one({
                'timestamp': datetime.now(),
                'visitor_count': visitor_count
            })
            
            # Get recent visits count (last 100)
            recent_visits = db.visits.count_documents({})
            if recent_visits > 100:
                # Keep only last 100 visits
                oldest_visits = db.visits.find().sort('timestamp', 1).limit(recent_visits - 100)
                oldest_ids = [visit['_id'] for visit in oldest_visits]
                db.visits.delete_many({'_id': {'$in': oldest_ids}})
                recent_visits = 100
            
            mongodb_status = True
        else:
            visitor_count = 0
            recent_visits = 0
            mongodb_status = False
            
        return render_template('index.html', 
                             visitor_count=visitor_count,
                             recent_visits=recent_visits,
                             mongodb_status=mongodb_status)
    except Exception as e:
        return render_template('index.html', 
                             visitor_count=0,
                             recent_visits=0,
                             mongodb_status=False,
                             error=str(e))

@app.route('/health')
def health_check():
    """Health check endpoint for container monitoring"""
    try:
        db = get_mongodb_connection()
        mongodb_connected = db is not None
        
        health_data = {
            "status": "healthy" if mongodb_connected else "degraded",
            "timestamp": datetime.now().isoformat(),
            "mongodb_connected": mongodb_connected,
            "uptime_seconds": int(time.time() - start_time),
            "version": "1.0.0"
        }
        
        return jsonify(health_data), 200
        
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 503

@app.route('/metrics')
def metrics():
    """Application metrics endpoint"""
    try:
        db = get_mongodb_connection()
        
        if db is not None:
            # Get visitor counter
            counter_doc = db.visitors.find_one({'_id': 'counter'})
            total_visits = counter_doc['count'] if counter_doc else 0
            
            # Get recent visits count
            recent_visits = db.visits.count_documents({})
            
            # Get visits in last 5 minutes
            five_minutes_ago = datetime.now().timestamp() - 300
            recent_count = db.visits.count_documents({
                'timestamp': {'$gte': datetime.fromtimestamp(five_minutes_ago)}
            })
            
            metrics_data = {
                "total_visits": total_visits,
                "recent_visits": recent_visits,
                "visits_last_5min": recent_count,
                "mongodb_connected": True,
                "uptime_seconds": int(time.time() - start_time),
                "timestamp": datetime.now().isoformat()
            }
        else:
            metrics_data = {
                "total_visits": 0,
                "recent_visits": 0,
                "visits_last_5min": 0,
                "mongodb_connected": False,
                "uptime_seconds": int(time.time() - start_time),
                "timestamp": datetime.now().isoformat()
            }
            
        return jsonify(metrics_data)
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/reset', methods=['POST'])
def reset_counter():
    """Reset visitor counter"""
    try:
        db = get_mongodb_connection()
        
        if db is not None:
            # Reset counter
            db.visitors.delete_one({'_id': 'counter'})
            # Clear visits
            db.visits.delete_many({})
            
            return jsonify({
                "message": "Counter reset successfully",
                "timestamp": datetime.now().isoformat()
            })
        else:
            return jsonify({
                "error": "MongoDB not available",
                "timestamp": datetime.now().isoformat()
            }), 503
            
    except Exception as e:
        return jsonify({
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    print(f"Starting Flask application on port {port}")
    print(f"Debug mode: {debug}")
    print(f"MongoDB host: {os.getenv('MONGODB_HOST', 'localhost')}")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
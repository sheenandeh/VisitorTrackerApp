# Project 1: Docker Containerization Basics

## Application Overview

This project demonstrates containerization fundamentals using a Flask Visitor Counter Web Application. The app tracks website visitors using MongoDB for data persistence and provides real-time metrics through a modern web interface.

### App Functionality
- Visitor Counter: Automatically increments each time someone visits the homepage
- Real-time Metrics: Displays total visits, recent activity, and system health status
- Interactive Dashboard: Modern Bootstrap interface with status indicators and action buttons
- API Endpoints: RESTful endpoints for health checks, metrics, and counter management
- Data Persistence: MongoDB stores visitor data that survives container restarts

## Quick Start Guide

### Step 1: Prerequisites
# Verify Docker installation
```sh
docker --version
docker-compose --version
```
# Navigate to project directory
```sh
cd project-1-docker-basics
```
### Step 2: Environment Setup
# Copy environment template
```sh
cp .env.example .env
```
# Edit environment variables if needed
```sh
nano .env
```
### Step 3: Build and Start Application
# Build all containers
```sh
docker-compose build
```
# Start application stack
```sh
docker-compose up -d
```
# Verify containers are running
```sh
docker-compose ps
```
### Step 4: Access the Application

Primary Interface:
- Web App: http://localhost:5000
- Dashboard: Interactive visitor counter with real-time updates

API Endpoints:
- Health Check: http://localhost:5000/health
- Metrics: http://localhost:5000/metrics
- Reset Counter: curl -X POST http://localhost:5000/reset

### Step 5: Test Application Functions

# Test main application
```sh
curl http://localhost:5000
```
# Check health status
```sh
curl http://localhost:5000/health

# View metrics data
```sh
curl http://localhost:5000/metrics
```
# Reset visitor counter
```sh
curl -X POST http://localhost:5000/reset
```
### Step 6: Monitor Application

# View application logs
```sh
docker-compose logs -f app
```
# Monitor MongoDB
```sh
docker-compose logs -f mongodb
```
# Check resource usage
```sh
docker stats
```
## Container Management

# Stop all containers
```sh
docker-compose stop
```
# Start stopped containers
```sh
docker-compose start
```
# Restart all services
```sh
docker-compose restart
```
# Stop and remove everything
```sh
docker-compose down -v
```
# View resource usage
```sh
docker stats
```
# Access container shell
```sh
docker-compose exec app /bin/bash
```
## Database Management

# Access MongoDB shell
```sh
docker-compose exec mongodb mongosh
```
# View visitor data
```sh
docker-compose exec mongodb mongosh --eval "db.visitors.find().pretty()"
```
# Check database status
```sh
docker-compose exec mongodb mongosh --eval "db.stats()"
```
# Backup database
```sh
docker-compose exec mongodb mongodump --out /data/backup

# View MongoDB logs
```sh
docker-compose logs mongodb
```
## Troubleshooting

# Rebuild containers without cache
```sh
docker-compose build --no-cache
```
# View detailed container information
```sh
docker-compose ps -a
```
# Check container health
docker-compose exec app curl http://localhost:5000/health

# Reset environment completely
```sh
docker-compose down -v
docker system prune -a
```
## Project Structure
```sh
project-1-docker-basics/
├── app.py                      # Flask application with MongoDB integration
├── requirements.txt            # Python dependencies (Flask, PyMongo)
├── Dockerfile                  # Development container configuration
├── Dockerfile.prod             # Production container with optimizations
├── docker-compose.yml          # Development stack with MongoDB
├── docker-compose.prod.yml     # Production deployment configuration
├── .dockerignore               # Docker build context exclusions
├── .env.example                # Environment variables template
├── templates/
│   └── index.html              # Bootstrap web interface
└── requirements.md             # Complete student assignment guide
```
## Expected Behavior

When working correctly, you should see:

1. Homepage Visit: Counter increases each time you visit http://localhost:5000
2. Dashboard Updates: Real-time status indicators show MongoDB connection
3. API Responses: All endpoints return proper JSON data
4. Data Persistence: Counter value survives container restarts
5. Health Status: Green indicators show system is healthy

## Success Verification

✅ Application Running: http://localhost:5000 displays visitor counter  
✅ Database Connected: MongoDB status shows "connected" in dashboard  
✅ Counter Working: Number increases with each page refresh  
✅ API Functional: All endpoints return valid JSON responses  
✅ Data Persists: Counter survives docker-compose restart  
✅ Health Checks: /health endpoint reports "healthy" status  

## Next Steps
- Add monitoring with Prometheus
- Implement CI/CD pipeline
- Configure reverse proxy
- Scale with orchestration

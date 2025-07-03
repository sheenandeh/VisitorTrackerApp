# Project 1: Docker Containerization Challenge
## Nebulance Systems BootCamp DevOps Class2025A

## PROJECT TIMELINE: 
* 4 DAYS  Submit a github repo by Monday 7th
* A screenshot of the application.
* Present App on Tuesday

## PROJECT OVERVIEW

As a DevOps engineer, you are provided with a Flask visitor counter web application that requires containerization and deployment. Your task is to analyze the application architecture, understand the dependencies, and successfully deploy the multi-service application using Docker and Docker Compose.

**No step-by-step instructions are provided. This tests your ability to understand application requirements and implement proper containerization strategies.**

## Application Functionality

### Core Features Required

**1. Visitor Counter System**
- Automatically increment counter each time homepage is accessed
- Display current visitor count prominently on main page
- Store all visitor data persistently in MongoDB database
- Counter must survive container restarts and rebuilds

**2. Interactive Web Dashboard**
- Modern, responsive Bootstrap-based user interface
- Real-time status indicators for database connectivity
- Interactive buttons for testing API endpoints
- Display visitor metrics and system health information

**3. RESTful API Endpoints**
- `GET /` - Main dashboard with visitor counter
- `GET /health` - Health check endpoint returning JSON status
- `GET /metrics` - Application metrics including visit statistics
- `POST /reset` - Reset visitor counter (for testing purposes)

**4. Database Integration**
- MongoDB for persistent data storage
- Two collections: `visitors` (counter) and `visits` (visit logs)
- Automatic database initialization and connection handling
- Graceful degradation when database is unavailable

## Technical Requirements

### Container Architecture
- **Flask Application**: Python web server with PyMongo dependencies
- **MongoDB Database**: NoSQL database for visitor data persistence
- **Docker Compose**: Multi-container orchestration
- **Volume Management**: Persistent storage for database data
- **Port Configuration**: Application accessible on port 5050

### Key Technologies
- **Flask**: Python web framework serving the application
- **MongoDB**: Document database storing visitor counts and visit logs
- **PyMongo**: Python MongoDB driver for database operations
- **Bootstrap**: Frontend UI framework for responsive design
- **Docker**: Containerization platform
- **Docker Compose**: Multi-container deployment tool

## DevOps Engineering Challenges

### Architecture Analysis Required
- Examine the Flask application (`app.py`) to understand MongoDB integration
- Review the HTML template to understand the user interface requirements
- Identify required Python dependencies from the application code
- Understand the database collections: `visitors` (counter) and `visits` (logs)

### Docker Implementation Tasks
- Create appropriate `Dockerfile` for the Flask application
- Configure `docker-compose.yml` for multi-service deployment
- Set up environment variables for database connectivity
- Implement named volumes for MongoDB data persistence
- Configure proper networking between Flask and MongoDB containers

### Deployment Verification
Your deployment must demonstrate:
- Application accessible at `http://localhost:5050`
- Visitor counter increments with each page visit
- MongoDB connection status displays correctly
- API endpoints (`/health`, `/metrics`, `/reset`) function properly
- Data persists across container restarts
- Recent activity tracking works correctly

### Testing Requirements
Your deployment must successfully handle:
- Visitor counter increments correctly on page refresh
- MongoDB connection status shows "Connected" when database is running
- Counter value persists after `docker-compose restart`
- API endpoints return proper JSON responses
- Reset functionality clears counter and refreshes page
- System shows "Degraded" status when MongoDB is unavailable

## Deliverables

### Required Files
- `Dockerfile` - Container configuration for Flask application
- `docker-compose.yml` - Multi-service orchestration configuration
- `.env` file - Environment variables for database connection
- Working application accessible at `http://localhost:5050`

### Demonstration Requirements
- Application loads successfully in web browser
- Visitor counter functionality works correctly
- Database connectivity indicators function properly
- API endpoints accessible and returning valid responses
- Data persistence verified through container restart testing

## Evaluation Criteria

### Docker Containerization (40%)
- Proper Dockerfile creation for Flask application
- Correct docker-compose.yml configuration
- Successful multi-container deployment
- Application accessible on specified port (5050)

### Database Integration (30%)
- MongoDB container properly configured
- Persistent volume implementation for data storage
- Database connectivity working correctly
- Data persistence across container restarts

### Application Functionality (20%)
- Visitor counter incrementing correctly
- All API endpoints responding properly
- UI displaying correct status information
- Error handling when database unavailable

### DevOps Best Practices (10%)
- Environment variable configuration
- Container networking setup
- Proper service dependencies
- Clean container shutdown and startup
- Create a clean readme.md demostration how the application functions and how to deploy and access the application

## Success Criteria

Your deployment is successful when:
- `docker-compose up -d` starts all services without errors
- Application loads at `http://localhost:5050`
- Visitor counter increments with each page visit
- MongoDB status shows "Connected" in the dashboard
- Counter value persists after `docker-compose restart`
- All API endpoints return valid JSON responses

## Key Learning Objectives

This challenge tests your ability to:
- Analyze Flask application architecture and dependencies
- Create proper Docker containers for Python web applications
- Configure multi-service deployments with Docker Compose
- Implement persistent data storage with named volumes
- Set up container networking and service communication
- Apply containerization best practices for development environments

## Getting Started Hints

1. **Examine the Application**: Start by reviewing `app.py` to understand the Flask application structure and MongoDB requirements
2. **Check Dependencies**: Look at the imports to identify required Python packages
3. **Environment Variables**: The app expects MongoDB connection details via environment variables
4. **Port Configuration**: The application runs on port 5000 internally but should be accessible on port 5050
5. **Database Requirements**: MongoDB needs persistent storage and proper initialization

**Remember**: The use of AI is highly recommended

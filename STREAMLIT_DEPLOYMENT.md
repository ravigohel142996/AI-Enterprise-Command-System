# Streamlit Deployment Guide

## Quick Start

This application has been optimized for fast startup on Streamlit Cloud.

### Key Features

✅ **Fast Startup** - App boots in under 10 seconds
✅ **SQLite Database** - Embedded database, no external server needed
✅ **Lazy-loaded Database Connections** - No blocking at import time
✅ **Proper Error Handling** - Graceful degradation if services unavailable
✅ **Request Timeouts** - All API calls have 10-second timeout
✅ **Health Monitoring** - Built-in health check and logging
✅ **Production Ready** - Optimized for Streamlit Cloud deployment

### Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run frontend/app.py

# Or use the startup script
./start_streamlit.sh
```

### Deployment to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Select your repository
4. Set main file path: `frontend/app.py`
5. Deploy!

The app will start quickly without hanging on "Loading..."

### Configuration

The app uses `.streamlit/config.toml` for optimal performance:
- Headless mode enabled
- CORS enabled for cross-origin requests
- XSRF protection enabled for security
- Optimal upload limits
- Error details enabled for debugging

### Troubleshooting

If the app is slow to start:
1. Check the logs for any warnings
2. Ensure no external services are blocking
3. Verify database connections are optional
4. Check API timeout settings

### Environment Variables

Optional - only needed if using backend API:
- `API_BASE_URL` - Backend API URL (default: http://localhost:8000/api/v1)

### Health Check

Look for "✅ App Loaded Successfully" in the sidebar after startup.

### Logging

The app logs startup progress to console:
- Import progress
- Configuration setup
- Database connection status (non-blocking)
- API availability

All logs are INFO level for production monitoring.

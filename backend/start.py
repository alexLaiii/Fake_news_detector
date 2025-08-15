import os
import uvicorn
from app import app

if __name__ == "__main__":
    # Get port from environment variable or default to 8000
    port = int(os.getenv("PORT", 8000))
    
    # Run the app
    uvicorn.run(
        "app:app",
        host="0.0.0.0",  # Bind to all interfaces
        port=port,
        reload=False,  # Disable reload in production
        log_level="info"
    ) 
#!/usr/bin/env python3
"""
Simple runner script for the Azure Reimbursement Application
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Starting Azure Reimbursement Application...")
    print(f"📁 Project root: {project_root}")
    print(f"🐍 Python path: {sys.path[0]}")
    
    # Set environment variables
    os.environ.setdefault("PYTHONPATH", str(project_root))
    
    # Run the application
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )
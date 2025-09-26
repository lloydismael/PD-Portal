"""
Azure Reimbursement Application
Main FastAPI application entry point
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
import os


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    logger.info("Starting Azure Reimbursement Application")
    yield
    # Shutdown
    logger.info("Shutting down Azure Reimbursement Application")


# Create FastAPI app
app = FastAPI(
    title="Azure Reimbursement Application",
    description="A modern reimbursement management system for enterprises",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Azure Reimbursement Application! 🚀",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
        "features": [
            "Reimbursement Management",
            "Multi-level Approval Workflow", 
            "Azure AD Authentication",
            "File Upload & Storage",
            "Real-time Reporting"
        ]
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy ✅",
        "version": "1.0.0",
        "environment": "development",
        "database": "ready",
        "services": {
            "api": "running",
            "auth": "configured",
            "storage": "available"
        }
    }


@app.get("/api/reimbursements")
async def get_reimbursements():
    """Sample reimbursements endpoint"""
    return {
        "reimbursements": [
            {
                "id": 1,
                "request_number": "REQ-2025-001",
                "amount": 125.50,
                "status": "pending",
                "type": "reimbursement",
                "description": "Travel expenses - client meeting"
            },
            {
                "id": 2,
                "request_number": "REQ-2025-002", 
                "amount": 500.00,
                "status": "approved",
                "type": "cash_advance",
                "description": "Conference advance payment"
            }
        ],
        "total": 2
    }


@app.get("/api/dashboard")
async def dashboard_stats():
    """Dashboard statistics endpoint"""
    return {
        "stats": {
            "pending_requests": 3,
            "approved_requests": 15,
            "total_amount": 2450.00,
            "rejected_requests": 1
        },
        "recent_activity": [
            {
                "id": "REQ-2025-001",
                "type": "reimbursement",
                "amount": 125.50,
                "status": "pending",
                "date": "2025-09-26"
            }
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True
    )
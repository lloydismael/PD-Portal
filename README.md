# Azure Reimbursement Application 💼

A modern, containerized Python web application for managing company reimbursements, cash advances, and liquidations, designed for deployment on Microsoft Azure.

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Azure](https://img.shields.io/badge/azure-0078d4.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/)
[![Docker](https://img.shields.io/badge/docker-0db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

## 🚀 Features

### Core Functionality
- **Multi-type Forms**: Reimbursement, Cash Advance, Liquidation requests
- **Workflow Management**: Employee → Project Manager → Finance approval chain
- **File Management**: Secure upload/download with malware scanning
- **Role-based Access**: Employee, Project Manager, Finance/Admin roles
- **Audit Trail**: Complete history tracking for compliance

### User Experience
- Modern Azure blue theme with glass effects
- Responsive design (desktop + mobile)
- Real-time status updates
- Email/Teams notifications
- Inline form validation

### Enterprise Features
- Auto-scaling via Azure App Service
- Encryption in transit and at rest
- Comprehensive logging and monitoring
- Power BI integration for reporting
- Multi-tenant support

## 🏗️ Architecture

- **Backend**: Python FastAPI with async support
- **Database**: Azure SQL Database with SQLAlchemy ORM
- **Storage**: Azure Blob Storage for file attachments
- **Authentication**: Azure Active Directory (OAuth 2.0)
- **Hosting**: Azure App Service with Docker containers
- **CI/CD**: GitHub Actions
- **Monitoring**: Azure Application Insights
- **Frontend**: Modern responsive UI with Azure design system

## 📋 Prerequisites

- Python 3.9+
- Docker Desktop
- Azure CLI
- VS Code (recommended)
- Git

## 🛠️ Local Development Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd azure-reimbursement-app
```

### 2. Set Up Python Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements-dev.txt
```

### 3. Configure Environment
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your Azure credentials
# (See Configuration section below)
```

### 4. Run the Application
```bash
# Option 1: Using the runner script
python run.py

# Option 2: Using uvicorn directly
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# Option 3: Using VS Code (F5 or Ctrl+F5)
```

### 5. Access the Application
- **Application**: http://127.0.0.1:8000
- **API Documentation**: http://127.0.0.1:8000/docs
- **Health Check**: http://127.0.0.1:8000/health

## ⚙️ Configuration

Create a `.env` file from `.env.example` and configure the following:

### Azure Services
```env
# Azure Active Directory
AZURE_AD_TENANT_ID=your-tenant-id
AZURE_AD_CLIENT_ID=your-client-id
AZURE_AD_CLIENT_SECRET=your-client-secret

# Azure SQL Database
AZURE_SQL_SERVER=your-server.database.windows.net
AZURE_SQL_DATABASE=reimbursement-db
AZURE_SQL_USERNAME=your-username
AZURE_SQL_PASSWORD=your-password

# Azure Blob Storage
AZURE_STORAGE_ACCOUNT=yourstorageaccount
AZURE_STORAGE_KEY=your-storage-key

# Azure Application Insights
AZURE_INSIGHTS_KEY=your-insights-key
```

### Email & Notifications
```env
# SMTP Configuration
SMTP_SERVER=smtp.office365.com
SMTP_USERNAME=your-email@company.com
SMTP_PASSWORD=your-password

# Microsoft Teams
TEAMS_WEBHOOK_URL=your-teams-webhook-url
```

## 🐳 Docker Development

### Using Docker Compose
```bash
# Development environment
docker-compose -f docker/docker-compose.yml up --build

# Production environment
docker-compose -f docker/docker-compose.prod.yml up --build
```

### Building Docker Image
```bash
# Build the image
docker build -f docker/Dockerfile -t azure-reimbursement-app .

# Run the container
docker run -p 8000:8000 --env-file .env azure-reimbursement-app
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_auth.py

# Run with verbose output
pytest -v
```

## 🎨 Code Quality

```bash
# Format code
black app/ tests/

# Sort imports
isort app/ tests/

# Lint code
flake8 app/

# Type checking
mypy app/
```

## 🚢 Deployment

### Azure App Service

1. **Set up Azure resources** using the ARM templates in `/azure`
2. **Configure GitHub Actions** with your Azure credentials
3. **Push to main branch** to trigger deployment

```bash
# Deploy using Azure CLI
az webapp deploy --resource-group myResourceGroup --name myWebApp --src-path .
```

### Environment Variables (Production)
Set the following in Azure App Service Configuration:

- `ENVIRONMENT=production`
- `DEBUG=false`
- All Azure service configurations from `.env.example`

## 📊 Monitoring

- **Application Insights**: Real-time performance monitoring
- **Health Checks**: `/health` endpoint for load balancer checks
- **Logging**: Structured logging with correlation IDs
- **Metrics**: Custom metrics for business KPIs

## 🔐 Security

- **Authentication**: Azure AD OAuth 2.0
- **Authorization**: Role-based access control (RBAC)
- **Data Encryption**: At rest and in transit
- **Input Validation**: Comprehensive validation and sanitization
- **Security Headers**: CORS, CSRF protection
- **File Upload**: Malware scanning and type validation

## 📚 API Documentation

The API is fully documented using OpenAPI/Swagger. Access the interactive documentation at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key Endpoints
- `GET /` - Application information
- `GET /health` - Health check
- `GET /api/reimbursements` - List reimbursements
- `GET /api/dashboard` - Dashboard statistics
- `POST /api/auth/login` - User authentication
- `POST /api/files/upload` - File upload

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Write comprehensive tests
- Update documentation
- Use type hints
- Follow the existing code structure

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: Create an issue in the repository
- **Documentation**: Check the `/docs` folder
- **Email**: Contact the development team

## 🎯 Roadmap

- [ ] Mobile app (React Native)
- [ ] Advanced reporting with Power BI
- [ ] Integration with accounting systems
- [ ] Multi-currency support
- [ ] Advanced workflow automation
- [ ] AI-powered expense categorization

## 🙏 Acknowledgments

- **FastAPI**: Modern, fast web framework
- **Microsoft Azure**: Cloud platform and services
- **SQLAlchemy**: Python SQL toolkit
- **Bootstrap**: Frontend framework
- **VS Code**: Development environment

---

**Built with ❤️ for efficient expense management on Microsoft Azure**

## 📈 Project Stats

- **Language**: Python 3.9+
- **Framework**: FastAPI
- **Database**: SQLAlchemy + Azure SQL
- **Cloud**: Microsoft Azure
- **CI/CD**: GitHub Actions
- **Testing**: pytest
- **Code Quality**: black, flake8, mypy
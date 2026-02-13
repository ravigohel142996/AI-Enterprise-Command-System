# 🏢 AI Enterprise Operating System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B%20%7C%203.13-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

## 🎉 Streamlit Cloud Ready!

**The app now starts in under 10 seconds on Streamlit Cloud!**

✅ Fixed all blocking startup issues
✅ Fast startup (1 second locally, <10s on cloud)
✅ Graceful degradation if services unavailable
✅ Production-ready deployment

See [DEPLOYMENT_FIX_SUMMARY.md](DEPLOYMENT_FIX_SUMMARY.md) for details.

## ⚠️ Security & Compatibility Updates

**All dependencies have been updated to secure versions** to address recent CVEs:
- ✅ FastAPI 0.109.0 → 0.109.1 (ReDoS fix)
- ✅ LightGBM 4.3.0 → 4.6.0 (RCE fix)
- ✅ NLTK 3.8.1 → 3.9 (Deserialization fix)
- ✅ python-multipart 0.0.6 → 0.0.22 (Multiple fixes)
- ✅ PyTorch 2.1.2 → 2.6.0 (RCE & buffer overflow fixes)
- ✅ Transformers 4.37.0 → 4.48.0 (Deserialization fixes)
- ✅ **Database: Migrated from PostgreSQL to SQLite** (Streamlit Cloud compatibility & faster startup)

See [SECURITY.md](SECURITY.md) for details.

## 🚀 AI-Powered Enterprise Operating System

A production-ready, enterprise-scale AI operating system that manages all major company departments using artificial intelligence and machine learning. Built for companies like Google, OpenAI, and Amazon.

### ✨ Key Features

- **12 AI-Powered Departments**: HR, Finance, Customer Support, Marketing, Sales, Cybersecurity, and more
- **Microservice Architecture**: Scalable, modular, and cloud-ready
- **Real-time AI/ML**: Resume screening, fraud detection, churn prediction, sentiment analysis
- **Production-Grade Security**: JWT authentication, RBAC, encryption
- **Interactive Dashboards**: Real-time metrics and insights
- **Docker & Kubernetes**: Cloud-native deployment
- **REST API**: Comprehensive API with auto-generated documentation

## 🎯 Departments & AI Capabilities

### 1. 👥 Human Resources
- AI Resume Screening
- Employee Retention Prediction
- Performance Analytics
- Hiring Automation

### 2. 💰 Finance & Accounting
- Fraud Detection (ML)
- Revenue Forecasting
- Expense Classification
- Budget Optimization

### 3. 💬 Customer Support
- AI Chatbot (NLP)
- Ticket Classification
- Sentiment Analysis
- SLA Monitoring

### 4. 📈 Marketing & Growth
- Lead Scoring
- Campaign Optimization
- SEO Prediction
- Conversion Modeling

### 5. 🤝 Sales & CRM
- Churn Prediction
- Customer Lifetime Value
- Deal Forecasting
- CRM Automation

### 6. 🔒 Cybersecurity & Risk
- Intrusion Detection
- Anomaly Detection
- Compliance Monitoring
- Threat Intelligence

### 7. 📊 Data & Analytics
- BI Dashboards
- KPI Tracking
- Predictive Analytics

### 8-12. Additional Departments
- Operations & Automation
- AI/ML Research
- Cloud Infrastructure
- Legal & Compliance
- Strategy & Leadership

## 🚀 Quick Start

### Using Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/ravigohel142996/AI-Enterprise-Command-System.git
cd AI-Enterprise-Command-System

# Copy environment file
cp .env.example .env

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f
```

**Access:**
- 🌐 API: http://localhost:8000
- 📚 API Docs: http://localhost:8000/docs
- 📊 Dashboard: http://localhost:8501

### Local Development

**Requirements:**
- Python 3.11+ (Python 3.13 fully supported)
- SQLite (built-in with Python)

```bash
# Install dependencies
pip install -r requirements.txt

# Initialize database
python backend/init_db.py

# Start backend
cd backend
uvicorn main:app --reload --port 8000

# Start frontend (new terminal)
streamlit run frontend/app.py
```

### Streamlit Cloud Deployment

**Quick Deploy to Streamlit Cloud:**

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Select this repository
4. Set main file: `frontend/app.py`
5. Click "Deploy"!

The app will start in under 10 seconds. See [STREAMLIT_DEPLOYMENT.md](STREAMLIT_DEPLOYMENT.md) for details.

**Test locally first:**
```bash
./start_streamlit.sh
# App should start in under 10 seconds
```


**Note:** The application now uses SQLite for maximum compatibility with Streamlit Cloud and faster startup times. SQLite is built into Python and requires no external database server.

## 📁 Project Structure

```
AI-Enterprise-Command-System/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/         # API endpoints
│   │   ├── core/        # Configuration & security
│   │   ├── db/          # Database connections
│   │   ├── models/      # SQLAlchemy models
│   │   ├── schemas/     # Pydantic schemas
│   │   ├── services/    # Business logic (12 departments)
│   │   └── ml/          # ML utilities & models
│   └── main.py          # Application entry point
├── frontend/            # Streamlit dashboard
│   └── app.py
├── deployment/          # Docker & Kubernetes
│   ├── docker/
│   └── kubernetes/
├── docs/               # Documentation
├── data/               # Sample datasets
├── models/             # ML model storage
└── docker-compose.yml
```

## 🛠️ Technology Stack

### Backend
- **FastAPI** - High-performance API framework
- **SQLite** - Lightweight embedded database (production-ready, Streamlit Cloud compatible)
- **SQLAlchemy** - ORM

### Machine Learning
- **scikit-learn** - Traditional ML
- **XGBoost** - Gradient boosting
- **PyTorch** - Deep learning
- **Transformers** - NLP models

### Frontend
- **Streamlit** - Interactive dashboards
- **Plotly** - Visualizations

### DevOps
- **Docker** - Containerization
- **Kubernetes** - Orchestration
- **GitHub Actions** - CI/CD

## 📖 Documentation

- [Full Documentation](docs/README.md)
- [Database Schema](docs/DATABASE_SCHEMA.md)
- [API Documentation](http://localhost:8000/docs) (when running)

## 🔒 Security

- JWT-based authentication
- Role-based access control (RBAC)
- Password hashing (bcrypt)
- SQL injection prevention
- CORS protection
- Encrypted data at rest

## 🧪 API Examples

### Authenticate
```bash
POST /api/v1/auth/login
```

### Screen Resume (HR)
```bash
POST /api/v1/hr/resume/screen
```

### Detect Fraud (Finance)
```bash
POST /api/v1/finance/transaction/analyze
```

### Score Lead (Marketing)
```bash
POST /api/v1/marketing/lead/score
```

### Predict Churn (Sales)
```bash
POST /api/v1/sales/customer/health
```

## 🌐 Cloud Deployment

### AWS
- ECS/EKS for containers
- RDS for PostgreSQL
- DocumentDB for MongoDB
- ElastiCache for Redis

### GCP
- GKE for Kubernetes
- Cloud SQL
- Cloud Memorystore

### Azure
- AKS for Kubernetes
- Azure Database
- Azure Cache

## 📈 Roadmap

- [ ] Advanced NLP (GPT integration)
- [ ] Real-time notifications
- [ ] Mobile app
- [ ] Multi-tenant support
- [ ] Advanced analytics
- [ ] Integration marketplace

## 🤝 Contributing

Contributions welcome! Please read our contributing guidelines.

## 📝 License

MIT License - see LICENSE file

## 👥 Support

- 📧 Email: support@ai-enterprise-os.com
- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions

## ⭐ Star the Project

If you find this useful, please give it a star!

---

**Built with ❤️ for Enterprise Scale** | Version 1.0.0

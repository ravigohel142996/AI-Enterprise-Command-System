"""Initialize the database with sample data"""

import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app.db.database import Base, get_engine
from backend.app.models.models import User, Department
from backend.app.core.security import get_password_hash
from sqlalchemy.orm import sessionmaker

# Get engine and create tables
print("Creating SQLite database tables...")
engine = get_engine()
Base.metadata.create_all(bind=engine)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

try:
    # Check if admin already exists
    existing_admin = db.query(User).filter(User.email == "admin@ai-enterprise.com").first()
    if existing_admin:
        print("⚠️  Admin user already exists, skipping initialization.")
        db.close()
        sys.exit(0)
    
    # Create default admin user
    admin = User(
        email="admin@ai-enterprise.com",
        username="admin",
        hashed_password=get_password_hash("admin123"),
        full_name="System Administrator",
        role="admin",
        department="IT",
        is_active=True
    )
    db.add(admin)
    
    # Create departments
    departments = [
        Department(name="Human Resources", description="HR and talent management"),
        Department(name="Finance", description="Financial operations and accounting"),
        Department(name="Customer Support", description="Customer service and support"),
        Department(name="Marketing", description="Marketing and growth"),
        Department(name="Sales", description="Sales and CRM"),
        Department(name="Operations", description="Operations and automation"),
        Department(name="IT", description="Information Technology"),
        Department(name="Security", description="Cybersecurity and risk management"),
        Department(name="Data Analytics", description="Data science and analytics"),
        Department(name="AI Research", description="AI and ML research"),
        Department(name="Legal", description="Legal and compliance"),
        Department(name="Strategy", description="Business strategy and leadership")
    ]
    
    for dept in departments:
        db.add(dept)
    
    db.commit()
    print("✅ SQLite database initialized successfully!")
    print(f"✅ Database location: {os.path.abspath('./data/ai_enterprise.db')}")
    print("\nDefault admin credentials:")
    print("Email: admin@ai-enterprise.com")
    print("Password: admin123")
    print("\n⚠️  Please change the admin password after first login!")
    
except Exception as e:
    print(f"❌ Error initializing database: {e}")
    db.rollback()
finally:
    db.close()

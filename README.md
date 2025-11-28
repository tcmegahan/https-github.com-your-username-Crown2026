# Crown Christian School Management System – 2026
**Smart Start → Next Level → All-Access**

A comprehensive school management system built with Django 5.2.8, designed to streamline admissions, student/family portals, and administrative operations.

## 🎯 Project Overview

Crown2026 is a three-phase development project:

### Phase 1: Smart Start – Admissions & Enrollment
- Online application system
- Document upload and verification
- Application status tracking
- Automated email notifications
- Admin review dashboard

### Phase 2: Next Level – Student & Family Portal
- Parent/guardian login
- Student profiles and academic records
- Grade viewing and progress reports
- Attendance tracking
- Communication tools

### Phase 3: All-Access – Complete School Operations
- Staff management
- Class scheduling
- Financial management
- Reporting and analytics
- Integration with existing systems

## 🚀 Technology Stack

- **Backend**: Django 5.2.8
- **API**: Django REST Framework
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Authentication**: Django Auth + JWT
- **File Storage**: Django FileField / Cloud storage
- **Frontend**: (TBD - React/Vue planned)

## 📋 Getting Started

See [docs/IMMEDIATE_NEXT_STEPS.md](docs/IMMEDIATE_NEXT_STEPS.md) for detailed setup and development instructions.

### Quick Start

1. Clone the repository:
```powershell
git clone https://github.com/tcmegahan/CrownConnect.git
cd CrownConnect
```

2. Set up virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:
```powershell
pip install -r requirements.txt
```

4. Run migrations:
```powershell
python manage.py migrate
```

5. Start development server:
```powershell
python manage.py runserver
```

## 📁 Project Structure

```
Crown2026/
├── README.md
├── docs/
│   └── IMMEDIATE_NEXT_STEPS.md
├── crown_backend/          # Django project settings
├── admissions/             # Smart Start app
├── portal/                 # Next Level app (future)
├── operations/             # All-Access app (future)
└── requirements.txt
```

## 🤝 Contributing

This project uses GitHub for version control and collaboration:
- Create feature branches for new work
- Write clear commit messages
- Submit pull requests for review
- Follow Django best practices

## 📝 Development Status

- [x] Initial repository setup
- [x] Documentation structure
- [ ] Django project initialization
- [ ] Admissions app development
- [ ] API endpoints
- [ ] Testing suite
- [ ] Deployment configuration

## 📞 Contact

For questions or support, contact the development team.

---

**Current Phase**: Smart Start – Admissions & Enrollment  
**Last Updated**: November 28, 2025

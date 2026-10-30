# xrwvm-fullstack_developer_capstone

## Project Name
Car Dealer Django Application

## Repository
**GitHub Repository:** [xrwvm-fullstack_developer_capstone](https://github.com/aaryanbangale2306/xrwvm-fullstack_developer_capstone)

**GitHub Username:** aaryanbangale2306

---

## Project Description

A full-stack Car Dealership Review Portal web application built as part of the IBM Full Stack Software Developer Professional Certificate (Coursera Capstone Project).

The application allows users to:
- Browse car dealerships across the United States (50 dealerships)
- View and submit dealer reviews
- Register and log in as a user
- View car makes and models available at dealerships
- Analyze review sentiment

---

## Technology Stack

- **Backend:** Python, Django (REST API)
- **Frontend:** React.js, HTML, CSS, JavaScript
- **Database:** SQLite (development)
- **CI/CD:** GitHub Actions (Python lint + JavaScript lint)
- **Deployment:** Gunicorn + WhiteNoise

---

## Project Structure

```
xrwvm-fullstack_developer_capstone/
├── .github/
│   └── workflows/
│       └── ci.yml          # CI/CD: Python + JavaScript lint
├── server/
│   ├── dealership/         # Django app: models, migrations
│   ├── djangoapp/          # Django settings, views, URLs
│   ├── database/
│   │   └── data/
│   │       ├── dealerships.json  (50 dealerships - IBM official dataset)
│   │       ├── car_records.json
│   │       └── reviews.json
│   ├── frontend/
│   │   ├── src/
│   │   │   └── components/
│   │   │       └── Register/
│   │   │           ├── Register.jsx   # Registration form (5 fields + button)
│   │   │           └── Register.css
│   │   └── static/
│   │       └── index.html
│   ├── manage.py
│   └── requirements.txt
├── getalldealers.txt        # Q9 evidence: 50-dealer API response
├── getallcarmakes.txt       # Q14 evidence: 15 make-model pair API response
├── eslint.config.js
├── package.json
└── README.md
```

---

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/fetchDealers` | GET | Returns all 50 dealerships |
| `/fetchDealers/<state>` | GET | Returns dealers filtered by state |
| `/dealer/<id>` | GET | Returns single dealer by ID |
| `/dealer/<id>/reviews` | GET | Returns reviews for a dealer |
| `/djangoapp/get_cars` | GET | Returns 15 make-model pairs |
| `/djangoapp/login` | POST | User login |
| `/djangoapp/logout` | GET | User logout |
| `/djangoapp/register` | POST | User registration |

---

## Models

### CarMake
- `name`, `description`, `country`, `founded_year`

### CarModel
- `car_make` (FK), `dealer_id`, `name`, `type`, `year`

### Dealer
- `id`, `city`, `state`, `st`, `address`, `zip`, `latitude`, `longitude`, `short_name`, `full_name`

### DealerReview
- `dealer_id`, `dealership`, `name`, `purchase`, `review`, `purchase_date`, `car_make`, `car_model`, `car_year`, `sentiment`

---

## Setup and Installation

### Backend

```bash
cd server
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend (React)

The Register component is available at:
`server/frontend/src/components/Register/Register.jsx`

---

## CI/CD

GitHub Actions workflow (`.github/workflows/ci.yml`) runs two jobs on every push/PR to `main`:

1. **lint-python** – flake8 linting on all Python files
2. **lint-javascript** – ESLint linting on all JSX/JS files

---

## Grading Evidence

| Question | File | Status |
|---|---|---|
| Q9 – getalldealers | `getalldealers.txt` | 50 records |
| Q14 – getallcarmakes | `getallcarmakes.txt` | 15 make-model pairs |
| Task 23 – CI/CD | `CI-CD/` folder | Both jobs passing |

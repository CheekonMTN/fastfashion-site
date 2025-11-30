# Fighting Fast Fashion

A data-driven web application that visualizes the environmental impact of fast fashion materials. Calculate your personal footprint, explore material impacts, and discover sustainable solutions.

## Features

- **Personal Impact Calculator**: Calculate your environmental footprint based on clothing purchases
- **Live Water Counter**: Real-time visualization of fashion industry water usage
- **Material Deep Dives**: Detailed information on cotton, polyester, rayon, and wool
- **Interactive Visualizations**: Animated charts and data comparisons
- **Dark Mode**: Toggle between light and dark themes
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

## Technology Stack

- **Backend**: Django 5.2+
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Deployment**: AWS Elastic Beanstalk (configured)

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fastfashion-sitegit
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Open your browser and navigate to `http://127.0.0.1:8000/`

## Environment Variables

For production deployment, set the following environment variables:

- `SECRET_KEY`: Django secret key (required)
- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hostnames
- `DATABASE_URL`: Database connection string (for RDS)
- `SECURE_SSL_REDIRECT`: Set to `True` if using HTTPS

## Deployment

See `AWS_DEPLOYMENT.md` for detailed AWS Elastic Beanstalk deployment instructions.

## Project Structure

```
fastfashion-sitegit/
├── fastfashion/          # Django project settings
├── impact/              # Main application
│   ├── static/          # CSS, JS, images
│   ├── templates/       # HTML templates
│   └── models.py        # Database models
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## License

This is a student project for educational purposes.

## Data Sources

All statistics and data are sourced from public reports and research. See the Sources section on the website for detailed citations.

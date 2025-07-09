# Cats4Control - Applied Category Theory Research Community

A Django-based website for organizing a rich community of researchers in mathematics, engineering, computer science, and social science on the applications of category theory to control systems, optimization, and decision-making.

## Mission

Organize a rich community of researchers in mathematics, engineering, computer science and social science on the applications of category theory to the areas of human and cyber-physical-human information and decision systems, optimization, and control theory.

## Features

### Core Functionality
- **Home Page**: Welcome page with mission statement, upcoming events, active projects, and recent blog posts
- **Events**: Manage conferences, workshops, and seminars
- **Projects**: Collaborative research projects with the following focus areas:
  - Optimization Algorithms
  - Co-Design
  - Layered Control Architectures
  - Scientific Computing
  - Multi-Agent Coordination
- **Researchers**: Community member profiles
- **Blog**: Research insights and discoveries
- **References**: Essential papers and books library
- **ACC 2025**: Special workshop page for "Applied Category Theory for Compositional Decision Making"

### Django Models
- **Researcher**: User profiles with research areas and institutional affiliations
- **Reference**: Database of papers, books, and other academic resources
- **Event**: Conferences, workshops, and seminars
- **Post**: Blog posts by researchers
- **Project**: Collaborative research projects
- **Profile**: Website-specific user settings
- **Talk**: Individual presentations within events
- **Organizer**: Event organizers
- **Speaker**: Event speakers

## Technical Stack

- **Backend**: Django 5.2.4
- **Database**: PostgreSQL (production) / SQLite (development)
- **Frontend**: HTML5, CSS3, JavaScript (with Inter font and Font Awesome icons)
- **Image Processing**: Pillow
- **Deployment**: Heroku-ready with gunicorn
- **Static Files**: Organized in `static/files/slides/` directory

## Directory Structure

```
cats4control/
├── main/                    # Main Django application
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # URL patterns
│   ├── admin.py            # Admin interface
│   └── migrations/         # Database migrations
├── templates/main/         # HTML templates
├── static/files/slides/    # Presentation slides
├── acc2025/               # ACC 2025 workshop content
├── cats4control/          # Django project settings
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment
└── manage.py             # Django management script
```

## Installation and Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
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
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Admin Interface

Access the admin interface at `/admin/` to manage:
- Researchers and their profiles
- Events and workshops
- Research projects and collaborations
- Blog posts and references
- User profiles and settings

Default admin credentials (development only):
- Username: `admin`
- Password: `admin123`

## Heroku Deployment

The application is ready for Heroku deployment with:
- PostgreSQL database configuration
- Static file serving
- Gunicorn web server
- Environment variable support

Set these environment variables in production:
- `SECRET_KEY`: Django secret key
- `DATABASE_URL`: PostgreSQL connection string
- `DEBUG`: Set to `False` for production

## Current Content

### ACC 2025 Workshop
The website includes a dedicated page for the "Applied Category Theory for Compositional Decision Making" workshop at the American Control Conference 2025:
- **Date**: July 7, 2025
- **Time**: 1:45pm – 5:30pm
- **Location**: Plaza Court 6, Portland, OR
- **Organizers**: Gioele Zardini (MIT), James Fairbanks (UFL), Matthew Hale (Georgia Tech), Aaron D. Ames (Caltech)

### Available Slides
- Primer on Applied Category Theory
- Introduction to Categorical Lyapunov Theory
- Compositional Modeling of Sequential Decision Systems
- Scientific Computing with Categories

## Future Enhancements

1. User authentication and registration
2. Interactive project collaboration tools
3. Advanced search and filtering
4. Email notifications for events
5. Integration with academic databases
6. Mobile-responsive design improvements
7. API for external integrations

## Contributing

This platform is designed to grow with the research community. Researchers can:
- Create profiles and showcase their work
- Contribute blog posts and insights
- Organize events and workshops
- Share references and resources
- Collaborate on projects

## License

This project is designed for the academic research community. Please contact the maintainers for usage guidelines.
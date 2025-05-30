# MyToDo - Flask Todo Application

A simple, elegant, and productive Todo application built with Flask and SQLAlchemy.

## Features

- Create, Read, Update, and Delete (CRUD) todo tasks
- Clean and intuitive user interface using Bootstrap 5
- Persistent storage using SQLite database
- Automatic timestamp for each todo item
- Responsive design that works on desktop and mobile
- Search functionality (UI ready, backend implementation pending)

## Tech Stack

- Flask - Web framework
- SQLAlchemy - Database ORM
- Bootstrap 5 - Frontend styling
- SQLite - Database
- Jinja2 - Template engine
- Gunicorn - Production server

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/mytodo.git
cd mytodo
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
python app.py
```

The application will start running at `http://localhost:8000`

## Project Structure

```
├── app.py              # Main application file
├── todo.db            # SQLite database
├── Procfile           # Heroku deployment file
├── requirements.txt   # Project dependencies
├── static/           # Static files (CSS, JS, etc.)
└── templates/        # HTML templates
    ├── about.html
    ├── base_template.html
    ├── index.html
    └── update.html
```

## Database Schema

The application uses a simple Todo model with the following fields:
- sno (Integer, Primary Key)
- title (String, 80 chars)
- description (String, 220 chars)
- date_created (DateTime)

## API Routes

- `GET /` - Home page, displays all todos
- `POST /` - Create a new todo
- `GET /update/<int:sno>` - Display update form for a specific todo
- `POST /update/<int:sno>` - Update a specific todo
- `GET /delete/<int:sno>` - Delete a specific todo
- `GET /about` - About page

## Deployment

The application is ready for deployment on Heroku using Gunicorn. A Procfile is included.

## Development

To run the application in development mode:

```bash
python app.py
```

The development server will run with debug mode enabled at port 8000.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Credits

Created by Harshal Bhave 

UI Design inspired by modern, minimalist design principles and implemented using Bootstrap 5.

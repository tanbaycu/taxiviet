# Tuấn Taxi - Taxi Booking Website

This project is a simple and modern website for a taxi service called "Tuấn Taxi" (also referred to as "SAIGONWEST Premium Taxi Service"). It allows users to book taxi rides, get in touch with the service provider, and learn more about the services offered. The primary focus of the service is on providing taxi services between Saigon (Ho Chi Minh City) and the Mekong Delta region of Vietnam ("Miền Tây").

## Features

* **Online Booking:** Users can fill out a detailed form to book a taxi, specifying pickup and destination addresses, date, time, and car type.
* **Quick Booking:** A simplified booking form is available on the homepage for faster booking.
* **Contact Form:** Users can send messages to the taxi service provider through a contact form.
* **Email Notifications:** All booking and contact requests are sent to the administrator's email address.
* **Responsive Design:** The website is designed to work well on both desktop and mobile devices.
* **Modern UI/UX:** The user interface is built with Tailwind CSS and includes animations and interactive elements for a smooth user experience.

## Technologies Used

* **Frontend:**
  * HTML5
  * Tailwind CSS
  * JavaScript
* **Backend:**
  * Python
  * Flask (a micro web framework for Python)
  * Flask-Mail (for sending emails)
* **Deployment:**
  * Vercel
  * Gunicorn (as a WSGI HTTP server)

## Sample Project Structure

```txt
taxiviet/
│
├── app/                    # main app package
│   ├── __init__.py         # create app, load configs, register routes
│   ├── routes.py           # define routes here (or split later into /routes/)
│   ├── models.py           # for database models (optional now)
│   ├── services.py         # helper / logic functions (optional)
│   ├── templates/          # HTML templates
│   └── static/             # static files (CSS, JS, images)
│
├── tests/                  # future: add test files here
│   └── test_app.py
│
├── .env
├── .gitignore
├── .editorconfig
├── requirements.txt
├── dev-requirements.txt
├── vercel.json
├── README.md
├── GEMINI.md
└── app.py                  # simple entry point: `from app import app`
```

## Setup and Local Development

To run this project locally, you will need to have Python and `pip` installed.

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd taxiviet
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    pip install -r dev-requirements.txt
    ```

4. **Configure environment variables:**

    The application uses `flask-mail` to send emails and requires environment variables for configuration. Create a `.env` file in the root of the project and add the following variables with your SMTP server details:

    ```env
    MAIL_SERVER=smtp.gmail.com
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=your-email@example.com
    MAIL_PASSWORD=your-email-password
    MAIL_DEFAULT_SENDER="Your Name <your-email@example.com>"
    ADMIN_EMAIL=admin-email@example.com
    ```

5. **Run the application:**

    ```bash
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000`.

## Deployment

This project is configured for deployment on [Vercel](https://vercel.com/). The `vercel.json` file contains the necessary configuration to deploy the Flask application. When deploying to Vercel, make sure to set the environment variables for the email configuration in the Vercel project settings.

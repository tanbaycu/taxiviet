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

## Project Structure

```txt
.
├── .editorconfig
├── app.py              # Flask backend application
├── index.html          # Main frontend file
├── README.md           # This file
├── requirements.txt    # Python dependencies
└── vercel.json         # Vercel deployment configuration
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
    ```

4. **Configure environment variables:**

    The application uses `flask-mail` to send emails. You need to configure your SMTP server settings in `app.py`. It is recommended to use environment variables for sensitive information like email credentials.

    In `app.py`, modify the following lines with your email provider's details:

    ```python
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 587
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USERNAME"] = "your-email@example.com"
    app.config["MAIL_PASSWORD"] = "your-email-password"
    app.config["MAIL_DEFAULT_SENDER"] = ("Your Name", "your-email@example.com")
    app.config["ADMIN_EMAIL"] = "admin-email@example.com"
    ```

5. **Run the application:**

    ```bash
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000`.

## Deployment

This project is configured for deployment on [Vercel](https://vercel.com/). The `vercel.json` file contains the necessary configuration to deploy the Flask application. When deploying to Vercel, make sure to set the environment variables for the email configuration in the Vercel project settings.

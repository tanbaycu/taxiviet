# Gemini Project Overview: Tuấn Taxi Booking Website

This document provides a comprehensive overview of the Tuấn Taxi booking website project, designed to be understood by the Gemini model.

## 1. Project Purpose

The project is a website for a taxi service called "Tuấn Taxi" (or "SAIGONWEST Premium Taxi Service"). It facilitates booking taxi rides, primarily between Ho Chi Minh City (Saigon) and the Mekong Delta region of Vietnam ("Miền Tây").

## 2. Key Features

*   **Online Booking:** A detailed form for users to book a taxi, including pickup/destination, date/time, and car type.
*   **Quick Booking:** A simplified booking form on the homepage for faster bookings.
*   **Contact Form:** Allows users to send messages to the service provider.
*   **Email Notifications:** All booking and contact requests trigger an email to the administrator.
*   **Responsive Design:** The website is optimized for both desktop and mobile devices, serving different HTML files (`index.html` for desktop, `mobile.html` for mobile) based on the user agent.
*   **Modern UI/UX:** Built with Tailwind CSS, featuring animations and interactive elements.

## 3. Technologies Used

*   **Backend:**
    *   **Python:** The core programming language.
    *   **Flask:** A micro web framework for handling routing and requests.
    *   **Flask-Mail:** Used for sending email notifications.
    *   **Gunicorn:** A WSGI HTTP server for production deployment.
    *   **python-dotenv:** For managing environment variables.
    *   **user-agents:** To parse user-agent strings and determine if the user is on a mobile device.
*   **Frontend:**
    *   **HTML5:** The markup language for the website.
    *   **Tailwind CSS:** A utility-first CSS framework for styling.
    *   **JavaScript:** For client-side interactivity.
*   **Deployment:**
    *   **Vercel:** The project is configured for deployment on Vercel.

## 4. Project Structure

```
/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies for production
├── dev-requirements.txt # Python dependencies for development
├── vercel.json         # Vercel deployment configuration
├── templates/
│   ├── index.html      # Desktop version of the website
│   └── mobile.html     # Mobile version of the website
├── .gitignore
├── README.md
└── GEMINI.md
```

## 5. How the Application Works

### 5.1. Routing and Rendering

*   The main Flask application is in `app.py`.
*   The root URL (`/`) checks the user agent. If it's a mobile device or tablet, it redirects to `/mobile.html`. Otherwise, it redirects to `/index.html`.
*   `/index.html` renders the `index.html` template (for desktops).
*   `/mobile.html` renders the `mobile.html` template (for mobile devices).

### 5.2. Form Submissions

The application has three main form submission endpoints:

1.  **`/submit_booking` (POST):**
    *   Handles the detailed booking form.
    *   Extracts form data (name, phone, email, pickup/destination, date/time, car type, notes).
    *   Formats the data into an HTML email.
    *   Sends the email to the admin's email address (configured via environment variables).
    *   Returns a JSON response for AJAX requests or flashes a message and redirects for standard form submissions.

2.  **`/submit_contact` (POST):**
    *   Handles the contact form.
    *   Extracts form data (name, email, phone, subject, message).
    *   Formats the data into an HTML email.
    *   Sends the email to the admin's email address.
    *   Returns a JSON response or flashes a message and redirects.

3.  **`/quick_booking` (POST):**
    *   Handles the simplified booking form from the homepage.
    *   Extracts form data (pickup, destination, date, time).
    *   Formats the data into an HTML email with a note that it's a quick booking.
    *   Sends the email to the admin's email address.
    *   Returns a JSON response or flashes a message and redirects.

### 5.3. Configuration

*   The application uses a `.env` file to load environment variables.
*   **Email Configuration:** `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_TLS`, `MAIL_USERNAME`, `MAIL_PASSWORD`, `MAIL_DEFAULT_SENDER`, and `ADMIN_EMAIL` must be set as environment variables for the email functionality to work.
*   **Secret Key:** A secret key for flash messages is generated using `os.urandom(24)`.

## 6. How to Run the Project Locally

1.  **Clone the repository.**
2.  **Create and activate a virtual environment.**
3.  **Install dependencies:** `pip install -r requirements.txt` (and `pip install -r dev-requirements.txt` for development).
4.  **Create a `.env` file** and configure the email server settings (as described in the `README.md`).
5.  **Run the application:** `python app.py`.
6.  The application will be available at `http://127.0.0.1:5000`.

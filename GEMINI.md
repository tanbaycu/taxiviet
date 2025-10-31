# Gemini Project Overview: Tuấn Taxi Booking Website

This document provides a comprehensive overview of the Tuấn Taxi booking website project, designed to be understood by the Gemini model.

## 1. Project Purpose

The project is a static website for a taxi service called "Tuấn Taxi" (or "SAIGONWEST Premium Taxi Service"). It showcases the services offered and provides contact information for booking.

## 2. Key Features

*   **Single-Page Layout:** A modern single-page design with smooth-scrolling navigation.
*   **Responsive Design:** The website is optimized for both desktop and mobile devices.
*   **Modern UI/UX:** Built with Tailwind CSS, featuring animations and interactive elements.
*   **Iconography:** Utilizes the `lucide` icon library for clean and consistent icons.
*   **Contact Information:** Prominently displays phone numbers and links to Zalo and Facebook for easy booking.

## 3. Technologies Used

*   **Frontend:**
    *   **HTML5:** The markup language for the website.
    *   **Tailwind CSS:** A utility-first CSS framework for styling.
    *   **JavaScript:** For client-side interactivity (e.g., mobile menu, scroll animations).
    *   **Vite:** A modern frontend build tool.
    *   **lucide:** A library for icons.
*   **Deployment:**
    *   **Vercel:** The project is configured for deployment on Vercel.

## 4. Project Structure

```
/
├── index.html          # Main HTML file
├── src/
│   ├── main.js         # Main JavaScript file
│   └── style.css       # Main CSS file
├── package.json        # Project dependencies and scripts
├── vite.config.js      # Vite configuration
├── postcss.config.js   # PostCSS configuration
├── vercel.json         # Vercel deployment configuration
├── .gitignore
├── README.md
└── GEMINI.md
```

## 5. How the Application Works

### 5.1. Build Process

*   The project is built using Vite. The `dev` script starts a development server, and the `build` script generates a static `dist` folder for production.
*   Tailwind CSS is used for styling, processed via PostCSS.

### 5.2. Client-Side Logic (`src/main.js`)

*   **Icon Initialization:** Initializes `lucide` icons.
*   **Mobile Menu:** Toggles the visibility of the mobile navigation menu.
*   **Scroll Effects:**
    *   Adds a "scrolled" class to the navbar when the user scrolls down.
    *   Shows/hides a "back to top" button based on scroll position.
*   **Animations:** Uses the Intersection Observer API to trigger fade-in animations as elements scroll into view.
*   **Smooth Scrolling:** Implements smooth scrolling for anchor links.
*   **Booking Form:** The booking form currently displays a simple alert and does not have a backend submission mechanism.

### 5.3. Deployment

*   The `vercel.json` file configures the project for deployment on Vercel. It specifies that the `dist` directory should be served as a static site.

## 6. How to Run the Project Locally

1.  **Clone the repository.**
2.  **Install dependencies:** `npm install`
3.  **Run the development server:** `npm run dev`
4.  The application will be available at `http://localhost:5173`.
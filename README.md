# Tuấn Taxi - Taxi Booking Website

This project is a simple and modern static website for a taxi service called "Tuấn Taxi" (also referred to as "SAIGONWEST Premium Taxi Service"). It showcases the services offered and provides contact information for booking.

## Key Features

* **Single-Page Layout:** A modern single-page design with smooth-scrolling navigation.
* **Responsive Design:** The website is optimized for both desktop and mobile devices.
* **Modern UI/UX:** Built with Tailwind CSS, featuring animations and interactive elements.
* **Iconography:** Utilizes the `lucide` icon library for clean and consistent icons.
* **Contact Information:** Prominently displays phone numbers and links to Zalo and Facebook for easy booking.

## Technologies Used

* **Frontend:**
  * HTML5
  * Tailwind CSS
  * JavaScript
  * Vite
  * lucide
* **Deployment:**
  * Vercel

## Project Structure

```txt
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

## Setup and Local Development

To run this project locally, you will need to have Node.js and `npm` installed.

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd taxiviet
    ```

2. **Install the dependencies:**

    ```bash
    npm install
    ```

3. **Run the development server:**

    ```bash
    npm run dev
    ```

    The application will be available at `http://localhost:5173`.

## Deployment

This project is configured for deployment on [Vercel](https://vercel.com/).

---

## 📱 Responsive Design Breakpoints

This project follows **mobile-first design**, meaning styles start from mobile (base) and scale up using Tailwind’s responsive prefixes.

| Breakpoint | Prefix   | Min Width | Common Device Range          |
| ---------- | -------- | --------- | ---------------------------- |
| **Base**   | _(none)_ | 0px       | Small phones (320–375px)     |
| **sm**     | `sm:`    | 640px     | Larger phones, small tablets |
| **md**     | `md:`    | 768px     | Tablets, small laptops       |
| **lg**     | `lg:`    | 1024px    | Laptops, desktops            |
| **xl**     | `xl:`    | 1280px    | Large desktops               |
| **2xl**    | `2xl:`   | 1536px    | Very large screens           |

**Tip:**

* Start designing for **mobile (320-375px)**.
* Gradually enhance layout using these breakpoints.
* Keep base styles lightweight and readable.

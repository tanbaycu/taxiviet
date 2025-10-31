import { createIcons, icons } from "lucide";
import "./style.css";

// Cache DOM elements
const el = {
    mobileMenuBtn: document.getElementById("mobile-menu-btn"),
    mobileMenu: document.getElementById("mobile-menu"),
    menuIcon: document.getElementById("menu-icon"),
    navbar: document.getElementById("navbar"),
    backToTopBtn: document.getElementById("back-to-top"),
    bookingForm: document.getElementById("bookingForm"),
};

// Update menu icon
const updateMenuIcon = (isHidden) => {
    if (!el.menuIcon) return;
    el.menuIcon.innerHTML = "";
    el.menuIcon.setAttribute("data-lucide", isHidden ? "menu" : "x");
    lucide.createIcons();
};

// Mobile menu toggle
el.mobileMenuBtn?.addEventListener("click", () => {
    updateMenuIcon(el.mobileMenu?.classList.toggle("hidden"));
});

// Close menu on link click
document.querySelectorAll("#mobile-menu a").forEach((link) => {
    link.addEventListener("click", () => {
        el.mobileMenu?.classList.add("hidden");
        updateMenuIcon(true);
    });
});

// Scroll handler
window.addEventListener("scroll", () => {
    const y = window.pageYOffset;

    el.navbar?.classList.toggle("scrolled", y > 100);
    el.backToTopBtn?.classList.toggle("opacity-0", y <= 300);
    el.backToTopBtn?.classList.toggle("invisible", y <= 300);
});

// Back to top
el.backToTopBtn?.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

// Form submission
el.bookingForm?.addEventListener("submit", (e) => {
    e.preventDefault();
    alert(
        "Cảm ơn bạn đã đặt xe! Chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất.",
    );
});

// Intersection Observer
const observer = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
            }
        });
    },
    {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px",
    },
);

document
    .querySelectorAll(".fade-in-up, .fade-in-left, .fade-in-right")
    .forEach((el) => {
        observer.observe(el);
    });

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));

        if (target) {
            window.scrollTo({
                top: target.offsetTop - 120,
                behavior: "smooth",
            });
            el.mobileMenu?.classList.add("hidden");
            updateMenuIcon(true);
        }
    });
});

// Initialize icons
createIcons({ icons });

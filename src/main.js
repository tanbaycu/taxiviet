"use strict";

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
    el.menuIcon.setAttribute("data-lucide", isHidden ? "menu" : "x");
    createIcons({ icons });
};

// Toggle mobile menu
const toggleMobileMenu = () => {
    if (!el.mobileMenu) return;
    const isHidden = el.mobileMenu.classList.toggle("hidden");
    updateMenuIcon(isHidden);
};

el.mobileMenuBtn?.addEventListener("click", toggleMobileMenu);

// Close mobile menu on link click
el.mobileMenu?.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
        el.mobileMenu.classList.add("hidden");
        updateMenuIcon(true);
    });
});

// Scroll handler
const handleScroll = () => {
    const y = window.pageYOffset;
    el.navbar?.classList.toggle("scrolled", y > 100);

    const showBackToTop = y > 300;
    if (el.backToTopBtn) {
        el.backToTopBtn.classList.toggle("opacity-0", !showBackToTop);
        el.backToTopBtn.classList.toggle("invisible", !showBackToTop);
    }
};

window.addEventListener("scroll", handleScroll);

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

// Intersection Observer for fade-in animations
const observer = new IntersectionObserver(
    (entries) => {
        entries.forEach(({ target, isIntersecting }) => {
            if (isIntersecting && target instanceof HTMLElement) {
                target.style.opacity = "1";
                target.style.transform = "translateY(0)";
            }
        });
    },
    { threshold: 0.1, rootMargin: "0px 0px -50px 0px" },
);

Array.from(
    document.querySelectorAll(".fade-in-up, .fade-in-left, .fade-in-right"),
).forEach((el) => {
    observer.observe(el);
});

// Smooth scroll for anchor links
Array.from(document.querySelectorAll('a[href^="#"]')).forEach((anchor) => {
    anchor.addEventListener("click", (e) => {
        e.preventDefault();
        const target = document.querySelector(
            anchor.getAttribute("href") || "",
        );
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

// Conversion function
function gtag_report_conversion(url) {
    var callback = function () {
        if (typeof url != "undefined") {
            window.location = url;
        }
    };
    gtag("event", "conversion", {
        send_to: "AW-17769752726/rG-8CK7m3MkbEJbRo5lC",
        event_callback: callback,
    });
    return false;
}

// Track all buttons with data attribute
document.querySelectorAll("[data-conversion]").forEach((btn) => {
    btn.addEventListener("click", function () {
        gtag_report_conversion();
    });
});

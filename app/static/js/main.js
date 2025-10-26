// Initialize Lucide icons
lucide.createIcons();

// Mobile menu toggle
const mobileMenuBtn = document.getElementById("mobile-menu-btn");
const mobileMenu = document.getElementById("mobile-menu");

mobileMenuBtn?.addEventListener("click", () => {
    mobileMenu?.classList.toggle("hidden");
});

const navbar = document.getElementById("navbar");
window.addEventListener("scroll", () => {
    if (window.pageYOffset > 100) {
        navbar?.classList.add("scrolled");
    } else {
        navbar?.classList.remove("scrolled");
    }
});

// Back to top functionality
const backToTopBtn = document.getElementById("back-to-top");

window.addEventListener("scroll", () => {
    if (window.pageYOffset > 300) {
        backToTopBtn?.classList.remove("opacity-0", "invisible");
    } else {
        backToTopBtn?.classList.add("opacity-0", "invisible");
    }
});

backToTopBtn?.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

// Form submission
document
    .getElementById("bookingForm")
    ?.addEventListener("submit", function (e) {
        e.preventDefault();
        alert(
            "Cảm ơn bạn đã đặt xe! Chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất.",
        );
    });

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = "1";
            entry.target.style.transform = "translateY(0)";
        }
    });
}, observerOptions);

// Observe all fade-in elements
document
    .querySelectorAll(".fade-in-up, .fade-in-left, .fade-in-right")
    .forEach((el) => {
        observer.observe(el);
    });

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
            const offsetTop = target.offsetTop - 120;
            window.scrollTo({
                top: offsetTop,
                behavior: "smooth",
            });
        }
        mobileMenu?.classList.add("hidden");
    });
});

// Initialize Lucide icons
lucide.createIcons();

// Cache DOM elements
const elements = {
    mobileMenuBtn: document.getElementById("mobile-menu-btn"),
    mobileMenu: document.getElementById("mobile-menu"),
    menuIcon: document.getElementById("menu-icon"),
    navbar: document.getElementById("navbar"),
    backToTopBtn: document.getElementById("back-to-top"),
    bookingForm: document.getElementById("bookingForm"),
};

// Mobile menu toggle with icon update
elements.mobileMenuBtn?.addEventListener("click", () => {
    const isHidden = elements.mobileMenu?.classList.toggle("hidden");
    updateMenuIcon(isHidden);
});

// Close menu when clicking navigation links
document.querySelectorAll("#mobile-menu a").forEach((link) => {
    link.addEventListener("click", () => {
        elements.mobileMenu?.classList.add("hidden");
        updateMenuIcon(true);
    });
});

// Update menu icon helper function
function updateMenuIcon(isHidden) {
    if (elements.menuIcon) {
        elements.menuIcon.innerHTML = "";
        elements.menuIcon.setAttribute("data-lucide", isHidden ? "menu" : "x");
        lucide.createIcons();
    }
}

// Scroll event handler (navbar + back to top)
window.addEventListener("scroll", () => {
    const scrollY = window.pageYOffset;

    // Navbar scrolled state
    if (scrollY > 100) {
        elements.navbar?.classList.add("scrolled");
    } else {
        elements.navbar?.classList.remove("scrolled");
    }

    // Back to top button visibility
    if (scrollY > 300) {
        elements.backToTopBtn?.classList.remove("opacity-0", "invisible");
    } else {
        elements.backToTopBtn?.classList.add("opacity-0", "invisible");
    }
});

// Back to top click handler
elements.backToTopBtn?.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

// Form submission handler
elements.bookingForm?.addEventListener("submit", (e) => {
    e.preventDefault();
    alert(
        "Cảm ơn bạn đã đặt xe! Chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất.",
    );
});

// Intersection Observer for animations
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

// Observe fade-in elements
document
    .querySelectorAll(".fade-in-up, .fade-in-left, .fade-in-right")
    .forEach((el) => {
        observer.observe(el);
    });

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));

        if (target) {
            window.scrollTo({
                top: target.offsetTop - 120,
                behavior: "smooth",
            });
        }

        // Close mobile menu and reset icon
        elements.mobileMenu?.classList.add("hidden");
        updateMenuIcon(true);
    });
});

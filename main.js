(() => {
    const mobileMenu = document.getElementById("mobileMenu");
    const mobileMenuBtn = document.getElementById("mobileMenuBtn");
    const backToTop = document.getElementById("backToTop");
    const nav = document.querySelector("nav");

    const setMobileMenuOpen = (isOpen) => {
        if (!mobileMenu) {
            return;
        }

        mobileMenu.classList.toggle("hidden", !isOpen);
        if (mobileMenuBtn) {
            mobileMenuBtn.setAttribute("aria-expanded", String(isOpen));
        }
    };

    const toggleMobileMenu = () => {
        if (!mobileMenu) {
            return;
        }

        const shouldOpen = mobileMenu.classList.contains("hidden");
        setMobileMenuOpen(shouldOpen);
    };

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener("click", toggleMobileMenu);
    }

    if (mobileMenu) {
        mobileMenu.querySelectorAll("[data-close-menu='true']").forEach((element) => {
            element.addEventListener("click", () => setMobileMenuOpen(false));
        });
    }

    document.querySelectorAll("a[href^='#']:not([href='#'])").forEach((anchor) => {
        anchor.addEventListener("click", (event) => {
            const href = anchor.getAttribute("href");
            if (!href) {
                return;
            }

            const targetId = href.slice(1);
            const target = targetId ? document.getElementById(targetId) : null;
            if (!target) {
                return;
            }

            event.preventDefault();
            target.scrollIntoView({ behavior: "smooth", block: "start" });
            setMobileMenuOpen(false);
        });
    });

    if ("IntersectionObserver" in window) {
        const skillObserver = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (!entry.isIntersecting) {
                        return;
                    }

                    const bar = entry.target;
                    const targetWidth = bar.getAttribute("data-width");
                    if (!targetWidth) {
                        return;
                    }

                    setTimeout(() => {
                        bar.style.width = targetWidth;
                    }, 200);
                });
            },
            { threshold: 0.3 }
        );

        document.querySelectorAll(".skill-progress").forEach((bar) => {
            const width = bar.style.width;
            bar.style.width = "0";
            bar.setAttribute("data-width", width);
            skillObserver.observe(bar);
        });
    }

    const updateOnScroll = () => {
        if (nav) {
            nav.style.background = window.scrollY > 50 ? "rgba(10, 10, 10, 0.95)" : "";
        }

        if (!backToTop) {
            return;
        }

        if (window.scrollY > 500) {
            backToTop.classList.remove("opacity-0", "pointer-events-none");
            backToTop.classList.add("opacity-100");
        } else {
            backToTop.classList.add("opacity-0", "pointer-events-none");
            backToTop.classList.remove("opacity-100");
        }
    };

    window.addEventListener("scroll", updateOnScroll);

    if (backToTop) {
        backToTop.addEventListener("click", () => {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }

    // Keep direct contact links out of static HTML to reduce basic scraping.
    const emailAddress = atob("YXJ5YW5taXNocmFhMThAZ21haWwuY29t");
    const phoneNumber = atob("KzkxOTk5OTMzMzMyOA==");

    document.querySelectorAll("[data-email-link='true']").forEach((link) => {
        link.setAttribute("href", `mailto:${emailAddress}`);
    });
    document.querySelectorAll("[data-phone-link='true']").forEach((link) => {
        link.setAttribute("href", `tel:${phoneNumber}`);
    });
    document.querySelectorAll("[data-email-text='true']").forEach((textElement) => {
        textElement.textContent = emailAddress;
    });
    document.querySelectorAll("[data-phone-text='true']").forEach((textElement) => {
        textElement.textContent = phoneNumber.replace("+91", "+91 ");
    });

    updateOnScroll();
})();

// Theme management
class ThemeManager {
    constructor() {
        this.theme = localStorage.getItem('theme') || 'light';
        this.themeToggle = document.getElementById('theme-toggle');
        this.themeIcon = document.querySelector('.theme-icon');
        
        this.init();
    }
    
    init() {
        this.setTheme(this.theme);
        this.themeToggle.addEventListener('click', () => this.toggleTheme());
        
        // Listen for system theme changes
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
            if (!localStorage.getItem('theme')) {
                this.setTheme(e.matches ? 'dark' : 'light');
            }
        });
    }
    
    setTheme(theme) {
        this.theme = theme;
        document.documentElement.setAttribute('data-theme', theme);
        this.themeIcon.textContent = theme === 'dark' ? '☀️' : '🌙';
        localStorage.setItem('theme', theme);
    }
    
    toggleTheme() {
        const newTheme = this.theme === 'light' ? 'dark' : 'light';
        this.setTheme(newTheme);
    }
}

// Tab management
class TabManager {
    constructor() {
        this.tabButtons = document.querySelectorAll('.tab-button');
        this.tabContents = document.querySelectorAll('.tab-content');
        
        this.init();
    }
    
    init() {
        this.tabButtons.forEach(button => {
            button.addEventListener('click', () => this.switchTab(button.dataset.tab));
        });
    }
    
    switchTab(targetTab) {
        // Remove active class from all buttons and contents
        this.tabButtons.forEach(btn => btn.classList.remove('active'));
        this.tabContents.forEach(content => content.classList.remove('active'));
        
        // Add active class to target button and content
        const targetButton = document.querySelector(`[data-tab="${targetTab}"]`);
        const targetContent = document.getElementById(targetTab);
        
        if (targetButton && targetContent) {
            targetButton.classList.add('active');
            targetContent.classList.add('active');
        }
    }
}

// Copy to clipboard functionality
class ClipboardManager {
    constructor() {
        this.copyButtons = document.querySelectorAll('.copy-btn');
        this.init();
    }
    
    init() {
        this.copyButtons.forEach(button => {
            button.addEventListener('click', () => this.copyToClipboard(button));
        });
    }
    
    async copyToClipboard(button) {
        const textToCopy = button.dataset.copy;
        
        try {
            await navigator.clipboard.writeText(textToCopy);
            this.showCopyFeedback(button);
        } catch (err) {
            // Fallback for older browsers
            this.fallbackCopyTextToClipboard(textToCopy, button);
        }
    }
    
    fallbackCopyTextToClipboard(text, button) {
        const textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.top = '0';
        textArea.style.left = '0';
        textArea.style.position = 'fixed';
        
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        
        try {
            document.execCommand('copy');
            this.showCopyFeedback(button);
        } catch (err) {
            console.error('Fallback: Oops, unable to copy', err);
        }
        
        document.body.removeChild(textArea);
    }
    
    showCopyFeedback(button) {
        const originalText = button.textContent;
        button.textContent = '✅';
        button.style.color = 'var(--accent-color)';
        
        setTimeout(() => {
            button.textContent = originalText;
            button.style.color = '';
        }, 2000);
    }
}

// Navigation management
class NavigationManager {
    constructor() {
        this.navbar = document.querySelector('.navbar');
        this.navLinks = document.querySelectorAll('.nav-link');
        this.hamburger = document.getElementById('nav-hamburger');
        
        this.init();
    }
    
    init() {
        // Smooth scrolling for nav links
        this.navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                const href = link.getAttribute('href');
                if (href.startsWith('#')) {
                    e.preventDefault();
                    const target = document.querySelector(href);
                    if (target) {
                        const offsetTop = target.offsetTop - 80; // Account for fixed navbar
                        window.scrollTo({
                            top: offsetTop,
                            behavior: 'smooth'
                        });
                    }
                }
            });
        });
        
        // Navbar scroll effect
        window.addEventListener('scroll', () => this.handleNavbarScroll());
        
        // Mobile menu toggle (if implemented)
        if (this.hamburger) {
            this.hamburger.addEventListener('click', () => this.toggleMobileMenu());
        }
    }
    
    handleNavbarScroll() {
        if (window.scrollY > 100) {
            this.navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
            if (document.documentElement.getAttribute('data-theme') === 'dark') {
                this.navbar.style.backgroundColor = 'rgba(15, 23, 42, 0.95)';
            }
        } else {
            this.navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.9)';
            if (document.documentElement.getAttribute('data-theme') === 'dark') {
                this.navbar.style.backgroundColor = 'rgba(15, 23, 42, 0.9)';
            }
        }
    }
    
    toggleMobileMenu() {
        // Mobile menu implementation would go here
        console.log('Mobile menu toggle clicked');
    }
}

// Scroll animations
class ScrollAnimations {
    constructor() {
        this.observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        this.init();
    }
    
    init() {
        if ('IntersectionObserver' in window) {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('animate-in');
                    }
                });
            }, this.observerOptions);
            
            // Observe cards and sections
            const elementsToAnimate = document.querySelectorAll('.feature-card, .install-card, .example-card, .type-category');
            elementsToAnimate.forEach(el => observer.observe(el));
        }
    }
}

// Analytics and tracking (optional)
class Analytics {
    constructor() {
        this.init();
    }
    
    init() {
        // Track button clicks
        document.addEventListener('click', (e) => {
            if (e.target.matches('.btn, .nav-link, .copy-btn')) {
                this.trackEvent('click', {
                    element: e.target.tagName.toLowerCase(),
                    text: e.target.textContent?.slice(0, 50) || '',
                    href: e.target.href || ''
                });
            }
        });
        
        // Track theme changes
        document.addEventListener('themeChanged', (e) => {
            this.trackEvent('theme_change', { theme: e.detail.theme });
        });
    }
    
    trackEvent(eventName, properties = {}) {
        // Console log for development
        console.log('Analytics Event:', eventName, properties);
        
        // Here you would integrate with your analytics provider
        // Examples: Google Analytics, Plausible, Fathom, etc.
        // gtag('event', eventName, properties);
        // plausible(eventName, { props: properties });
    }
}

// Performance monitoring
class PerformanceMonitor {
    constructor() {
        this.init();
    }
    
    init() {
        // Monitor page load time
        window.addEventListener('load', () => {
            const loadTime = performance.now();
            console.log(`Page loaded in ${loadTime.toFixed(2)}ms`);
        });
        
        // Monitor largest contentful paint
        if ('PerformanceObserver' in window) {
            const observer = new PerformanceObserver((entryList) => {
                const entries = entryList.getEntries();
                const lastEntry = entries[entries.length - 1];
                console.log('LCP:', lastEntry.startTime);
            });
            observer.observe({ entryTypes: ['largest-contentful-paint'] });
        }
    }
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize all managers
    new ThemeManager();
    new TabManager();
    new ClipboardManager();
    new NavigationManager();
    new ScrollAnimations();
    new Analytics();
    new PerformanceMonitor();
    
    // Add loading complete class
    document.body.classList.add('loaded');
    
    console.log('🎭 AutoFaker website initialized successfully!');
});

// Service Worker registration (for PWA capabilities)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}

// Handle errors gracefully
window.addEventListener('error', (e) => {
    console.error('Global error handler:', e.error);
    // You could send this to an error tracking service
});

// Export for testing purposes
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        ThemeManager,
        TabManager,
        ClipboardManager,
        NavigationManager,
        ScrollAnimations,
        Analytics,
        PerformanceMonitor
    };
}

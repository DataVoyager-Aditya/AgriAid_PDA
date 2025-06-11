// AgriAid Custom JavaScript

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {

    // Initialize all components
    initializeScrollAnimations();
    initializeImageUpload();
    initializeFormValidation();
    initializeNavigationEffects();
    initializeCounterAnimations();
    initializeTooltips();

});

// Scroll Animations
function initializeScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    // Observe elements that should animate on scroll
    const animateElements = document.querySelectorAll('.feature-card, .crop-card, .service-card, .testimonial-card, .mission-card');
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.6s ease';
        observer.observe(el);
    });

    // Add CSS for animation
    const style = document.createElement('style');
    style.textContent = `
        .animate-in {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
    document.head.appendChild(style);
}

// Image Upload Functionality
function initializeImageUpload() {
    const fileInput = document.getElementById('file');
    const uploadArea = document.getElementById('uploadArea');
    const uploadContent = document.getElementById('uploadContent');
    const imagePreview = document.getElementById('imagePreview');
    const previewImg = document.getElementById('previewImg');

    if (!fileInput || !uploadArea) return;

    // File input change handler
    fileInput.addEventListener('change', function(e) {
        handleFileSelect(e.target.files[0]);
    });

    // Drag and drop handlers
    uploadArea.addEventListener('dragover', function(e) {
        e.preventDefault();
        e.stopPropagation();
        uploadArea.classList.add('drag-over');
    });

    uploadArea.addEventListener('dragleave', function(e) {
        e.preventDefault();
        e.stopPropagation();
        uploadArea.classList.remove('drag-over');
    });

    uploadArea.addEventListener('drop', function(e) {
        e.preventDefault();
        e.stopPropagation();
        uploadArea.classList.remove('drag-over');

        const files = e.dataTransfer.files;
        if (files.length > 0) {
            handleFileSelect(files[0]);
        }
    });

    // Click to upload
    uploadArea.addEventListener('click', function(e) {
        if (e.target.tagName !== 'BUTTON') {
            fileInput.click();
        }
    });

    function handleFileSelect(file) {
        if (!file) return;

        // Validate file type
        const validTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp'];
        if (!validTypes.includes(file.type)) {
            showAlert('Please select a valid image file (JPEG, PNG, WebP)', 'error');
            return;
        }

        // Validate file size (16MB limit)
        const maxSize = 16 * 1024 * 1024;
        if (file.size > maxSize) {
            showAlert('File size must be less than 16MB', 'error');
            return;
        }

        // Create FileList and assign to input
        const dt = new DataTransfer();
        dt.items.add(file);
        fileInput.files = dt.files;

        // Show preview
        const reader = new FileReader();
        reader.onload = function(e) {
            previewImg.src = e.target.result;
            uploadContent.style.display = 'none';
            imagePreview.style.display = 'block';

            // Add fade-in animation
            imagePreview.style.opacity = '0';
            setTimeout(() => {
                imagePreview.style.transition = 'opacity 0.3s ease';
                imagePreview.style.opacity = '1';
            }, 10);
        };
        reader.readAsDataURL(file);
    }

    // Global function for removing image
    window.removeImage = function() {
        fileInput.value = '';
        uploadContent.style.display = 'block';
        imagePreview.style.display = 'none';
        uploadArea.classList.remove('drag-over');
    };
}

// Form Validation
function initializeFormValidation() {
    const forms = document.querySelectorAll('form[action*="predict"], form[action*="contact"]');

    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(form)) {
                e.preventDefault();
                return false;
            }

            // Show loading state for prediction form
            if (form.action.includes('predict')) {
                showLoadingState();
            }
        });
    });

    function validateForm(form) {
        let isValid = true;
        const requiredFields = form.querySelectorAll('[required]');

        requiredFields.forEach(field => {
            const errorMsg = field.parentNode.querySelector('.error-message');
            if (errorMsg) errorMsg.remove();

            if (!field.value.trim()) {
                showFieldError(field, 'This field is required');
                isValid = false;
            } else if (field.type === 'email' && !isValidEmail(field.value)) {
                showFieldError(field, 'Please enter a valid email address');
                isValid = false;
            }
        });

        // Special validation for prediction form
        if (form.action.includes('predict')) {
            const fileInput = form.querySelector('input[type="file"]');
            if (fileInput && !fileInput.files.length) {
                showAlert('Please select an image file', 'error');
                isValid = false;
            }
        }

        return isValid;
    }

    function showFieldError(field, message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message text-danger mt-1';
        errorDiv.textContent = message;
        field.parentNode.appendChild(errorDiv);

        field.classList.add('is-invalid');
        field.addEventListener('input', function() {
            field.classList.remove('is-invalid');
            const errorMsg = field.parentNode.querySelector('.error-message');
            if (errorMsg) errorMsg.remove();
        }, { once: true });
    }

    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
}

// Navigation Effects
function initializeNavigationEffects() {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;

    let lastScrollTop = 0;
    const scrollThreshold = 100;

    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        // Add/remove scrolled class
        if (scrollTop > scrollThreshold) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }

        // Hide/show navbar on scroll
        if (scrollTop > lastScrollTop && scrollTop > scrollThreshold) {
            navbar.style.transform = 'translateY(-100%)';
        } else {
            navbar.style.transform = 'translateY(0)';
        }

        lastScrollTop = scrollTop;
    });

    // Add CSS for navbar effects
    const style = document.createElement('style');
    style.textContent = `
        .navbar {
            transition: all 0.3s ease;
        }
        .navbar-scrolled {
            background: rgba(40, 167, 69, 0.95) !important;
            backdrop-filter: blur(10px);
            box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
        }
    `;
    document.head.appendChild(style);

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Counter Animations
function initializeCounterAnimations() {
    const counters = document.querySelectorAll('.stat-item h3, .impact-stat h3');

    const animateCounter = (counter) => {
        const target = parseFloat(counter.textContent.replace(/[^0-9.]/g, ''));
        const suffix = counter.textContent.replace(/[0-9.]/g, '');
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;

        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }

            if (target >= 100) {
                counter.textContent = Math.floor(current) + suffix;
            } else {
                counter.textContent = current.toFixed(1) + suffix;
            }
        }, 16);
    };

    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => {
        counterObserver.observe(counter);
    });
}

// Initialize Tooltips
function initializeTooltips() {
    // Add tooltips to form elements
    const tooltipElements = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltipElements.forEach(element => {
        new bootstrap.Tooltip(element);
    });

    // Add helpful tooltips to certain elements
    const helpElements = [
        { selector: 'input[type="file"]', text: 'Supported formats: JPEG, PNG, WebP (Max 16MB)' },
        { selector: 'select[name="crop"]', text: 'Select the crop you want to analyze' }
    ];

    helpElements.forEach(item => {
        const elements = document.querySelectorAll(item.selector);
        elements.forEach(el => {
            el.setAttribute('title', item.text);
            el.setAttribute('data-bs-toggle', 'tooltip');
            el.setAttribute('data-bs-placement', 'top');
            new bootstrap.Tooltip(el);
        });
    });
}

// Loading State
function showLoadingState() {
    const submitBtn = document.getElementById('submitBtn');
    const loadingSpinner = document.getElementById('loadingSpinner');

    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Analyzing...';
    }

    if (loadingSpinner) {
        loadingSpinner.style.display = 'block';
        loadingSpinner.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

// Alert System
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type === 'error' ? 'danger' : type} alert-dismissible fade show position-fixed`;
    alertDiv.style.cssText = 'top: 100px; right: 20px; z-index: 9999; min-width: 300px;';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    document.body.appendChild(alertDiv);

    // Auto remove after 5 seconds
    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 5000);
}

// Image Lazy Loading
function initializeLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');

    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => {
        imageObserver.observe(img);
    });
}

// Performance Optimization
function optimizePerformance() {
    // Debounce scroll events
    let scrollTimeout;
    const originalScrollHandler = window.onscroll;

    window.onscroll = function() {
        if (scrollTimeout) {
            clearTimeout(scrollTimeout);
        }
        scrollTimeout = setTimeout(() => {
            if (originalScrollHandler) {
                originalScrollHandler();
            }
        }, 16);
    };

    // Preload critical images
    const criticalImages = [
        'https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80',
        'https://images.unsplash.com/photo-1586201375761-83865001e31c?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80'
    ];

    criticalImages.forEach(src => {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.as = 'image';
        link.href = src;
        document.head.appendChild(link);
    });
}

// Accessibility Enhancements
function enhanceAccessibility() {
    // Add skip to main content link
    const skipLink = document.createElement('a');
    skipLink.href = '#main-content';
    skipLink.textContent = 'Skip to main content';
    skipLink.className = 'sr-only sr-only-focusable position-absolute';
    skipLink.style.cssText = 'top: 10px; left: 10px; z-index: 10000; background: white; padding: 10px; border-radius: 5px;';
    document.body.insertBefore(skipLink, document.body.firstChild);

    // Add main content landmark
    const main = document.querySelector('main');
    if (main) {
        main.id = 'main-content';
    }

    // Enhance form labels
    const inputs = document.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
        if (!input.getAttribute('aria-label') && !input.id) {
            const label = input.closest('div').querySelector('label');
            if (label) {
                const id = 'input-' + Math.random().toString(36).substr(2, 9);
                input.id = id;
                label.setAttribute('for', id);
            }
        }
    });

    // Add focus indicators
    const style = document.createElement('style');
    style.textContent = `
        .sr-only {
            position: absolute !important;
            width: 1px !important;
            height: 1px !important;
            padding: 0 !important;
            margin: -1px !important;
            overflow: hidden !important;
            clip: rect(0, 0, 0, 0) !important;
            white-space: nowrap !important;
            border: 0 !important;
        }
        .sr-only-focusable:focus {
            position: static !important;
            width: auto !important;
            height: auto !important;
            padding: 0.5rem !important;
            margin: 0 !important;
            overflow: visible !important;
            clip: auto !important;
            white-space: normal !important;
        }
        *:focus {
            outline: 2px solid #28a745 !important;
            outline-offset: 2px !important;
        }
    `;
    document.head.appendChild(style);
}

// Initialize everything when page loads
document.addEventListener('DOMContentLoaded', function() {
    optimizePerformance();
    enhanceAccessibility();
    initializeLazyLoading();
});

// Service Worker Registration (for offline functionality)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/sw.js')
            .then(function(registration) {
                console.log('SW registered: ', registration);
            })
            .catch(function(registrationError) {
                console.log('SW registration failed: ', registrationError);
            });
    });
}

// Export functions for global use
window.AgriAid = {
    showAlert,
    removeImage: window.removeImage,
    showLoadingState
};
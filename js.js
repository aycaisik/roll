// Mobile Menu Toggle
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    hamburger.classList.toggle('active');
});

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
            // Close mobile menu if open
            navLinks.classList.remove('active');
        }
    });
});

// Navbar Background on Scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(0, 0, 0, 0.85)';
    } else {
        navbar.style.background = 'rgba(0, 0, 0, 0.6)';
    }
});

// Form Submit with Fetch API (Formspree example)
const form = document.getElementById('iletisim-formu');
const formStatus = document.getElementById('form-status');
const submitButton = document.getElementById('submit-button');

if(form) {
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Gönderim sırasında butonu kilitle ve bildirim göster
        const originalBtnText = submitButton.textContent;
        submitButton.textContent = 'Gönderiliyor...';
        submitButton.disabled = true;
        formStatus.style.display = 'none';

        const formData = new FormData(form);

        try {
            const response = await fetch(form.action, {
                method: form.method,
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            });

            if (response.ok) {
                formStatus.textContent = 'Mesajınız başarıyla gönderildi! Teşekkür ederiz.';
                formStatus.style.color = '#fff';
                formStatus.style.background = '#28a745';
                formStatus.style.padding = '10px 15px';
                formStatus.style.borderRadius = '8px';
                formStatus.style.display = 'block';
                form.reset();
            } else {
                const data = await response.json();
                if (Object.hasOwn(data, 'errors')) {
                    formStatus.textContent = data.errors.map(error => error.message).join(', ');
                } else {
                    formStatus.textContent = 'Eyvah! Form gönderilirken bir sorun oluştu.';
                }
                formStatus.style.color = '#fff';
                formStatus.style.background = '#dc3545';
                formStatus.style.padding = '10px 15px';
                formStatus.style.borderRadius = '8px';
                formStatus.style.display = 'block';
            }
        } catch (error) {
            // Eğer Formspree ID değiştirilmemişse veya ağ hatası var ise;
            formStatus.textContent = 'Gönderilemedi. Lütfen Formspree ID\'nizi girdikten sonra tekrar deneyin.';
            formStatus.style.color = '#fff';
            formStatus.style.background = '#dc3545';
            formStatus.style.padding = '10px 15px';
            formStatus.style.borderRadius = '8px';
            formStatus.style.display = 'block';
        } finally {
            submitButton.textContent = originalBtnText;
            submitButton.disabled = false;
            
            // Eğer başarılı olduysa durumu birkaç saniye sonra gizle
            setTimeout(() => {
                if(formStatus.style.background === 'rgb(40, 167, 69)' || formStatus.style.background === '#28a745') {
                    formStatus.style.display = 'none';
                }
            }, 6000);
        }
    });
}

// Add animation on scroll (Staggered Apple-style)
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    let delay = 0;
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            observer.unobserve(entry.target);
            setTimeout(() => {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }, delay);
            delay += 120; // Staggered delay of 120ms
        }
    });
}, observerOptions);

document.querySelectorAll('.service-card, .portfolio-item, .about-card, .sub-service-image, .sub-service-text, .contact-item').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(40px)';
    el.style.transition = 'opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1)';
    observer.observe(el);
});

// Count-up animation for stats
const statNumbers = document.querySelectorAll('.stat-number[data-target]');

function animateCount(el, { durationMs = 1200 } = {}) {
    const target = Number(el.dataset.target);
    if (!Number.isFinite(target)) return;
    if (el.dataset.animated === 'true') return;
    el.dataset.animated = 'true';

    const suffix = el.dataset.suffix ?? '';
    const formatter = new Intl.NumberFormat('tr-TR');
    const start = performance.now();

    function tick(now) {
        const t = Math.min(1, (now - start) / durationMs);
        const eased = 1 - Math.pow(1 - t, 3); // easeOutCubic
        const value = Math.round(target * eased);
        el.textContent = `${formatter.format(value)}${suffix}`;
        if (t < 1) requestAnimationFrame(tick);
    }

    requestAnimationFrame(tick);
}

if (statNumbers.length) {
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCount(entry.target);
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.4 });

    statNumbers.forEach(el => statsObserver.observe(el));
}

// Portfolio Modal & Slider Logic
const modal = document.getElementById('portfolioModal');
if (modal) {
    const modalImageContainer = document.getElementById('modalImageContainer');
    const modalTitle = document.getElementById('modalTitle');
    const modalDesc = document.getElementById('modalDesc');
    const closeBtn = document.querySelector('.modal-close');
    const scrollItems = document.querySelectorAll('.scroll-item, .gallery-item');
    
    let sliderInterval;

    scrollItems.forEach(item => {
        item.addEventListener('click', () => {
            const imgEl = item.querySelector('img');
            const title = item.getAttribute('data-title') || 'Proje Detayı';
            const desc = item.getAttribute('data-desc') || 'Bu etkinlik için mekanın ruhuna ve projenin konseptine uygun olarak Roll Event Lab tarafından yaratıcı teknik ve görsel çözümler tasarlanmıştır.';
            
            // Check for multiple images via data-images attr
            const dataImages = item.getAttribute('data-images');
            let images = [];
            
            if (dataImages) {
                images = dataImages.split(',').map(s => s.trim()).filter(s => s);
            } else {
                images = [imgEl.src];
            }

            modalTitle.textContent = title;
            modalDesc.textContent = desc;
            
            // Build Slider HTML
            let sliderHTML = `<div class="modal-slider"><div class="slider-track" id="sliderTrack">`;
            
            images.forEach(src => {
                sliderHTML += `<div class="slider-slide"><img src="${src}" alt="Slider Resim"></div>`;
            });
            
            sliderHTML += `</div>`;
            
            // Add Controls if there are multiple images
            if (images.length > 1) {
                sliderHTML += `
                    <button class="slider-btn prev" id="sliderPrev">&#10094;</button>
                    <button class="slider-btn next" id="sliderNext">&#10095;</button>
                    <div class="slider-dots" id="sliderDots">
                `;
                images.forEach((_, idx) => {
                    sliderHTML += `<div class="slider-dot ${idx === 0 ? 'active' : ''}" data-idx="${idx}"></div>`;
                });
                sliderHTML += `</div>`;
            }
            
            sliderHTML += `</div>`;
            modalImageContainer.innerHTML = sliderHTML;
            
            // Slider Interaction Logic
            if (images.length > 1) {
                const track = document.getElementById('sliderTrack');
                const btnPrev = document.getElementById('sliderPrev');
                const btnNext = document.getElementById('sliderNext');
                const dots = document.querySelectorAll('.slider-dot');
                
                let currentSlide = 0;
                
                const updateSlider = () => {
                    track.style.transform = `translateX(-${currentSlide * 100}%)`;
                    dots.forEach(dot => dot.classList.remove('active'));
                    if(dots[currentSlide]) dots[currentSlide].classList.add('active');
                };
                
                const nextSlide = () => {
                    currentSlide = (currentSlide + 1) % images.length;
                    updateSlider();
                };
                
                const prevSlide = () => {
                    currentSlide = (currentSlide - 1 + images.length) % images.length;
                    updateSlider();
                };
                
                btnNext.addEventListener('click', nextSlide);
                btnPrev.addEventListener('click', prevSlide);
                
                dots.forEach(dot => {
                    dot.addEventListener('click', (e) => {
                        currentSlide = parseInt(e.target.getAttribute('data-idx'));
                        updateSlider();
                        resetInterval();
                    });
                });
                
                // Auto Play Slider
                const startInterval = () => sliderInterval = setInterval(nextSlide, 3500);
                const resetInterval = () => { clearInterval(sliderInterval); startInterval(); };
                
                startInterval();
                
                // Pause slider on hover
                const modalSlider = document.querySelector('.modal-slider');
                modalSlider.addEventListener('mouseenter', () => clearInterval(sliderInterval));
                modalSlider.addEventListener('mouseleave', startInterval);
            }
            
            modal.classList.add('active');
        });
    });

    const closeModal = () => {
        modal.classList.remove('active');
        clearInterval(sliderInterval);
        setTimeout(() => {
            modalImageContainer.innerHTML = '';
        }, 400); // clear slider after fade out animation
    };

    closeBtn.addEventListener('click', closeModal);

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });
}

// ====== Portfolio Page Filtering Logic ======
const filterBtns = document.querySelectorAll('.filter-btn');
const galleryItems = document.querySelectorAll('.gallery-item');

if (filterBtns.length > 0 && galleryItems.length > 0) {
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            const filterValue = btn.getAttribute('data-filter');
            
            galleryItems.forEach(item => {
                const category = item.getAttribute('data-category');
                
                if (filterValue === 'all' || filterValue === category) {
                    item.classList.remove('hidden');
                    item.animate([
                        { opacity: 0, transform: 'scale(0.95)' },
                        { opacity: 1, transform: 'scale(1)' }
                    ], { duration: 400, fill: 'forwards', easing: 'ease' });
                } else {
                    item.classList.add('hidden');
                }
            });
        });
    });
}

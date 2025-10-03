// Form validation
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('preferencesForm');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            // Get all checked subjects
            const subjects = document.querySelectorAll('input[name="subjects"]:checked');
            
            // Get all checked difficulties
            const difficulties = document.querySelectorAll('input[name="difficulties"]:checked');
            
            // Validate subjects
            if (subjects.length === 0) {
                e.preventDefault();
                alert('Please select at least one subject');
                return false;
            }
            
            // Validate difficulties
            if (difficulties.length === 0) {
                e.preventDefault();
                alert('Please select at least one difficulty');
                return false;
            }
            
            // Validate age
            const age = document.getElementById('age');
            if (age && age.value) {
                const ageValue = parseInt(age.value);
                if (ageValue < 18 || ageValue > 30) {
                    e.preventDefault();
                    alert('Age must be between 18 and 30');
                    return false;
                }
            }
        });
    }
});

// Mobile sidebar toggle (for responsive design)
function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('open');
}

// Add smooth scroll behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Auto-hide alerts after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-20px)';
            setTimeout(() => {
                alert.style.display = 'none';
            }, 300);
        }, 5000);
    });
});
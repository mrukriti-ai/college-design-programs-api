// College App JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Navigation functionality
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.section');

    // Navigation click handlers
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remove active class from all links and sections
            navLinks.forEach(l => l.classList.remove('active'));
            sections.forEach(s => s.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
            
            // Show corresponding section
            const targetSection = this.getAttribute('data-section');
            document.getElementById(targetSection).classList.add('active');
        });
    });

    // Schedule navigation
    const prevWeekBtn = document.getElementById('prevWeek');
    const nextWeekBtn = document.getElementById('nextWeek');
    const weekDisplay = document.querySelector('.schedule-header h2');

    let currentWeek = new Date();
    
    prevWeekBtn.addEventListener('click', function() {
        currentWeek.setDate(currentWeek.getDate() - 7);
        updateWeekDisplay();
    });
    
    nextWeekBtn.addEventListener('click', function() {
        currentWeek.setDate(currentWeek.getDate() + 7);
        updateWeekDisplay();
    });

    function updateWeekDisplay() {
        const options = { 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric' 
        };
        const weekStart = new Date(currentWeek);
        weekStart.setDate(weekStart.getDate() - weekStart.getDay());
        weekDisplay.textContent = `Week of ${weekStart.toLocaleDateString('en-US', options)}`;
    }

    // Class slot click handlers
    const classSlots = document.querySelectorAll('.class-slot');
    classSlots.forEach(slot => {
        slot.addEventListener('click', function() {
            const course = this.getAttribute('data-course');
            showClassDetails(course);
        });
    });

    function showClassDetails(course) {
        // Create modal for class details
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close">&times;</span>
                <h2>${course} Details</h2>
                <div class="class-details">
                    <p><strong>Instructor:</strong> Professor Name</p>
                    <p><strong>Room:</strong> Room Number</p>
                    <p><strong>Time:</strong> Class Time</p>
                    <p><strong>Office Hours:</strong> Available Times</p>
                </div>
                <div class="modal-actions">
                    <button class="btn-primary">View Materials</button>
                    <button class="btn-secondary">Contact Professor</button>
                </div>
            </div>
        `;

        document.body.appendChild(modal);

        // Close modal functionality
        const closeBtn = modal.querySelector('.close');
        closeBtn.onclick = function() {
            modal.remove();
        };

        window.onclick = function(event) {
            if (event.target === modal) {
                modal.remove();
            }
        };
    }

    // Search functionality for library
    const searchInput = document.querySelector('.search-box input');
    const searchBtn = document.querySelector('.search-btn');
    const filterBtns = document.querySelectorAll('.filter-btn');

    searchBtn.addEventListener('click', performSearch);
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            performSearch();
        }
    });

    function performSearch() {
        const query = searchInput.value.trim();
        if (query) {
            // Simulate search results
            showSearchResults(query);
        }
    }

    function showSearchResults(query) {
        // Create search results modal
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close">&times;</span>
                <h2>Search Results for "${query}"</h2>
                <div class="search-results">
                    <div class="result-item">
                        <h3>Introduction to Computer Science</h3>
                        <p>Author: John Smith</p>
                        <p>Available in: Main Library</p>
                        <button class="btn-primary">Reserve</button>
                    </div>
                    <div class="result-item">
                        <h3>Advanced Mathematics</h3>
                        <p>Author: Jane Doe</p>
                        <p>Available in: Science Library</p>
                        <button class="btn-primary">Reserve</button>
                    </div>
                </div>
            </div>
        `;

        document.body.appendChild(modal);

        // Close modal functionality
        const closeBtn = modal.querySelector('.close');
        closeBtn.onclick = function() {
            modal.remove();
        };

        window.onclick = function(event) {
            if (event.target === modal) {
                modal.remove();
            }
        };
    }

    // Filter buttons for library
    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            // Add filter functionality here
        });
    });

    // Quick action buttons
    const actionBtns = document.querySelectorAll('.action-btn');
    actionBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const action = this.textContent.trim();
            handleQuickAction(action);
        });
    });

    function handleQuickAction(action) {
        switch(action) {
            case 'Register for Classes':
                showRegistrationModal();
                break;
            case 'View Transcript':
                showTranscriptModal();
                break;
            case 'Pay Tuition':
                showPaymentModal();
                break;
            case 'Get Help':
                showHelpModal();
                break;
        }
    }

    function showRegistrationModal() {
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close">&times;</span>
                <h2>Course Registration</h2>
                <div class="registration-form">
                    <div class="form-group">
                        <label>Select Course:</label>
                        <select>
                            <option>CS 201 - Data Structures</option>
                            <option>MATH 301 - Linear Algebra</option>
                            <option>PHYS 201 - Mechanics</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Select Section:</label>
                        <select>
                            <option>Section A - Mon/Wed 10:00 AM</option>
                            <option>Section B - Tue/Thu 2:00 PM</option>
                        </select>
                    </div>
                    <button class="btn-primary">Register</button>
                </div>
            </div>
        `;

        document.body.appendChild(modal);
        setupModalClose(modal);
    }

    function showTranscriptModal() {
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close">&times;</span>
                <h2>Academic Transcript</h2>
                <div class="transcript">
                    <div class="semester">
                        <h3>Fall 2024</h3>
                        <div class="course-grade">
                            <span>CS 101 - Computer Science</span>
                            <span>A-</span>
                        </div>
                        <div class="course-grade">
                            <span>MATH 201 - Calculus</span>
                            <span>B+</span>
                        </div>
                        <div class="course-grade">
                            <span>PHYS 101L - Physics Lab</span>
                            <span>A</span>
                        </div>
                    </div>
                    <div class="gpa-summary">
                        <h3>GPA: 3.8</h3>
                    </div>
                </div>
            </div>
        `;

        document.body.appendChild(modal);
        setupModalClose(modal);
    }

    function showPaymentModal() {
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close">&times;</span>
                <h2>Tuition Payment</h2>
                <div class="payment-info">
                    <div class="amount">
                        <h3>Amount Due: $15,000</h3>
                        <p>Due Date: October 15, 2024</p>
                    </div>
                    <div class="payment-methods">
                        <h4>Payment Methods:</h4>
                        <button class="btn-primary">Credit Card</button>
                        <button class="btn-secondary">Bank Transfer</button>
                        <button class="btn-secondary">Payment Plan</button>
                    </div>
                </div>
            </div>
        `;

        document.body.appendChild(modal);
        setupModalClose(modal);
    }

    function showHelpModal() {
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close">&times;</span>
                <h2>Need Help?</h2>
                <div class="help-options">
                    <div class="help-item">
                        <h4>Academic Advising</h4>
                        <p>Contact your academic advisor for course planning</p>
                        <button class="btn-primary">Schedule Meeting</button>
                    </div>
                    <div class="help-item">
                        <h4>Technical Support</h4>
                        <p>Get help with technical issues</p>
                        <button class="btn-primary">Submit Ticket</button>
                    </div>
                    <div class="help-item">
                        <h4>Student Services</h4>
                        <p>General student services and information</p>
                        <button class="btn-primary">Contact</button>
                    </div>
                </div>
            </div>
        `;

        document.body.appendChild(modal);
        setupModalClose(modal);
    }

    function setupModalClose(modal) {
        const closeBtn = modal.querySelector('.close');
        closeBtn.onclick = function() {
            modal.remove();
        };

        window.onclick = function(event) {
            if (event.target === modal) {
                modal.remove();
            }
        };
    }

    // Course card interactions
    const courseCards = document.querySelectorAll('.course-card');
    courseCards.forEach(card => {
        const viewMaterialsBtn = card.querySelector('.btn-primary');
        const assignmentsBtn = card.querySelector('.btn-secondary');

        viewMaterialsBtn.addEventListener('click', function() {
            const courseName = card.querySelector('h3').textContent;
            showCourseMaterials(courseName);
        });

        assignmentsBtn.addEventListener('click', function() {
            const courseName = card.querySelector('h3').textContent;
            showCourseAssignments(courseName);
        });
    });

    function showCourseMaterials(courseName) {
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close">&times;</span>
                <h2>${courseName} - Course Materials</h2>
                <div class="materials-list">
                    <div class="material-item">
                        <i class="fas fa-file-pdf"></i>
                        <span>Syllabus.pdf</span>
                        <button class="btn-secondary">Download</button>
                    </div>
                    <div class="material-item">
                        <i class="fas fa-file-powerpoint"></i>
                        <span>Lecture 1 - Introduction.pptx</span>
                        <button class="btn-secondary">Download</button>
                    </div>
                    <div class="material-item">
                        <i class="fas fa-file-word"></i>
                        <span>Assignment 1.docx</span>
                        <button class="btn-secondary">Download</button>
                    </div>
                </div>
            </div>
        `;

        document.body.appendChild(modal);
        setupModalClose(modal);
    }

    function showCourseAssignments(courseName) {
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close">&times;</span>
                <h2>${courseName} - Assignments</h2>
                <div class="assignments-list">
                    <div class="assignment-item">
                        <div class="assignment-info">
                            <h4>Assignment 1</h4>
                            <p>Due: September 20, 2024</p>
                            <p>Status: <span class="status pending">Pending</span></p>
                        </div>
                        <button class="btn-primary">Submit</button>
                    </div>
                    <div class="assignment-item">
                        <div class="assignment-info">
                            <h4>Assignment 2</h4>
                            <p>Due: September 27, 2024</p>
                            <p>Status: <span class="status not-started">Not Started</span></p>
                        </div>
                        <button class="btn-secondary">Start</button>
                    </div>
                </div>
            </div>
        `;

        document.body.appendChild(modal);
        setupModalClose(modal);
    }

    // Add CSS for modals
    const modalStyles = document.createElement('style');
    modalStyles.textContent = `
        .modal {
            display: block;
            position: fixed;
            z-index: 2000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.5);
            backdrop-filter: blur(5px);
        }

        .modal-content {
            background: white;
            margin: 5% auto;
            padding: 30px;
            border-radius: 16px;
            width: 90%;
            max-width: 600px;
            position: relative;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }

        .close {
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
            position: absolute;
            right: 20px;
            top: 15px;
        }

        .close:hover {
            color: #667eea;
        }

        .modal h2 {
            margin-bottom: 20px;
            color: #333;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: 500;
        }

        .form-group select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 8px;
        }

        .search-results {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .result-item {
            padding: 15px;
            border: 1px solid #eee;
            border-radius: 8px;
        }

        .result-item h3 {
            margin-bottom: 10px;
        }

        .transcript .semester {
            margin-bottom: 20px;
        }

        .course-grade {
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid #eee;
        }

        .help-options {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .help-item {
            padding: 15px;
            border: 1px solid #eee;
            border-radius: 8px;
        }

        .materials-list,
        .assignments-list {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .material-item,
        .assignment-item {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 15px;
            border: 1px solid #eee;
            border-radius: 8px;
        }

        .material-item i {
            color: #667eea;
            font-size: 20px;
        }

        .assignment-info {
            flex: 1;
        }

        .status {
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 0.8rem;
            font-weight: 600;
        }

        .status.pending {
            background: #fff3cd;
            color: #856404;
        }

        .status.not-started {
            background: #f8d7da;
            color: #721c24;
        }

        .payment-info {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .amount {
            text-align: center;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
        }

        .payment-methods {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
    `;
    document.head.appendChild(modalStyles);

    // Initialize the app
    updateWeekDisplay();
    
    // Add some interactive animations
    addHoverEffects();
});

function addHoverEffects() {
    // Add smooth hover effects to cards
    const cards = document.querySelectorAll('.stat-card, .course-card, .resource-card, .facility-card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
}

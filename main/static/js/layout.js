// Theme Switching Logic - Improved
const themes = {
    'theme-blue': 'fa-sun',
    'theme-dark': 'fa-moon',
    'theme-light': 'fa-lightbulb'
};

const themeOrder = ['theme-blue', 'theme-dark', 'theme-light'];
let currentTheme = localStorage.getItem('theme') || 'theme-blue';
const htmlEl = document.documentElement;
const themeBtn = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');

// Initialize theme
function setTheme(theme) {
    if (!themes[theme]) theme = 'theme-blue';
    htmlEl.className = theme;
    themeIcon.className = `fas ${themes[theme]}`;
    localStorage.setItem('theme', theme);
    currentTheme = theme;
}

setTheme(currentTheme);

// Theme toggle handler
themeBtn.addEventListener('click', () => {
    const currentIndex = themeOrder.indexOf(currentTheme);
    const nextIndex = (currentIndex + 1) % themeOrder.length;
    setTheme(themeOrder[nextIndex]);
});

// File Upload Logic - Improved with better error handling
const fileInput = document.getElementById('file-input');
const fileName = document.getElementById('file-name');
const dropArea = document.getElementById('drop-area');
const uploadBtn = document.getElementById('upload-btn');
const uploadProgress = document.getElementById('upload-progress');
const progressBar = document.getElementById('progress-bar');
const successMessage = document.getElementById('success-message');

// Improved file handling
function handleFiles(files) {
    if (!files || files.length === 0) {
        fileName.textContent = 'No files selected';
        fileName.classList.remove('has-file');
        uploadBtn.disabled = true;
        return;
    }

    // Validate files (example: check size or type)
    const validFiles = Array.from(files).filter(file => {
        return file.size < 10 * 1024 * 1024; // 10MB limit
    });

    if (validFiles.length === 0) {
        fileName.textContent = 'No valid files selected';
        fileName.classList.remove('has-file');
        uploadBtn.disabled = true;
        return;
    }

    // Create new DataTransfer to properly set files
    const dataTransfer = new DataTransfer();
    validFiles.forEach(file => dataTransfer.items.add(file));
    fileInput.files = dataTransfer.files;

    fileName.textContent = validFiles.length === 1
        ? validFiles[0].name
        : `${validFiles.length} files selected`;
    fileName.classList.add('has-file');
    uploadBtn.disabled = false;
}

// Enhanced drag and drop functionality
function setupDragAndDrop() {
    const dragEvents = ['dragenter', 'dragover', 'dragleave', 'drop'];

    const preventDefaults = (e) => {
        e.preventDefault();
        e.stopPropagation();
    };

    const highlight = () => {
        dropArea.classList.add('active');
        dropArea.setAttribute('aria-highlighted', 'true');
    };

    const unhighlight = () => {
        dropArea.classList.remove('active');
        dropArea.setAttribute('aria-highlighted', 'false');
    };

    dragEvents.forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults);
    });

    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight);
    });

    dropArea.addEventListener('drop', (e) => {
        const files = e.dataTransfer.files;
        handleFiles(files);
    });

    // Click to select files
    dropArea.addEventListener('click', () => {
        fileInput.click();
    });
}

// Improved upload simulation
function setupUpload() {
    fileInput.addEventListener('change', () => handleFiles(fileInput.files));

    uploadBtn.addEventListener('click', async () => {
        if (!fileInput.files || fileInput.files.length === 0) return;

        uploadBtn.disabled = true;
        uploadProgress.style.display = 'block';
        successMessage.style.display = 'none';

        try {
            // Simulate upload progress
            await simulateUpload();
            uploadComplete();
        } catch (error) {
            console.error('Upload failed:', error);
            fileName.textContent = 'Upload failed';
            uploadBtn.disabled = false;
            uploadProgress.style.display = 'none';
        }
    });
}

function simulateUpload() {
    return new Promise((resolve) => {
        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.random() * 10;
            if (progress >= 100) {
                progress = 100;
                clearInterval(interval);
                resolve();
            }
            progressBar.style.width = `${progress}%`;
        }, 200);
    });
}

function uploadComplete() {
    successMessage.style.display = 'flex';
    uploadBtn.disabled = false;

    setTimeout(() => {
        progressBar.style.width = '0';
        uploadProgress.style.display = 'none';
        // Don't clear selection automatically
    }, 3000);
}

// Initialize everything
document.addEventListener('DOMContentLoaded', () => {
    setupDragAndDrop();
    setupUpload();
});
// footer
// Add this to your layout.js
document.getElementById('current-year').textContent = new Date().getFullYear();
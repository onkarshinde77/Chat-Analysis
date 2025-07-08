const themes = ['theme-blue', 'theme-dark', 'theme-light'];
const icons = ['fa-sun', 'fa-moon', 'fa-lightbulb'];
const htmlEl = document.documentElement;
const themeBtn = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');
let currentTheme = localStorage.getItem('theme') || 'theme-blue';
let currentIdx = themes.indexOf(currentTheme);
if (currentIdx === -1) currentIdx = 0;
htmlEl.className = themes[currentIdx];
themeIcon.className = `fas ${icons[currentIdx]}`;

themeBtn.addEventListener('click', () => {
    currentIdx = (currentIdx + 1) % themes.length;
    htmlEl.className = themes[currentIdx];
    themeIcon.className = `fas ${icons[currentIdx]}`;
    localStorage.setItem('theme', themes[currentIdx]);
});

// File upload logic
const fileInput = document.getElementById('file-input');
const fileName = document.getElementById('file-name');
const dropArea = document.getElementById('drop-area');
const uploadBtn = document.getElementById('upload-btn');
const uploadProgress = document.getElementById('upload-progress');
const progressBar = document.getElementById('progress-bar');
const successMessage = document.getElementById('success-message');

// Handle file selection
fileInput.addEventListener('change', handleFiles);

function handleFiles() {
    const files = fileInput.files;
    if (files.length > 0) {
        fileName.textContent = files.length === 1 ? files[0].name : `${files.length} files selected`;
        fileName.classList.add('has-file');
        uploadBtn.disabled = false;
    } else {
        fileName.textContent = 'No files selected';
        fileName.classList.remove('has-file');
        uploadBtn.disabled = true;
    }
}

// Drag and drop functionality
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false);
});

['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false);
});

function highlight() {
    dropArea.classList.add('active');
}

function unhighlight() {
    dropArea.classList.remove('active');
}

dropArea.addEventListener('drop', handleDrop, false);

function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;
    fileInput.files = files;
    handleFiles();
}

// Upload simulation
uploadBtn.addEventListener('click', () => {
    if (fileInput.files.length === 0) return;

    uploadBtn.disabled = true;
    uploadProgress.style.display = 'block';
    successMessage.style.display = 'none';

    // Simulate upload progress
    let progress = 0;
    const interval = setInterval(() => {
        progress += Math.random() * 10;
        if (progress >= 100) {
            progress = 100;
            clearInterval(interval);
            uploadComplete();
        }
        progressBar.style.width = `${progress}%`;
    }, 200);
});

function uploadComplete() {
    successMessage.style.display = 'flex';
    uploadBtn.disabled = false;

    // Reset after 3 seconds
    setTimeout(() => {
        progressBar.style.width = '0';
        uploadProgress.style.display = 'none';
    }, 3000);
}

// Click drop area to trigger file input
dropArea.addEventListener('click', () => {
    fileInput.click();
});
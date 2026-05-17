const form = document.getElementById("resume-form");
const jobDescription = document.getElementById("job-description");
const resumeFile = document.getElementById("resume-file");
const results = document.getElementById("results");

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const jobtext = jobDescription.value.trim();
    const file = resumeFile.files[0];

    if (!jobtext) {
        results.textContent = "Please enter a job description.";
        return;
    }

    if (!file) {
        results.textContent = "Please upload a PDF resume.";
        return;
    }

    results.textContent = `Evaluating ${file.name} against the job description... (AI integration coming soon)`;

});


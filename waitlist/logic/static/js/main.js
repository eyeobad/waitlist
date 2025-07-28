document.addEventListener('DOMContentLoaded', () => {
    // --- REAL-TIME MASCOT LOGIC ---
    const schoolData = JSON.parse(document.getElementById('school-data').textContent);
    const emailInput = document.getElementById('email-input');
    const submitButton = document.getElementById('submit-button');
    const buttonLogoContainer = document.getElementById('button-logo-container');

    emailInput.addEventListener('input', (event) => {
        const email = event.target.value.toLowerCase();
        const domainMatch = email.match(/@(.*)/);
        let schoolFound = false;
        if (domainMatch && domainMatch[1]) {
            const domain = domainMatch[1];
            if (schoolData[domain]) {
                const school = schoolData[domain];
                buttonLogoContainer.innerHTML = `<img src="/static/${school.logo}" alt="${school.name} logo">`;
                submitButton.classList.add('has-logo');
                schoolFound = true;
            }
        }
        if (!schoolFound) {
            submitButton.classList.remove('has-logo');
            setTimeout(() => {
                if (!submitButton.classList.contains('has-logo')) {
                    buttonLogoContainer.innerHTML = '';
                }
            }, 300);
        }
    });

    
});

document.addEventListener('DOMContentLoaded', () => {
    const copyButton = document.getElementById('copy-button');
    const referralLinkInput = document.getElementById('referral-link');
    const copyIcon = document.getElementById('copy-icon');
    const checkIcon = document.getElementById('check-icon');

    copyButton.addEventListener('click', () => {
        // Select the text
        referralLinkInput.select();
        referralLinkInput.setSelectionRange(0, 99999); // For mobile devices

        // Copy the text to the clipboard
        navigator.clipboard.writeText(referralLinkInput.value).then(() => {
            // Success feedback
            copyIcon.classList.add('hidden');
            checkIcon.classList.remove('hidden');

            // Revert back to the copy icon after 2 seconds
            setTimeout(() => {
                copyIcon.classList.remove('hidden');
                checkIcon.classList.add('hidden');
            }, 2000);
        }).catch(err => {
            console.error('Failed to copy text: ', err);
        });
    });
});

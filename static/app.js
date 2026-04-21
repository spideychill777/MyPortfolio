/*Code used to make the form useful.*/
document.getElementById('contact-form').addEventListener('submit', function(event){
    event.preventDefault();

    const submitButton = this.querySelector('button[type="submit"]');
    submitButton.classList.add('loading');

    const formData = new FormData(this);

    fetch('/send_email', {
        method: 'POST',
        body: formData
    })
    .then(Response => Response.text())
    .then(data => {
        showFlashMessage('Mensaje enviado correctamente.', 'success');
        this.reset(); // Clean the form
        submitButton.classList.remove('loading');
    })
    .catch(error => {
        showFlashMessage('There was an error sending the message.', 'danger');
       console.error('Error:', error);
       submitButton.classList.remove('loading'); 
    });
});

function showFlashMessage(message, category) {
    const flashContainer = document.getElementById('flash-messages');
    const showFlashMessage = document.createElement('div');
    showFlashMessage.className = `alert ${category}`;
    showFlashMessage.textContent = message;

    flashContainer.appendChild(flashMessage);


    setTimeout(() => {
        flashMessage.remove();
    }, 5000);
}

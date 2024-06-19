document.addEventListener('htmx:afterOnLoad', function (evt) {
    var modal = document.getElementById('flat-modal');
    var modalInstance = new bootstrap.Modal(modal);
    modalInstance.show();

    // Update the modal title based on the content loaded
    var titleElement = modal.querySelector('.modal-title');
    var newTitle = evt.detail.elt.querySelector('.modal-title');
    if (newTitle) {
        titleElement.innerHTML = newTitle.innerHTML;
    }
});

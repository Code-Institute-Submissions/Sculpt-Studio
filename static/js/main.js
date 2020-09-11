//get Id for programs in cart //

document.querySelectorAll('.remove').forEach(e => {
    e.addEventListener('click', function() {
        let getId = this.id.split('program_')[1];
        let url = window.location.href + 'remove_from_cart/' + `${getId}`;
        window.location.href = url;
    })
});
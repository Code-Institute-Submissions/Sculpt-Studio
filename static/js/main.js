//get Id for programs in cart //

document.querySelector('.remove').addEventListener('click', function() {
    let getId = document.querySelector('.remove').id.split('program_')[1];
    let url = window.location.href + 'remove_from_cart/' + `${getId}`;
    window.location.href = url;
})
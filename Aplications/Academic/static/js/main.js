(function () {

    const btnDelete = document.querySelectorAll(".btn-Delete");

    btnDelete.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmation = confirm('Are you sure you want to eliminate this?');
            if (!confirmation) {
                e.preventDefault();
            }
        });
    });
    
})();

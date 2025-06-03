document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const table = document.getElementById('moviesTable');
    const rows = table.querySelectorAll('tbody tr'); // Získá pouze řádky s daty

    searchInput.addEventListener('input', function() {
        const searchText = this.value.toLowerCase();
        
        rows.forEach(row => {
            const cells = row.querySelectorAll('td');
            let rowContainsText = false;
            
            // Projdeme všechny buňky v řádku
            cells.forEach(cell => {
                const cellText = cell.textContent.toLowerCase();
                if (cellText.includes(searchText)) {
                    rowContainsText = true;
                }
            });
            
            // Zobrazíme/skryjeme řádek podle shody
            row.style.display = rowContainsText ? '' : 'none';
        });
    });
});
document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('searchInput').addEventListener('keyup', filterTable);
});

function filterTable() {
    const searchInput = document.getElementById('searchInput');
    const filter = searchInput.value.toLowerCase();
    const table = document.getElementById('Table');
    const tr = table.getElementsByTagName('tr');
    for (let i = 1; i < tr.length; i++) { // Start from 1 to skip the header row
        let tdArray = tr[i].getElementsByTagName('td');
        let isVisible = false;
        for (let j = 0; j < tdArray.length; j++) {
            let td = tdArray[j];
            if (td) {
                if (td.textContent.toLowerCase().indexOf(filter) > -1) {
                    isVisible = true;
                    break;
                }
            }
        }
        if (isVisible) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
    }
}
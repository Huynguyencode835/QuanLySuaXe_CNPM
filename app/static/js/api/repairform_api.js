document.getElementById('repair-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(this);

    fetch('/api/repairform/create', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        sessionStorage.setItem("toast_message", data.message);
        sessionStorage.setItem("toast_category", data.category);
        window.location.reload();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Có lỗi xảy ra khi lưu dữ liệu!');
    });
});
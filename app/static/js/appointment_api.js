function checkLimitVehicle() {
    fetch('/api/appointment/limit', {
        method: 'GET'
    })
    .then(res => res.json())
    .then(data => {
        if(data.isReached){
            window.location.href = '/appointment';
        }else{
            alert("Hôm nay đã đủ số lượng xe tiếp nhận!");
        }
    });
    return false;
}

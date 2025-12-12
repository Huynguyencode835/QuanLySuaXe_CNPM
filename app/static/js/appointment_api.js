let isDataLoaded = false;

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
}

function fillInfor() {
    if(!isDataLoaded){
        fetch('/api/appointment/info', {
            method: 'GET'
        })
        .then(res => res.json())
        .then(data => {
            document.querySelector(".fill-info-name").value = data.name;
            document.querySelector(".fill-info-phonenumber").value = data.phonenumber;
            isDataLoaded = true;
        });
    }
}
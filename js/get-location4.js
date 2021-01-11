
function showLocation(data) {
    console.log(data)
    let latitude = document.getElementById("latitude");
    let longitude = document.getElementById("longitude");
    
    if(data.status == 0){
        latitude.value = data.result.location.lat;
        longitude.value = data.result.location.lng;
    }else{
        console.log("地点输入错误");
    }
}

window.onload = function () {

    let province = document.getElementById("province");
    let city = document.getElementById("city");
    let district = document.getElementById("district");
    
    
    
    district.onblur = function () {
        let addr = province.value + city.value + district.value;
        console.log(addr);
        let oScript = document.createElement("script");
        oScript.src =
            `http://api.map.baidu.com/geocoding/v3/?address=${addr}&output=json&ak=i2cwYYn9hDPSELZilNBGthOqQ9wtpYDe&callback=showLocation`;
        document.body.appendChild(oScript);
    }

}

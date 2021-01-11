            /* 
                method
                url
                data
                success  数据下载成功以后执行的函数
                error    数据下载失败以后执行的函数
             */
            function $ajax({method = "get", url, data, success, error}){
                //1、创建ajax对象
                var xhr = null;
                try{
                    xhr = new XMLHttpRequest();
                }catch(error){
                    xhr = new ActiveXObject("Microsoft.XMLHTTP");
                }

                //判断如果数据存在
                if(data){
                    data = querystring(data);
                }

                if(method == "get" && data){
                    url += "?" + data;
                }

                xhr.open(method, url, true);

                if(method == "get"){
                    xhr.send();
                }else{
                    //必须在send方法之前，去设置请求的格式
                    xhr.setRequestHeader("content-type", "application/x-www-form-urlencoded");
                    xhr.send(data);
                }
                 //4、等待数据响应  
                xhr.onreadystatechange = function(){
                    if(xhr.readyState == 4){
                        //判断本次下载的状态码都是多少
                        if(xhr.status == 200){
                            /* 
                                如何去处理数据操作不确定
                                回调函数
                            */
                            if(success){
                                // alert(2);
                                success(xhr.responseText);
                            }
                        }else{
                            if(error){
                                error("Error:" + xhr.status);
                            }
                        }
                    }
                }
            }

            function querystring(obj){
                var str = "";
                for(var attr in obj){
                    str += attr + "=" + obj[attr] + "&";
                }
                return str.substring(0, str.length - 1);
            }

/**
 * 现在所有错误已经改过来了-_-
 * ajax.js:33 
 * POST http://localhost:8888/php/register.php 405 
 * (Method Not Allowed)
 * 这个应该是跨域问题
 * 数据库的端口号是80
 * gulp创建的临时服务器的端口是8888
 * 现在我把文件移到，80端口的服务器下
 */
 
function showLocation(data) {
    console.log(data)
    let latitude = document.getElementById("latitude");
    let longitude = document.getElementById("longitude");
    
    if(data.status == 0){
        latitude.value = data.result.location.lat.toFixed(6);//四舍五入保留6位小数
        longitude.value = data.result.location.lng.toFixed(6);
    }else{
        console.log("地点输入错误");
    }
}
window.onload = function () {
    console.log("正常");
    var oinputs = document.getElementsByTagName("input");
    var btn = document.getElementById("btn");

    btn.onclick = function () {
        //做个简单的验证，输入内容不能为空
        var time = new Date();
        var ale = document.getElementById("alert");
        if (!oinputs[0].value || !oinputs[1].value || !oinputs[2].value ||!oinputs[3].value || !oinputs[4].value || !oinputs[5].value || !oinputs[6].value || !oinputs[7].value || !oinputs[8].value) {
            alert("输入内容不能为空哦");
        } else {
            // method = "get", url, data, success, error
            // alert(121);
            $ajax({
                method : "post",
                url : "./php/submit.php",
                data : {
                    name : oinputs[0].value,
                    token : oinputs[1].value,
                    email : oinputs[2].value,
                    latitude : oinputs[7].value,
                    longitude : oinputs[8].value,
                    country : oinputs[3].value,
                    city : oinputs[5].value,
                    district : oinputs[6].value,
                    province : oinputs[4].value,
                    township : oinputs[9].value,
                    street : oinputs[10].value,
                    create_time : time.getTime()//获取到毫秒数
                },
                success : function(result){
                    var res = JSON.parse(result);
                    //alert(res)
                    console.log(res);
                    //alert(res);
                    if(res.code == 2){
                        ale.className = "alert-success";
                        ale.innerHTML = res.message;
                        //ale.style.display = "block";
                    }else{
                        ale.className = "alert-warning";
                        ale.innerHTML = res.message;
                        //ale.style.display = "block";
                    }
                },
                error : function(msg){
                    //alert(res)
                    console.log(msg);
                }
            });
        }
    }
    
    //自动获取经纬度
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
    city.onblur = function () {
        let addr = province.value + city.value + district.value;
        console.log(addr);
        let oScript = document.createElement("script");
        oScript.src =
            `http://api.map.baidu.com/geocoding/v3/?address=${addr}&output=json&ak=i2cwYYn9hDPSELZilNBGthOqQ9wtpYDe&callback=showLocation`;
        document.body.appendChild(oScript);
    }
    province.onblur = function () {
        let addr = province.value + city.value + district.value;
        console.log(addr);
        let oScript = document.createElement("script");
        oScript.src =
            `http://api.map.baidu.com/geocoding/v3/?address=${addr}&output=json&ak=i2cwYYn9hDPSELZilNBGthOqQ9wtpYDe&callback=showLocation`;
        document.body.appendChild(oScript);
    }
}
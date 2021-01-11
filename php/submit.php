<?php

header('content-type:text/html;charset="utf-8"');

$name = $_POST['name'];
$token = $_POST['token'];
$email = $_POST['email'];
$latitude = $_POST['latitude'];
$longitude = $_POST['longitude'];
$country = $_POST['country'];
$city = $_POST['city'];
$district = $_POST['district'];
$province = $_POST['province'];
$township = $_POST['township'];
$street = $_POST['street'];
$create_time = $_POST['create_time'];



$servername = "localhost";
$username = "root";
$password = "jia599599";
$dbname = "book";
 
 // $responddata = ["code"=>"","message"=>""];
$responddata = array("code"=>"","message"=>"");

// 创建链接
$conn = mysqli_connect($servername, $username, $password, $dbname);
// 检测连接
if (!$conn) {
    $responddata['code'] = 0;
    $responddata['message'] = "数据库链接失败";
    echo json_encode($responddata);
    exit;
}




$sql = "SELECT * FROM stu_info WHERE name='{$name}'";
$res = mysqli_query($conn, $sql);

if(mysqli_num_rows($res) > 0){
    $responddata['code'] = 1;
    $responddata['message'] = "用户名重复";
    echo json_encode($responddata);
    exit;
}


$sql1 = "INSERT INTO stu_info(name,token,email,create_time) VALUES('{$name}','{$token}','{$email}','{$create_time}')";

$sql2 = "INSERT INTO stu_position(email,latitude,longitude,country,city,district,province,township,street) VALUES('{$email}','{$latitude}','{$longitude}','{$country}','{$city}','{$district}','{$province}','{$township}','{$street}')";


if (mysqli_query($conn, $sql1) && mysqli_query($conn, $sql2)) {
    $responddata['code'] = 2;
    $responddata['message'] = "信息添加成功";
    echo json_encode($responddata);
    exit;
} else {
    $responddata['code'] = 3;
    $responddata['message'] = "信息添加失败";
    echo json_encode($responddata);
}
 
mysqli_close($conn);

?>
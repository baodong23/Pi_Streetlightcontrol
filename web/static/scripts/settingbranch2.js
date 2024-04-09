$(document).ready(function (){
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    var ip="0";
    socket.on('connect', function () {
        console.log("WS connected");
        sessionStorage.setItem("errorcode", '0');
        var js = { cmd: "refresh" };
        js.data = "refreshsetting2";
        var a = JSON.stringify(js);
        socket.send(a);
    });
    socket.on('disconnect', function () {
        console.log("WS disconnected.");
    });
    socket.on('ip',function(ip_address){
        ip = ip_address;
        console.log(ip);
        console.log(localStorage.getItem("IP"))
    });
    socket.on('error',function(error){
        if(ip == localStorage.getItem("IP")){
            if (error === "1"){
                $("#loss").modal('show');
            }
        }
    });
    socket.on('get_connect', function(msg){
        var a = $.parseJSON(msg);
        console.log(a);
        if(a.connect_PLC === '1'){
            $("#connectplc").modal('show')
        }
    });
    socket.on('errorcode',function(error){
        if(ip == localStorage.getItem("IP")){
          if (error !== '0' && sessionStorage.getItem('errorcode') === '0'){
            sessionStorage.setItem("errorcode", '1');
            $("#over-alarm").modal('show');
          }
          else if (error === '0'){
            sessionStorage.setItem("errorcode", '0');
          }
        }
    });
    socket.on('timecontrol2', function(msg){
        if(ip == localStorage.getItem("IP")){
            var a = $.parseJSON(msg);
            $("#starttime1-branch2").val(a.starttime2_1);
            $("#stoptime1-branch2").val(a.stoptime2_1);
            $("#u1-branch2max").val(a.u2_1max);
            $("#i1-branch2max").val(a.i2_1max);
            $("#starttime2-branch2").val(a.starttime2_2);
            $("#stoptime2-branch2").val(a.stoptime2_2);
            $("#u2-branch2max").val(a.u2_2max);
            $("#i2-branch2max").val(a.i2_2max);
            $("#starttime3-branch2").val(a.starttime2_3);
            $("#stoptime3-branch2").val(a.stoptime2_3);
            $("#u3-branch2max").val(a.u2_3max);
            $("#i3-branch2max").val(a.i2_3max);
            $("#starttime4-branch2").val(a.starttime2_4);
            $("#stoptime4-branch2").val(a.stoptime2_4);
            $("#u4-branch2max").val(a.u2_4max);
            $("#i4-branch2max").val(a.i2_4max);
        }
    });
    $("#u1-branch2max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui2-max"};
            js.data = ["u2_1max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#u2-branch2max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui2-max"};
            js.data = ["u2_2max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#u3-branch2max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui2-max"};
            js.data = ["u2_3max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#u4-branch2max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui2-max"};
            js.data = ["u2_4max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#i1-branch2max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui2-max"};
            js.data = ["i2_1max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#i2-branch2max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui2-max"};
            js.data = ["i2_2max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#i3-branch2max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui2-max"};
            js.data = ["i2_3max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#i4-branch2max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui2-max"};
            js.data = ["i2_4max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    //Setting Branch2 start
    $("#starttime1-branch2").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch2"};
            js.data = ["starttime1-branch2", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#stoptime1-branch2").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch2"};
            js.data = ["stoptime1-branch2", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
  ////////

    $("#starttime2-branch2").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch2"};
            js.data = ["starttime2-branch2", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#stoptime2-branch2").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch2"};
            js.data = ["stoptime2-branch2", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
  ////////

    $("#starttime3-branch2").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch2"};
            js.data = ["starttime3-branch2", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#stoptime3-branch2").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch2"};
            js.data = ["stoptime3-branch2", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
  ////////
  
    $("#starttime4-branch2").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch2"};
            js.data = ["starttime4-branch2", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#stoptime4-branch2").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch2"};
            js.data = ["stoptime4-branch2", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
  //Setting Branch2 finish
    $("#delete2").click(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "delete"};
            js.data = "delete2";
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });

    $("#copybranch2_1").click(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "copy2"};
            js.data = "copy2_1";
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#copybranch2_3").click(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "copy2"};
            js.data = "copy2_3";
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#copybranch2_4").click(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "copy2"};
            js.data = "copy2_4";
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#ds").click(function(){
        if(ip == localStorage.getItem("IP")){
          var js = {cmd: "plc"};
          var a = JSON.stringify(js);
          socket.send(a);
        }
      })
    $("#re").click(function(){
    if(ip == localStorage.getItem("IP")){
        var js = {cmd: "replc"};
        var a = JSON.stringify(js);
        socket.send(a);
    }
    })
    $(function () {
        if(ip == localStorage.getItem("IP")){
            var a = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11",
                    "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"];
            for (var i = 0; i < a.length; i++) {
                $("#starthour1-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stophour1-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#starthour2-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stophour2-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#starthour3-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stophour3-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#starthour4-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stophour4-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
            }
        }
    });
    $(function () {
        if(ip == localStorage.getItem("IP")){
            var a = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11",
                    "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
                    "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35",
                    "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47",
                    "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"];
            for (var i = 0; i < a.length; i++) {
                $("#startminute1-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stopminute1-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#startminute2-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stopminute2-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#startminute3-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stopminute3-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#startminute4-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stopminute4-branch2").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
            }
        }
    });
});
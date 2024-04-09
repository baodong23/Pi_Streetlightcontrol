$(document).ready(function (){
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    var ip="0";

    socket.on('connect', function () {
        console.log("WS connected");
        sessionStorage.setItem("errorcode", '0');
        var js = { cmd: "refresh" };
        js.data = "refreshsetting1";
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
        if(ip == localStorage.getItem("IP")){
            var a = $.parseJSON(msg);
            console.log(a);
            if(a.connect_PLC === '1'){
                $("#connectplc").modal('show')
            }
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
    socket.on('timecontrol1', function(msg){
        if(ip == localStorage.getItem("IP")){
            var a = $.parseJSON(msg);
            $("#starttime1-branch1").val(a.starttime1_1);
            $("#stoptime1-branch1").val(a.stoptime1_1);
            $("#u1-branch1max").val(a.u1_1max);
            $("#i1-branch1max").val(a.i1_1max);
            $("#starttime2-branch1").val(a.starttime1_2);
            $("#stoptime2-branch1").val(a.stoptime1_2);
            $("#u2-branch1max").val(a.u1_2max);
            $("#i2-branch1max").val(a.i1_2max);
            $("#starttime3-branch1").val(a.starttime1_3);
            $("#stoptime3-branch1").val(a.stoptime1_3);
            $("#u3-branch1max").val(a.u1_3max);
            $("#i3-branch1max").val(a.i1_3max);
            $("#starttime4-branch1").val(a.starttime1_4);
            $("#stoptime4-branch1").val(a.stoptime1_4);
            $("#u4-branch1max").val(a.u1_4max);
            $("#i4-branch1max").val(a.i1_4max);
        }
    });

    $("#u1-branch1max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui1-max"};
            js.data = ["u1_1max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#u2-branch1max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui1-max"};
            js.data = ["u1_2max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#u3-branch1max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui1-max"};
            js.data = ["u1_3max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#u4-branch1max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui1-max"};
            js.data = ["u1_4max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#i1-branch1max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui1-max"};
            js.data = ["i1_1max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#i2-branch1max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui1-max"};
            js.data = ["i1_2max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#i3-branch1max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui1-max"};
            js.data = ["i1_3max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#i4-branch1max").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "ui1-max"};
            js.data = ["i1_4max", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    
    $("#starttime1-branch1").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch1"};
            js.data = ["starttime1-branch1", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#stoptime1-branch1").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch1"};
            js.data = ["stoptime1-branch1", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
      ////////
    
    $("#starttime2-branch1").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch1"};
            js.data = ["starttime2-branch1", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#stoptime2-branch1").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch1"};
            js.data = ["stoptime2-branch1", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
      ////////
    
    $("#starttime3-branch1").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch1"};
            js.data = ["starttime3-branch1", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#stoptime3-branch1").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch1"};
            js.data = ["stoptime3-branch1", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
      ////////
    
    $("#starttime4-branch1").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch1"};
            js.data = ["starttime4-branch1", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#stoptime4-branch1").change(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "settingbranch1"};
            js.data = ["stoptime4-branch1", $(this).val()];
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    //Setting Branch1 finish
    
    $("#delete1").click(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "delete"};
            js.data = "delete1";
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });

    $("#copybranch1_2").click(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "copy1"};
            js.data = "copy1_2";
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#copybranch1_3").click(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "copy1"};
            js.data = "copy1_3";
            var a = JSON.stringify(js);
            socket.send(a);
        }
    });
    $("#copybranch1_4").click(function(){
        if(ip == localStorage.getItem("IP")){
            var js = {cmd : "copy1"};
            js.data = "copy1_4";
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
                $("#starthour1-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stophour1-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#starthour2-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stophour2-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#starthour3-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stophour3-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#starthour4-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stophour4-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
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
                $("#startminute1-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stopminute1-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#startminute2-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stopminute2-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#startminute3-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stopminute3-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#startminute4-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
                $("#stopminute4-branch1").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
            }
        }
    });

});
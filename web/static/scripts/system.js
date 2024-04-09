$(document).ready(function (){

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    var ip = "0";
    socket.on('connect', function () {
        console.log("connected");
        var js = { cmd: "refresh" };
        js.data = "refreshsystem";
        var a = JSON.stringify(js);
        socket.send(a);
      });
    
    socket.on('disconnect', function () {
        console.log("disconnected.");
    });

    socket.on('ip',function(ip_address){
        ip = ip_address;
        console.log(ip);
        console.log(localStorage.getItem("IP"));
    });
    socket.on('get_connect', function(msg){
        var a = $.parseJSON(msg);
        console.log(a);
        if(a.connect_PLC === '1'){
            $("#connectplc").modal('show')
        }
        else if(a.connect_PLC === '0'){
            $("#disconnectplc").modal('show')
        }
    });
    socket.on('login', function(msg){
        var a = $.parseJSON(msg);
        $("#loginsuccess").modal('show');
        if (sessionStorage.getItem("ID") === "1"){ 
            localStorage.setItem("IP", a.login);
            sessionStorage.setItem("ID",0);
            sessionStorage.setItem("errorcode", '0');
        }
        if($("#person").hasClass('fa-user')){
            $("#person").removeClass('fa-user');
            $("#person").addClass('fa-user-check success');
        }
    });
    socket.on('loginok', function(msg){
        if(ip == localStorage.getItem("IP")){
            if (msg === "1"){
                if($("#person").hasClass('fa-user')){
                    $("#person").removeClass('fa-user');
                    $("#person").addClass('fa-user-check success');
                }
            }
        }
    });
    $("#login").click(function(){
        var js = {cmd: "login"};
        js.data = {};
        js.data.user = $("#user").val();
        js.data.pass = $("#pass").val();
        sessionStorage.setItem("ID",1);
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $(function(){
        var a = ["admin", "operator"];
        for(i=0 ; i<a.length ;i++){
            $("#user").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
        }
    });
    $(function () {
        $('#eye').click(function () {
          if ($(this).hasClass('fa-eye-slash')) {
            $(this).removeClass('fa-eye-slash');
            $(this).addClass('fa-eye');
            $('#pass').attr('type', 'text');
          } else {
            $(this).removeClass('fa-eye');
            $(this).addClass('fa-eye-slash');
            $('#pass').attr('type', 'password');
          }
        });
    });
    $("#logout").click(function(){
        $("#savelogout").modal('show');
    });
    $("#logoutok").click(function(){
        sessionStorage.setItem("errorcode", '0');
        if($("#person").hasClass('fa-user-check success')){
            $("#person").removeClass('fa-user-check success');
            $("#person").addClass('fa-user');
        }
        var js = {cmd: "logout"};
        var a = JSON.stringify(js);
        sessionStorage.setItem("ID",0)
        socket.send(a);
    });
    $("#dis").click(function(){
        var js = {cmd: "plc"};
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $("#rec").click(function(){
        var js = {cmd: "replc"};
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $("#connect").click(function(){
        var js = {cmd: "option"};
        js.data = [parseInt($("#option").val()), $("#plcip").val(), $("#piip").val(), $("#serverip").val(), $("#dns").val()];
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $(function(){
            var a = ["S7-1200 CPU1211", "Logo 230RCE"];
            for(i=0 ; i<a.length ;i++){
                $("#option").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
        }
    });
});
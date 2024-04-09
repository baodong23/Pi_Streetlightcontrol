$(document).ready(function(){
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    var ip="0";
    
    socket.on('connect', function () {
        console.log("WS connected");
        sessionStorage.setItem("errorcode", '0');
        var js = { cmd: "refresh" };
        js.data = "refreshsettinghome";
        var a = JSON.stringify(js);
        socket.send(a);
    });
    socket.on('disconnect', function () {
        console.log("WS disconnected.");
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
    socket.on('ip',function(ip_address){
        ip = ip_address;
        console.log(ip);
        console.log(localStorage.getItem("IP"));
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
    socket.on('settinghome', function(msg){
        var a = $.parseJSON(msg);
        if(ip === localStorage.getItem("IP")){
            $("#U1max").val(a.u1max);
            $("#U2max").val(a.u2max);
            $("#U3max").val(a.u3max);
            $("#I1max").val(a.i1max);
            $("#I2max").val(a.i2max);
            $("#I3max").val(a.i3max);
            $("#W1max").val(a.w1max);
            $("#W2max").val(a.w2max);
            $("#W3max").val(a.w3max);
            $("#Pfmax").val(a.Pfmax);
            $("#Irmax").val(a.Irmax);
            $("#Qcmax").val(a.Qcmax);
        }
    });
    $("#U1max").change(function(){
        var js = {cmd : "settinghome"};
        js.data = ["U1max",$(this).val()];
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $("#U2max").change(function(){
        var js = {cmd : "settinghome"};
        js.data = ["U2max", $(this).val()];
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $("#U3max").change(function(){
        var js = {cmd : "settinghome"};
        js.data = ["U3max",$(this).val()];
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $("#I1max").change(function(){
        var js = {cmd : "settinghome"};
        js.data = ["I1max",$(this).val()];
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $("#I2max").change(function(){
        var js = {cmd : "settinghome"};
        js.data = ["I2max",$(this).val()];
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $("#I3max").change(function(){
        var js = {cmd : "settinghome"};
        js.data = ["I3max",$(this).val()];
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $("#W1max").change(function(){
        var js = {cmd : "settinghome"};
        js.data = ["W1max",$(this).val()];
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $("#W2max").change(function(){
        var js = {cmd : "settinghome"};
        js.data = ["W2max",$(this).val()];
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $("#W3max").change(function(){
        var js = {cmd : "settinghome"};
        js.data = ["W3max",$(this).val()];
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $("#Pfmax").change(function(){
        var js = {cmd : "settinghome"};
        js.data = ["Pfmax",$(this).val()];
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $("#Irmax").change(function(){
        var js = {cmd : "settinghome"};
        js.data = ["Irmax",$(this).val()];
        var a = JSON.stringify(js);
        socket.send(a);
    });
    $("#Qcmax").change(function(){
        var js = {cmd : "settinghome"};
        js.data = ["Qcmax",$(this).val()];
        var a = JSON.stringify(js);
        socket.send(a);
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
});
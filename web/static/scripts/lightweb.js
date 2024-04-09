$(document).ready(function () {
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  var manual1 = "0";
  var manual2 = "0";
  var manual3 = "0";
  var manual4 = "0";
  var auto1 = "0";
  var auto2 = "0";
  var auto3 = "0";
  var auto4 = "0";
  var Pf = 0, P= 0, U=0, I=0;
  var ip = "0";
  socket.on('connect', function () {
    sessionStorage.setItem("errorcode", '0');
    console.log("WS connected");
    var js = { cmd: "refresh" };
    js.data = "refreshhomepage";
    var a = JSON.stringify(js);
    socket.send(a);
  });

  socket.on('disconnect', function () {
    console.log("WS disconnected");
  });
  
  socket.on('manage', function(msg){
    if(ip == localStorage.getItem("IP")){
      var a = $.parseJSON(msg);
      console.log(a);
      $("#ID").text(a.jsid);
      $("#manage").text(a.jsmanager);
      $("#lightbranch").text(a.jslightbranch);
      if (a.btn_branch1 === "1"){
        $("#btnbranch1").toggleClass('btn btn-branch btn btn-success');
      }
    }
  });
  socket.on('ip',function(ip_address){
    ip = ip_address;
    console.log(ip);
    console.log(localStorage.getItem("IP"));
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
  socket.on('parameter', function(msg){
      var a = $.parseJSON(msg);
        console.log(a);
      if(ip == localStorage.getItem("IP")){
        $("#U1").text(a.vol1);
        $("#U2").text(a.vol2);
        $("#U3").text(a.vol3);
        $("#I1").text(a.cur1);
        $("#I2").text(a.cur2);
        $("#I3").text(a.cur3);
        $("#W1").text(a.pow1);
        $("#W2").text(a.pow2);
        $("#W3").text(a.pow3);
        $("#Pf").text(a.aPf);
        $("#Qc").text(a.Qc);
        Pf = a.aPf;
        P = a.tpow;
        U = a.avol;
        I = a.acur;
    }
  });
  socket.on('timehome', function(msg){
    var a = $.parseJSON(msg);
    if(ip == localStorage.getItem("IP")){
      $("#starttime-home").val(a.starttime);
      $("#stoptime-home").val(a.stoptime);
    }
  });
  socket.on('lightstatus', function(msg){
    var a = $.parseJSON(msg);
    if(ip == localStorage.getItem("IP")){
      if (a.light1 === "1"){
        $("#light1").removeClass('color-light');
        $("#light1").addClass('color-man');
      }
      else if (a.light1 === "0"){
        $("#light1").removeClass('color-man');
        $("#light1").addClass('color-light');
      }
      if (a.light2 === "1"){
        $("#light2").removeClass('color-light');
        $("#light2").addClass('color-man');
      }
      else if (a.light2 === "0"){
        $("#light2").removeClass('color-man');
        $("#light2").addClass('color-light');
      }
      if (a.light3 === "1"){
          $("#light3").removeClass('color-light');
          $("#light3").addClass('color-man');
      }
      else if (a.light3 === "0"){
        $("#light3").removeClass('color-man');
        $("#light3").addClass('color-light');
      }
      if (a.light4 === "1"){
        $("#light4").removeClass('color-light');
        $("#light4").addClass('color-man');
      }
      else if (a.light4 === "0"){
        $("#light4").removeClass('color-man');
        $("#light4").addClass('color-light');
      }
    }
  });
  socket.on('control', function(msg){
    var a = $.parseJSON(msg);
    if(ip == localStorage.getItem("IP")){
      console.log(a);
      if (a.jsmanual1 === "1" && a.jsauto1 === "0" && manual1 === "0"){
        manual1 = "1";
        auto1 = "0";
        if($("#light1").hasClass('color-light')){
          $("#light1").removeClass('color-light');
          $("#light1").addClass('color-man');
        }
        $("#m1").toggleClass('fa-solid fa-hand-pointer btn-manualdis fa-solid fa-hand-pointer btn-manualac');
        $("#auto1").removeClass('btn btn-success');
        $("#auto1").addClass('btn btn-secondary');
  
      }
      else if(a.jsmanual1 === "0" && a.jsauto1 === "0" && manual1 === "1"){
        manual1 = "0";
        if($("#light1").hasClass('color-man')){
          $("#light1").removeClass('color-man');
          $("#light1").addClass('color-light');
        }
        $("#m1").toggleClass('fa-solid fa-hand-pointer btn-manualdis fa-solid fa-hand-pointer btn-manualac');
        $("#auto1").removeClass('btn btn-success');
        $("#auto1").addClass('btn btn-secondary');
      }
      else if(a.jsauto1 === "1" && a.jsmanual1 === "0" && auto1 === "0"){
        manual1 = "0";
        auto1 = "1";
        $("#auto1").removeClass('btn btn-secondary');
        $("#auto1").addClass('btn btn-success');
        /*if ($("#light1").hasClass('color-man')){
          $("#light1").removeClass('color-man');
          $("#light1").addClass('color-light');
        }*/
        $("#m1").removeClass('fa-solid fa-hand-pointer btn-manualac');
        $("#m1").addClass('fa-solid fa-hand-pointer btn-manualdis');
      }
      if (a.jsmanual2 === "1" && a.jsauto2 === "0" && manual2 === "0"){
        manual2 = "1";
        auto2 = "0";
        if($("#light2").hasClass('color-light')){
          $("#light2").removeClass('color-light');
          $("#light2").addClass('color-man');
        }
        $("#m2").toggleClass('fa-solid fa-hand-pointer btn-manualdis fa-solid fa-hand-pointer btn-manualac')
        $("#auto2").removeClass('btn btn-success');
        $("#auto2").addClass('btn btn-secondary');
  
      }
      else if(a.jsmanual2 === "0" && a.jsauto2 === "0" && manual2 === "1"){
        manual2 = "0";
        if($("#light2").hasClass('color-man')){
          $("#light2").removeClass('color-man');
          $("#light2").addClass('color-light');
        }
        $("#m2").toggleClass('fa-solid fa-hand-pointer btn-manualdis fa-solid fa-hand-pointer btn-manualac')
        $("#auto2").removeClass('btn btn-success');
        $("#auto2").addClass('btn btn-secondary');
      }
      else if(a.jsauto2 === "1" && a.jsmanual2 === "0" && auto2 === "0"){
        manual2 = "0";
        auto2 = "1";
        $("#auto2").removeClass('btn btn-secondary');
        $("#auto2").addClass('btn btn-success');
        /*if ($("#light2").hasClass('color-man')){
          $("#light2").removeClass('color-man');
          $("#light2").addClass('color-light');
        }*/
        $("#m2").removeClass('fa-solid fa-hand-pointer btn-manualac');
        $("#m2").addClass('fa-solid fa-hand-pointer btn-manualdis');
      }
      if (a.jsmanual3 === "1" && a.jsauto3 === "0" && manual3 === "0"){
        manual3 = "1";
        auto3 = "0";
        if($("#light3").hasClass('color-light')){
          $("#light3").removeClass('color-light');
          $("#light3").addClass('color-man');
        }
        $("#m3").toggleClass('fa-solid fa-hand-pointer btn-manualdis fa-solid fa-hand-pointer btn-manualac')
        $("#auto3").removeClass('btn btn-success');
        $("#auto3").addClass('btn btn-secondary');
  
      }
      else if(a.jsmanual3 === "0" && a.jsauto3 === "0" && manual3 === "1"){
        manual3 = "0";
        if($("#light3").hasClass('color-man')){
          $("#light3").removeClass('color-man');
          $("#light3").addClass('color-light');
        }
        $("#m3").toggleClass('fa-solid fa-hand-pointer btn-manualdis fa-solid fa-hand-pointer btn-manualac')
        $("#auto3").removeClass('btn btn-success');
        $("#auto3").addClass('btn btn-secondary');
      }
      else if(a.jsauto3 === "1" && a.jsmanual3 === "0" && auto3 === "0"){
        manual3 = "0";
        auto3 = "1";
        $("#auto3").removeClass('btn btn-secondary');
        $("#auto3").addClass('btn btn-success');
        /*if ($("#light3").hasClass('color-man')){
          $("#light3").removeClass('color-man');
          $("#light3").addClass('color-light');
        }*/
        $("#m3").removeClass('fa-solid fa-hand-pointer btn-manualac');
        $("#m3").addClass('fa-solid fa-hand-pointer btn-manualdis');
      }
      if (a.jsmanual4 === "1" && a.jsauto4 === "0" && manual4 === "0"){
        manual4 = "1";
        auto4 = "0";
        if($("#light4").hasClass('color-light')){
          $("#light4").removeClass('color-light');
          $("#light4").addClass('color-man');
        }
        $("#m4").toggleClass('fa-solid fa-hand-pointer btn-manualdis fa-solid fa-hand-pointer btn-manualac')
        $("#auto4").removeClass('btn btn-success');
        $("#auto4").addClass('btn btn-secondary');
  
      }
      else if(a.jsmanual4 === "0" && a.jsauto4 === "0" && manual4 === "1"){
        manual4 = "0";
        if($("#light4").hasClass('color-man')){
          $("#light4").removeClass('color-man');
          $("#light4").addClass('color-light');
        }
        $("#m4").toggleClass('fa-solid fa-hand-pointer btn-manualdis fa-solid fa-hand-pointer btn-manualac')
        $("#auto4").removeClass('btn btn-success');
        $("#auto4").addClass('btn btn-secondary');
      }
      else if(a.jsauto4 === "1" && a.jsmanual4 === "0" && auto4 === "0"){
        manual4 = "0";
        auto4 = "1";
        $("#auto4").removeClass('btn btn-secondary');
        $("#auto4").addClass('btn btn-success');
        /*if ($("#light4").hasClass('color-man')){
          $("#light4").removeClass('color-man');
          $("#light4").addClass('color-light');
        }
        else if ($("#light4").hasClass('color-light')){
          $("#light4").removeClass('color-light');
          $("#light4").addClass('color-man');
        }*/
        $("#m4").removeClass('fa-solid fa-hand-pointer btn-manualac');
        $("#m4").addClass('fa-solid fa-hand-pointer btn-manualdis');
      }
    }
  });
  socket.on('timecontrol', function(msg){
    var a = $.parseJSON(msg);
    if(ip == localStorage.getItem("IP")){
      $("#starttime1").text(a.start1);
      $("#stoptime1").text(a.stop1);
      $("#starttime2").text(a.start2);
      $("#stoptime2").text(a.stop2);
      $("#starttime3").text(a.start3);
      $("#stoptime3").text(a.stop3);
      $("#starttime4").text(a.start4);
      $("#stoptime4").text(a.stop4);
    }
  });
  function error(msg) {
    var ada = $("#ada");
    $("#ada div").remove();
    ada.append("<div class='alert alert-danger alert-dismissible' role='alert' id='ok'>"
        + "<strong>Báo lỗi</strong>" + msg
        + "<button type='button' class='close' data-dismiss='alert' aria-label='Close'>"
        + "<span aria-hidden='true'>&times;</span></button></div>");
    $("#ok").delay(5000).fadeOut(200);
  }
  $("#starttime-home").change(function(){
    if(ip == localStorage.getItem("IP")){
      var js = {cmd : "settime-home"};
      js.data = ["start",$(this).val()];
      var a = JSON.stringify(js);
      socket.send(a);
    }
  });
  $("#stoptime-home").change(function(){
    if(ip == localStorage.getItem("IP")){
      var js = {cmd : "settime-home"};
      js.data = ["stop",$(this).val()];
      var a = JSON.stringify(js);
      socket.send(a);
    }
  });
  $("#datetime").change(function() {
    if(ip == localStorage.getItem("IP")){
      var js = {cmd : "set-datetime"};
      js.data = $(this).val();
      var a = JSON.stringify(js);
      socket.send(a);
    }
  });
          /*$("#config").click(function () {
            $("#sys").modal('show');
          });*/
          $("#setup").click(function(){
            $("#set").modal('show');
          });
        
          $("#saveid").click(function(){
            if(ip == localStorage.getItem("IP")){
              var js = {cmd: "manage"};
              js.data = {};
              js.data.id = $("#setID").val();
              js.data.manager = $("#setmanager").val();
              js.data.lightbranch = $("#setlightbranch").val();
              var a=JSON.stringify(js);
              socket.send(a);
            }
          });
          
          $("#manual1").click(function(){
            if(ip == localStorage.getItem("IP")){
              var js = {cmd: "m1"};
              js.data = {m1: manual1 === "1" ? "0" : "1"};
              var a = JSON.stringify(js);
              console.log(a);
              socket.send(a);
            }
          });
          $("#manual2").click(function(){
            if(ip == localStorage.getItem("IP")){
              var js = {cmd: "m2"};
              js.data = {m2: manual2 === "1" ? "0" : "1"};
              var a = JSON.stringify(js);
              socket.send(a);
            }
          });
          $("#manual3").click(function(){
            if(ip == localStorage.getItem("IP")){
              var js = {cmd: "m3"};
              js.data = {m3: manual3 === "1" ? "0" : "1" };
              var a = JSON.stringify(js);
              socket.send(a);
            }
          });
          $("#manual4").click(function(){
            if(ip == localStorage.getItem("IP")){
              var js = {cmd: "m4"};
              js.data = {m4: manual4 === "1" ? "0" : "1"};
              var a = JSON.stringify(js);
              socket.send(a);
            }
          });
          $("#auto1").click(function(){
            if(ip == localStorage.getItem("IP")){
              var js = {cmd: "a1"};
              js.data = {a1: "1"};
              var a = JSON.stringify(js);
              socket.send(a);
            }
          });
          $("#auto2").click(function(){
            if(ip == localStorage.getItem("IP")){
              var js = {cmd: "a2"};
              js.data = {a2: "1"};
              var a = JSON.stringify(js);
              socket.send(a);
            }
          });
          $("#auto3").click(function(){
            if(ip == localStorage.getItem("IP")){
              var js = {cmd: "a3"};
              js.data = {a3: "1"};
              var a = JSON.stringify(js);
              socket.send(a);
            }
          });
          $("#auto4").click(function(){
            if(ip == localStorage.getItem("IP")){
              var js = {cmd: "a4"};
              js.data = {a4: "1"};
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
      var a = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11",
        "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"];
      for (var i = 0; i < a.length; i++) {
        $("#starttime-hour").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
        $("#stoptime-hour").append("<option value='" + (i + 1) + "'>" + a[i] + "</option>");
      }
    });

    $(function(){
      new Chart($("#chartP"), {
        type: 'line',
        labels: ['Red'],
        data: {
          datasets: [{
            label : 'P(kW)',
            backgroundColor:'black',
            borderColor:'red',
            color:'red'
          }]
        },
        options: {
          plugins: {
            colors: {
              enabled: false,
              forceOverride: true
            }
          },
          scales: {
            xAxes: {
              type: 'realtime',
              realtime: {
                onRefresh: chart =>{ 
                    chart.data.datasets.forEach(dataset => {
                    dataset.data.push({
                        x: Date.now(),
                        y: P
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartPf"), {
        type: 'line',
        labels: 'I(A)',
        data: {
          datasets: [{
            label: 'Pf',
            yAxisID: 'yAxis'
          }]
        },
        options: {
          scales: {
            xAxes: {
              type: 'realtime',
              realtime: {
                onRefresh: chart =>{ 
                    chart.data.datasets.forEach(dataset => {
                    dataset.data.push({
                        x: Date.now(),
                        y: Pf
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartU"), {
        type: 'line',
        labels: 'U(V)',
        data: {
          datasets: [{
            label: 'U(V)',
            yAxisID: 'yAxis'
          }]
        },
        options: {
          scales: {
            xAxes: {
              type: 'realtime',
              realtime: {
                onRefresh: chart =>{ 
                    chart.data.datasets.forEach(dataset => {
                    dataset.data.push({
                        x: Date.now(),
                        y: U
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartI"), {
        type: 'line',
        labels: 'I(A)',
        data: {
          datasets: [{
            label: 'I(A)',
            yAxisID: 'yAxis'
          }]
        },
        options: {
          scales: {
            xAxes: {
              type: 'realtime',
              realtime: {
                onRefresh: chart =>{ 
                    chart.data.datasets.forEach(dataset => {
                    dataset.data.push({
                        x: Date.now(),
                        y: I
                    });
                  });
                }
              }
            }
          }
        }
      });
    });
});
$(document).ready(function () {
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    
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
      new Chart($("#chartP1"), {
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartPf1"), {
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartU1"), {
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartI1"), {
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });

      new Chart($("#chartP2"), {
        type: 'line',
        labels: 'P(kW)',
        data: {
          datasets: [{
            label: 'P(kW)',
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartPf2"), {
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartU2"), {
        type: 'line',
        labels: 'I(A)',
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartI2"), {
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });

      new Chart($("#chartP3"), {
        type: 'line',
        labels: 'I(A)',
        data: {
          label: 'I(A)',
          datasets: [{
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartPf3"), {
        type: 'line',
        labels: 'I(A)',
        data: {
          label: 'I(A)',
          datasets: [{
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartU3"), {
        type: 'line',
        labels: 'I(A)',
        data: {
          label: 'I(A)',
          datasets: [{
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartI3"), {
        type: 'line',
        labels: 'I(A)',
        data: {
          label: 'I(A)',
          datasets: [{
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });

      new Chart($("#chartP4"), {
        type: 'line',
        labels: 'I(A)',
        data: {
          label: 'I(A)',
          datasets: [{
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartPf4"), {
        type: 'line',
        labels: 'I(A)',
        data: {
          label: 'I(A)',
          datasets: [{
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartU4"), {
        type: 'line',
        labels: 'I(A)',
        data: {
          label: 'I(A)',
          datasets: [{
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
        }
      });
      new Chart($("#chartI4"), {
        type: 'line',
        labels: 'I(A)',
        data: {
          label: 'I(A)',
          datasets: [{
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
                        y: Math.random()*10
                    });
                  });
                }
              }
            }
          }
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
});

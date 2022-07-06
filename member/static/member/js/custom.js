

    var xValues = ["Temperature °C", "CO", "Voice dB", "Pressure Pa", "Light"];
    var temp='{{ temperature }}';
    console.log('sdkjfjlsjflsjflsjdlkf '+ temp+ " nothing");
    var co = '{{ c }}';
    var voice = '{{ v }}';
    var pressure = '{{ p }}';
    var light = '{{ temperature }}';
    
    var yValues = [temp, co, voice, pressure, light];
    var barColors = ["red", "green","blue","orange","brown"];
    
    new Chart("myChart", {
      type: "bar",
      data: {
        labels: xValues,
        datasets: [{
          backgroundColor: barColors,
          data: yValues
        }]
      },
    
    options: {
            legend: {display: false,
         text: "irfan"}, 
         title: {
           display: true,
           text: "Vehicle Data Acquisition System"
         },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }],
                xAxes: [{
                    // Change here
                    barPercentage: 0.5
                }]
            }
        }
     
    });

    // HideThinkSpeakLAble

 
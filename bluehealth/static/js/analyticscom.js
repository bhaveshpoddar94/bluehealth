function makeChart(fieldname, labels, values, unit, color, chart_name){
  var ctx = document.getElementById(chart_name).getContext('2d');
  var myChart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',
    // The data for our dataset
    data: {
        labels: labels,
        datasets: [{
            label: fieldname + "( "+unit+" )",
            fill: false,
            borderColor: color,
            data: values,
            borderWidth: 3,
        }],
    },
    // Configuration options go here
    options: {
        layout: {
            padding: {
                left: 0,
                right: 0,
                top: 30,
                bottom: 0
            }
        }
    }
  });
}

function loadData(chartname, type) {
    $.ajax({
      type: "GET",
      url: 'observations/ajax-data/',
      data:{"type": type},
      dataType: 'json',
      success: function (data) {
        makeChart(data.fieldname, data.labels, data.values, data.unit, data.color, chartname);
      }
    });
}

function loadcomData(type1, type2) {
    $.ajax({
      type: "GET",
      url: '/ajax-com-data/',
      data:{"type1": type1, "type2": type2},
      dataType: 'json',
      success: function (data) {
        var ctx = document.getElementById("myChart1").getContext('2d');
        var myChart = new Chart(ctx, {
          // The type of chart we want to create
          type: 'line',
          // The data for our dataset
          data: {
              labels: data.data1.labels,
              datasets: [{
                  label: data.data1.fieldname + "( "+data.data1.unit+" )",
                  fill: false,
                  borderColor: data.data1.color,
                  data: data.data1.values,
                  borderWidth: 3,
              },
              {
                  label: data.data2.fieldname + "( "+data.data2.unit+" )",
                  fill: false,
                  borderColor: data.data2.color,
                  data: data.data2.values,
                  borderWidth: 3,
              }]
          },
          // Configuration options go here
          options: {}
        });
    }
  });
}

$(function(){
  loadcomData('f1', 'f3');
  loadData('myChart2', 'f2');
  loadData('myChart3', 'f4');
  loadData('myChart4', 'f7');
  loadData('myChart5', 'f8');
});

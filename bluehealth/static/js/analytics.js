function makeChart(fieldname, labels, values, unit, color){
  var ctx = document.getElementById("myChart").getContext('2d');
  myChart = new Chart(ctx, {
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
        }]
    },
    // Configuration options go here
    options: {}
  });
}

function add_data(type){
  
}

function loadData(type) {
    $.ajax({
      type: "GET",
      url: '/ajax-data/',
      data:{"type": type},
      dataType: 'json',
      success: function (data) {
        makeChart(data.fieldname, data.labels, data.values, data.unit, data.color);
        last_label = data.labels[data.labels.length-1]
        call_id = setInterval(add_data, 5000, type);
      }
    });
}

$(function(){
  loadData('f1');
});


$('.sidenav a').click(function(event) {
   event.preventDefault();
   clearInterval(call_id);
   var type = $(this).attr("id");
   myChart.destroy();
   loadData(type);
});

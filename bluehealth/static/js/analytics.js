function makeChart(fieldname, labels, values, unit, color){
  var ctx = document.getElementById("myChart").getContext('2d');
  myChart = new Chart(ctx, {
    type: 'line',
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

function loadData(type) {
    $.ajax({
      type: "GET",
      url: '/observations/',
      data: {"type": type},
      dataType: 'json',
      success: function (data) {
        const fieldname = data[0].type;
        makeChart(fieldname, labels, values, 'cm', '#ff4d4d');
      },
      error: function (err) {
        console.log(err);
      }
    });
}

$(function(){
  loadData('f1');
});


$('.sidenav a').click(function(event) {
   event.preventDefault();
   var type = $(this).attr("id");
   myChart.destroy();
   loadData(type);
});
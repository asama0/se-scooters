var week_array = []
var month_array = []
var year_array = []
var total_array = []

//sets array and gets data from flask
function InitializeMe(){
    $.post("/week_request", function (data){
        week_array = data.slice();
        updateTheGraphs(barchar, weekl, week_array);
    })

     $.post("/month_request", function (data){
        month_array = data.slice();
        updateTheGraphs(barchar2, month_lable, month_array);
    })

     $.post("/year_request", function (data){
        year_array = data.slice();
        updateTheGraphs(barchar3, year_lable, year_array);
    })

     $.post("/total_request", function (data){
        total_array = data.slice();
        updateTheGraphs(barchar4, total_lable, total_array);
    })
}







function updateTheGraphs(chart, label, arr) {

    for (var i = 0; i < arr.length; i++) {
        //datasets[0] - shows the index of a dataset, there can be more then 1
        chart.config.data.datasets[0].data[i] = arr[i];
    }
    chart.update();
}



const weekl = ['Monday', 'Tuesday', 'Wednesday', 'Thurthsday', 'Friday', 'Saturday', 'Sunday']

var data_week = {
  labels: weekl,
        datasets: [{
            label: 'WEEKLY GRAPH',
            data: [],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
};



const month_lable = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
'13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', "24", "25", '26',
'27', '28', '29', '30']

var data_month = {
  labels: month_lable,
        datasets: [{
            label: 'MONTHLY GRAPH',
            data: [],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
};



var config2 = {
  type: 'line',
  data: data_week,
  options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
};


var monthl = {
  type: 'line',
  data: data_month,
  options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
};







const year_lable = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

var data_year = {
  labels: year_lable,
        datasets: [{
            label: 'YEARLY GRAPH',
            data: [],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
};




var yearl = {
  type: 'bar',
  data: data_year,
  options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
};






const total_lable = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

var data_total = {
  labels: total_lable,
        datasets: [{
            label: 'TOTAL GRAPH',
            data: [],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
};




var totals = {
  type: 'bar',
  data: data_total,
  options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
};








//for  different layers dublicated
var barchar = new Chart(
    document.getElementById('canvas_plot1'),
    config2
)
//for  different layers dublicated
const barchar2 = new Chart(
    document.getElementById('canvas_plot2'),
    monthl
)

//for  different layers dublicated
const barchar3 = new Chart(
    document.getElementById('canvas_plot3'),
    yearl
)


//for  different layers dublicated
const barchar4 = new Chart(
    document.getElementById('canvas_plot4'),
    totals
)



//for  different layers dublicated
const barchar5 = new Chart(
    document.getElementById('canvas_plot7'),
    yearl
)



// //for  different layers dublicated
// const barchar5 = new Chart(
//     document.getElementById('canvas_plot7'),
//     config2
// )







//---------------------------------------------------//






  const labels = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
  ];

  const data = {
    labels: labels,
    datasets: [{
      label: 'Lololop',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [],
    },
        // {
        //     label: 'Something',
        //   backgroundColor: 'rgb(100, 99, 132)',
        //   borderColor: 'rgb(100, 99, 132)',
        //   data: [0, 30, 5, 33, 20, 30, 45],
        // }
    ]
  };



  const config = {
    type: 'line',
    data: data,
    options: {

    }
  };


    //for  different layers dublicated
    const myChart = new Chart(
    document.getElementById('canvas_plot5'),
    config2
  );



    //for  different layers dublicated
    const myChart2 = new Chart(
    document.getElementById('canvas_plot6'),
    monthl
  );


     //for  different layers dublicated
    const myChart3 = new Chart(
    document.getElementById('canvas_plot8'),
    totals
  );










    //code for showing and hiding canvas layers


// let content2 = document.getElementById("item")
// let content = document.getElementById("content")
// let show = document.getElementById("showContent")
// let hide = document.getElementById("hideContent")
//
// show.addEventListener("click", () => {
//     content.style.display = "block"
//     content2.style.display = "none"
// })
//
// hide.addEventListener("click", () => {
//     content.style.display = "none"
//     content2.style.display = "block"
// })

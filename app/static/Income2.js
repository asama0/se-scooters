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
        updateTheGraphs(barchar, labels2, year_array);
    })

     $.post("/total_request", function (data){
        total_array = data.slice();
        updateTheGraphs(barchar, labels2, total_array);
    })
}







function updateTheGraphs(chart, label, arr) {

    for (var i = 0; i < arr.length; i++) {
        //datasets[0] - shows the index of a dataset, there can be more then 1
        chart.config.data.datasets[0].data[i] = arr[i];
    }
    chart.update();
}



const weekl = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']

var data_week = {
  labels: weekl,
        datasets: [{
            label: '# of Votes',
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



const month_lable = ['1', '2', '3', '4', '5', '6']

var data_month = {
  labels: month_lable,
        datasets: [{
            label: 'Second',
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
  type: 'bar',
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
  type: 'bar',
  data: data_month,
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
    config2
)


//for  different layers dublicated
const barchar4 = new Chart(
    document.getElementById('canvas_plot5'),
    config2
)



//for  different layers dublicated
const barchar5 = new Chart(
    document.getElementById('canvas_plot7'),
    config2
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
    document.getElementById('canvas_plot4'),
    config
  );



    //for  different layers dublicated
    const myChart2 = new Chart(
    document.getElementById('canvas_plot6'),
    config
  );


     //for  different layers dublicated
    const myChart3 = new Chart(
    document.getElementById('canvas_plot8'),
    config
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
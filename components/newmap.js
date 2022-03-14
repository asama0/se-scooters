//Scooter icon made by Freepik from: https://www.w3schools.com/html/html5_geolocation.asp

//leeds art gallery
var map_centre = {lat: 53.8000, lng: -1.5482}; 


                                //lat   long    ,zoom.
var map = L.map('map').setView([map_centre.lat, map_centre.lng], 15);

const attribution = 
'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors ';

const tileURL = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
const tiles = L.tileLayer(tileURL,{attribution});
tiles.addTo(map)

var myIcon = L.icon({

iconUrl: 'scooter_icon.png',
iconSize: [40, 40],
iconAnchor: [22, 94],
popupAnchor: [-3, -76],

});

//adding parkings

//trinity parking
var park_a = { name : "trinity", loc : {lat: 53.7965, lng: -1.5425}, 
availability: "Available",
scooters : "100-103" };


//Train station
var park_b = { name: "Train station", loc : {lat: 53.7956, lng: -1.5472},
availability: "Available", scooters:"104-107"};


//Merrion centre
var park_c = { name: "Merrion centre", loc : {lat: 53.8013, lng:  -1.5432},
availability: "Available", scooters:"108-201"};



//LRI hospital 

var park_d = { name: "LRI hospital", loc : {lat: 53.8025, lng:  -1.5528},
availability: "Available", scooters:"202-205"};



//UoL Edge sports centre

var park_e = { name: "UoL Edge sports centre", loc : {lat: 53.8039, lng:   -1.5530},
availability: "Available", scooters:"206-209"};



//adding markers for parkings
var marker0 = L.marker([park_a.loc.lat, park_a.loc.lng], {icon: myIcon}).addTo(map);
var marker1 = L.marker([park_b.loc.lat, park_b.loc.lng], {icon: myIcon}).addTo(map);
var marker2 = L.marker([park_c.loc.lat, park_c.loc.lng], {icon: myIcon}).addTo(map);
var marker3 = L.marker([park_d.loc.lat, park_d.loc.lng], {icon: myIcon}).addTo(map);
var marker4 = L.marker([park_e.loc.lat, park_e.loc.lng], {icon: myIcon}).addTo(map);

const str = "some text";

const form0 = "<form action=\"#\" method=\"get\"> " +
            "<label for=\"date\">Date:</label><input type=\"date\" "+
            " id=\"time\" name=\"time\"><br><br><label for=\"time\"> " +
            " Time:</label><input type=\"time\" id=\"time\" name=\" time\"> " +
            "<br></br>"+   
            " <label for=\"duration\">Duration:</label> " +       
            "<select name = \"select\" id = \'#'>" +
            "<option value \"1\"> 1 hour</option>>" +
            "<option value \"2\"> 24 hours</option>>" +
            "<option value \"3\"> 1 week</option>>" +
            "</select>" +
            "<br><br>" +
            "<input type=\"submit\" value=\"Book\">" +
            "</form>";

// function dynamic_form(){

// }
marker0.bindPopup(form0);
marker1.bindPopup(form0);
marker2.bindPopup(form0);
marker3.bindPopup(form0);
marker4.bindPopup(form0);

//lat   long    ,zoom.
var map = L.map('map').setView([0, 0], 1);

const attribution = 
'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors ';

const tileURL = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
const tiles = L.tileLayer(tileURL,{attribution});
tiles.addTo(map)

var myIcon = L.icon({

iconUrl: 'scooter_icon.png',
iconSize: [30, 30],
iconAnchor: [22, 94],
popupAnchor: [-3, -76],

});
var marker = L.marker([50.5, 30.5], {icon: myIcon}).addTo(map);

const str = "some text";

const form0 = "<form action=\"#\" method=\"get\"> " +
            "<label for=\"date\">Date:</label><input type=\"date\" "+
            " id=\"time\" name=\"time\"><br><br><label for=\"time\"> " +
            " Time:</label><input type=\"time\" id=\"time\" name=\" " +
            " time\"><br><br><input type=\"submit\" value=\"Book\">"  +
            "<br></br><select name = \"select\" id = \'#'>" +
            "<option value \"1\"> option 1</option>>" +
            "<option value \"2\"> option 2</option>>" +
            "<option value \"3\"> option 3</option>>" +
            "</select>" +
            "</form>"
marker.bindPopup(form0);


//Not going to attempt changing var values inside functions
//
var p1 = document.getElementById("p1");
var p2 = document.getElementById("p2");
var p3 = document.getElementById("p3");


//This code is to find user's current location
//NOTE: the code works, but the value of location when stored in
//a var, the var value returns again to original value when
//outside of the function scope.

//TODO:  move everything inside initmap methode.

// if(navigator.geolocation){
//     navigator.geolocation.getCurrentPosition(function(current_location){

//         //var place = {lat: 0, lng: 0};
//         place.lat = current_location.coords.latitude;
//         place.lng = current_location.coords.longitude;  
//         //return place;

//     });             
// }else{    
//     p1.innerHTML = ("Your browser does not support GPS!");
// }





//https://developers.google.com/maps/documentation/javascript/overview

//This is the function the google link with be looking for when
//it launches the map's api.

function initMap() {

    //leeds art gallery
    var map_centre = {lat: 53.8000, lng: -1.5482}; 

    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: map_centre
        });
    

    //adding parkings
    
    //trinity parking
    var park_a = { name : "trinity", loc : {lat: 53.7965, lng: -1.5425}, 
    availability: "Available",
    scooters : "100-103" };
    addMarker(park_a);
    
    //Train station
    var park_b = { name: "Train station", loc : {lat: 53.7956, lng: -1.5472},
    availability: "Available", scooters:"104-107"};
    addMarker(park_b);

    //Merrion centre
    var park_c = { name: "Merrion centre", loc : {lat: 53.8013, lng:  -1.5432},
    availability: "Available", scooters:"108-201"};
    addMarker(park_c);


    //LRI hospital 

    var park_d = { name: "LRI hospital", loc : {lat: 53.8025, lng:  -1.5528},
    availability: "Available", scooters:"202-205"};
    addMarker(park_d);



    //UoL Edge sports centre

    var park_e = { name: "UoL Edge sports centre", loc : {lat: 53.8039, lng:   -1.5530},
    availability: "Available", scooters:"206-209"};
    addMarker(park_e);


    //Shows user current location in lat-lng formate
    p2.innerHTML = ("Your Current location is:" + 
    " Lat: " + place.lat +
    " Long: " + place.lng);  


    // source: https://www.youtube.com/watch?v=Zxf1mnP5zcw
    //dynamic function to add marker in map.
    //param: place: place of scooter, 

    function addMarker(park){

        var Marker =  new google.maps.Marker({
        position: park.loc,
        map: map,
        icon: "scooter_icon.png",
    
        });

        // var pop_up_form = ;
        var scooter_info = new google.maps.InfoWindow({

            
            content: "<h3> Parking name: </h3>" + park.name +
                    "<h3> Available Scooters: </h3>"  + park.scooters +
                    "<form action=\"/action_page.php\" method=\"get\"> " +
                    "<label for=\"fname\">First name:</label><input type=\"text\" "+
                    " id=\"fname\" name=\"fname\"><br><br><label for=\"lname\"> " +
                    " Last name:</label><input type=\"text\" id=\"lname\" name=\" " +
                    " lname\"><br><br><input type=\"submit\" value=\"Submit\"></form>"
                    
        });

        Marker.addListener('click',function(){
            
            scooter_info.open(map,Marker);
            //p3.innerHTML("Scooter id: " + id);
        });
        
    }
        
}
    



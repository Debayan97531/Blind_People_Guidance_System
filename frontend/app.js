x=navigator.geolocation;

x.getCurrentPosition(success,failure);

function success(position){

    var myLat=position.coords.latitude;
    var myLong=position.coords.longitude;

    var coords = new google.maps.LatLng(myLat,myLong);

    var mapOptions={
        zoom:5,
        center:coords,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }

    var map=new google.maps.Map(document.getElementById("map"),mapOptions);

    var maker= new google.maps.Marker({
        map:map,
        position:coords
    });
}

function failure(){}
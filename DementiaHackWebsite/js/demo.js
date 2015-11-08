//Data format: {"time": "2015-11-07 15:33:36.714000", "y": 2.883, "uuid": "0x0000", "x": 3.424}
$(document).ready(function(){
    //get position data
    function track(data){  
        //process the data string
        dataObject = JSON.parse(data);
        //get time data for checking purposes
        time = dataObject.time;
        //plot position data
        xData = dataObject.x;
        yData = dataObject.y;
        debugger;
        
        $("canvas").drawArc({
            fillStyle: 'red',
            x : numBorder + xData* factor , y : numBorder + yData* factor, 
            radius: 10
        });
    }
    
    function getData(){
        debugger;
        url = 'http://mensangeli.mybluemix.net/datapull/';
        data = {uuid:'0x0000'};
        $.post(url, data).done(track)
    }
    // when the button is clicked, start demo!
    $(".button").click(function(){
        debugger;
        //draw the ibeacons on the canvas
        //modifies the position of the beacons to better fit the screen
        numBorder = 30;
        factor = 120;
        
        //beacon 1:
        $("canvas").drawPolygon({
            fillStyle: 'black',
            sides:3,
            x : numBorder, y : numBorder, //(0,0)
            radius: 10
        })
        
        //beacon 2: 
        .drawPolygon({
            fillStyle: 'black',
            sides: 3,
            x : numBorder , y : numBorder + 5*factor, //(0,5) distances are multiplied by 5 and add 20
            radius: 10
        })
        
        //beacon 3: 
        .drawPolygon({
            fillStyle: 'black',
            sides: 3,
            x : numBorder + 5*factor , y : numBorder, //(0,5)
            radius: 10
        });
        
        //Tracker:
        //getData();
        //Get data and plot it every second
        var tid = setInterval(getData,10000);
       
    }); 
});


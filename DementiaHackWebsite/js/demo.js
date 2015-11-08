//Data format: {"time": "2015-11-07 15:33:36.714000", "y": 2.883, "uuid": "0x0000", "x": 3.424}
$(document).ready(function(){
    
    numBorder = 30;
    factor = 120;
    radius = 20;
    k = 0;
    dataArray = new Array('{"time": "2015-11-07 15:33:36.714000", "y": 2.883, "uuid": "0x0000", "x": 3.424}',
    '{"time": "2015-11-07 15:33:37", "y": 3.2, "uuid": "0x0000", "x": 3.424}',
    '{"time": "2015-11-07 15:33:38.714000", "y": 3.4, "uuid": "0x0000", "x": 4.0}',
    '{"time": "2015-11-07 15:33:39.714000", "y": 3.0, "uuid": "0x0000", "x": 3.8}',
    '{"time": "2015-11-07 15:33:36.714000", "y": 3.5, "uuid": "0x0000", "x": 3.4}',
    '{"time": "2015-11-07 15:33:36.714000", "y": 4.0, "uuid": "0x0000", "x": 3.0}',
    '{"time": "2015-11-07 15:33:37.714000", "y": 4.2, "uuid": "0x0000", "x": 2.5}',
    '{"time": "2015-11-07 15:33:38.714000", "y": 4.3, "uuid": "0x0000", "x": 3.5}',
    '{"time": "2015-11-07 15:33:36.714000", "y": 4.0, "uuid": "0x0000", "x": 3.8}',
    '{"time": "2015-11-07 15:33:36.714000", "y": 3.5, "uuid": "0x0000", "x": 2.5}',
    '{"time": "2015-11-07 15:33:36.714000", "y": 2.8, "uuid": "0x0000", "x": 4.2}',
    '{"time": "2015-11-07 15:33:36.714000", "y": 2.7, "uuid": "0x0000", "x": 4.0}',
    '{"time": "2015-11-07 15:33:36.714000", "y": 2.6, "uuid": "0x0000", "x": 3.0}',
    '{"time": "2015-11-07 15:33:36.714000", "y": 2.50, "uuid": "0x0000", "x": 2.5}',
    '{"time": "2015-11-07 15:33:36.714000", "y": 2.0, "uuid": "0x0000", "x": 1.0}',
    '{"time": "2015-11-07 15:33:36.714000", "y": 1.6, "uuid": "0x0000", "x": 1.5}',
    '{"time": "2015-11-07 15:33:36.714000", "y": 1.1, "uuid": "0x0000", "x": 2.5}',
    '{"time": "2015-11-07 15:33:36.714000", "y": 1.0, "uuid": "0x0000", "x": 2.0}',
    '{"time": "2015-11-07 15:33:45.714000", "y": 1.0, "uuid": "0x0000", "x": 2.0}'
    );
    
    //constructor for tracker 
    function trackShape(color,xData, yData,time){
        this.color = color;
        x = xData;
        y = yData; 
        this.time = time;
    }
    
    trackObject = new trackShape('#00E500',0,0,0);
    
    //get position data
    function track(/*data*/){  
        data = dataArray[k];
        
        //process the data string
        dataObject = JSON.parse(data);
        
        //get time from the data recieved
        trackObject.time = new Date(dataObject.time);
        //get current time data for checking purposes      
        currentTime = new Date("2015-11-07 15:33:36.714000");//new Date($.now());
        
        //plot position data
        trackObject.x = numBorder + dataObject.x* factor;
        trackObject.y = numBorder + dataObject.y* factor; 
        //debugger;
        
        //If the data is old
        if(Math.abs(currentTime - trackObject.time) >= 5000)
        {
            //debugger;
            trackObject.color = 'red',            
            $("canvas").drawArc({
                layer:true,
                name: 'trackArc',
                fillStyle: trackObject.color,
                x : trackObject.x, y : trackObject.y, 
                strokeStyle:'black',
                radius: radius,
            }); 
        }
        //If data is new enough
        else{  
            $("canvas").drawArc({
                fillStyle: trackObject.color,
                x : trackObject.x, y : trackObject.y, 
                strokeStyle:'black',
                radius: radius,
            });
            
            setTimeout(function() {
                    $('canvas').clearCanvas({
                    x:trackObject.x, y: trackObject.y,
                    width: 50, height:50,
                })    
            }, 900)
        }
         k = k+1;
    }
    
    function getData(){
        //debugger;
        url = 'http://mensangeli.mybluemix.net/datapull/';
        data = {uuid:'0x0000'};
        
        $.post(url, data).done(track)
    }
    
    
    // when the button is clicked, start demo!
    $(".button").click(function(){
             
        //create the canvas area
        $("canvas").attr({
            height:"800px",
            width: "650px",
        });
        
        //draw the hallway edges on the canvas
        $("canvas").drawLine({
            strokeStyle : 'black',
            strokeWidth: 10,
            x1: 0, y1:0,
            x2: 0, y2: 800,
        });
        
        $("canvas").drawLine({
            strokeStyle : 'black',
            strokeWidth: 10,
            x1: 650, y1:0,
            x2: 650, y2: 800,
        });
        
        //draw the ibeacons on the canvas
        //modifies the position of the beacons to better fit the screen
        
        //beacon 1:
        $("canvas").drawPolygon({
            fillStyle: 'black',
            sides:3,
            x : numBorder, y : numBorder, //(0,0)
            radius: radius,
        });
        
        //beacon 2: 
        $("canvas").drawPolygon({
            fillStyle: 'black',
            sides: 3,
            x : numBorder , y : numBorder + 5*factor, //(0,5) distances are multiplied by 5 and add 20
            radius: radius,
        });
        
        //beacon 3: 
        $("canvas").drawPolygon({
            fillStyle: 'black',
            sides: 3,
            x : numBorder + 5*factor , y : numBorder, //(0,5)
            radius: radius,
        });

        //Tracker:
        //getData();
        //Get data and plot it every second
        var tid = setInterval(track /*getData*/,1000);
    }); 
});


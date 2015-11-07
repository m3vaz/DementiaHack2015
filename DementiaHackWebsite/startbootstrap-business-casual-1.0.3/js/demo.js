$(document).ready(function(){
    // when the button is clicked, start demo!
    $(".button").click(function(){
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
            
        //Get data and plot it every second
        //var tid = setInterval(getData,1000);
        
        //get position data
        function getData(){
            $.ajax({
                url:"http://mensangeli.mybluemix.net/",
                type: "GET",
                dataType:'jsonp',
                success : track,
            }) 
        }
        
        function track(data){
            debugger;
            $("canvas").drawText({
              fillStyle: '#9cf',
              strokeStyle: '#25a',
              strokeWidth: 2,
              x: 150, y: 100,
              fontSize: 48,
              fontFamily: 'Verdana, sans-serif',
              text: data,
            });
            /*        
            //plot position data
            xData = ;
            yData = ;
            
            .drawArc({
                fillStyle: 'red',
                x : numBorder + xData* factor , y : numBorder + yData* factor, 
                radius: 10
            });
            */
        }
    }); 
});


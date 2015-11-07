$(document).ready(function(){
    // when the button is clicked, start demo!
    $(".button").click(function(){
        //draw the ibeacons on the canvas
        //modifies the position of the beacons to better fit the screen
        numBorder = 30;
        factor = 120;
        
        //beacon 1:
        $("canvas").drawArc({
            fillStyle: 'black',
            x : numBorder, y : numBorder, //(0,0)
            radius: 10
        })
        
        //beacon 2: 
        .drawArc({
            fillStyle: 'black',
            x : numBorder , y : numBorder + 5*factor, //(0,5) distances are multiplied by 5 and add 20
            radius: 10
        })
        
        //beacon 3: 
        .drawArc({
            fillStyle: 'black',
            x : numBorder + 5*factor , y : numBorder, //(0,5)
            radius: 10
        });
        
        //get the data and then plot it 
        while(){
            
        }
    });
});


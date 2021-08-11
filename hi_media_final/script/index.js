$('#slide a').eq(0).css('left','0');
$('#slide a').eq(1).css('left','-1200px');
$('#slide a').eq(2).css('left','-1200px');

var start=0;
setInterval(()=>{
    if(start==2){
        start=0;
    }else{start++;}
    $('#slide a').eq(start-1).css('left','-1200px');
    $('#slide a').eq(start).css('left','0');
},3000);
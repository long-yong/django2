
function hello() {
    console.log("Hello");
}

function checkMM(MM){
   switch(MM)
   {
       case  1: return 'Jan';
       case  2: return 'Feb';
       case  3: return 'Mar';
       case  4: return 'Apr';
       case  5: return 'May';
       case  6: return 'Jun';
       case  7: return 'Jul';
       case  8: return 'Aug';
       case  9: return 'Sept';
       case 10: return 'Oct';
       case 11: return 'Nov';
       case 12: return 'Dec';
       default: return 'None';
   }
}

function checkPM(hh) {  if(hh>=12) return ' PM'; else return ' AM'; }
function checkdd(dd) {  if (dd<10) return '0'+ dd;  else return dd; }
function checkmm(mm) {  if (mm<10) return '0'+ mm;  else return mm; }
function checkss(ss){   if (ss<10) return '0'+ ss;  else return ss; }

function getTimeStr() {
    var today=new Date();
    var yyyy = today.getFullYear();
    var MM = today.getMonth()+1;
    var dd = today.getDate();
    var hh = today.getHours();
    var mm = today.getMinutes();
    var ss = today.getSeconds();
    PM=checkPM(hh);
    MM=checkMM(MM);
    dd=checkdd(dd);
    mm=checkmm(mm);
    ss=checkss(ss);
    arr = [0,0];
    arr[0] = MM + ' ' + dd + ', ' +  yyyy;
    arr[1] = hh + ":" + mm + ":" + ss + ' ' +PM;
    return arr;
}
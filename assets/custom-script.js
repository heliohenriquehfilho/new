function printData() {
    var divContents = document.getElementById("outter-box").innerHTML;
    var prnt = window.open('', '', 'height=500, width=500');
    prnt .document.write("POWERED BY: PECCE")
    prnt .document.write(divContents);
    prnt .document.close();
    prnt .print();
}

setTimeout(function mainFunction(){
    try {
        document.getElementById("run").addEventListener("click", function(){
            printData();
        })
      }
      catch(err) {
        console.log(err)
      }
    console.log('Listener Added!');
}, 5000);
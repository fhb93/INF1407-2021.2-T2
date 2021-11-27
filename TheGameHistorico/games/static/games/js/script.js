

// onclick = function () {
 
//     var selectField = document.getElementById("id_status");
//     var verified = document.getElementById("id_time_completion");

//     // show/hide on load based on existing value of selectField
//     value = selectField.value;

//     console.log(value);

//     console.log(verified);

//     if (value === "opt1") {
//         // verified.style.display = "none";
//         document.querySelector("#id_time_completion").style.disabled = 'disabled';

//     } else {
//         document.querySelector("#id_time_completion").style.disabled = "";
//         // verified.style.display = "block";
//     }
   
// }
onload = function() {
     document.querySelector('#id_time_completion').disabled = 'disabled';
};
// Wait for the page to finish loading
onclick = function() {
  // Select the billing text fields

    if(document.getElementById('id_status') != null) {
        var value = document.getElementById('id_status').value;

        if(value != "opt1")
        {
            document.querySelector('#id_time_completion').disabled = '';

        }
        else{
            document.querySelector('#id_time_completion').disabled = 'disabled';
        }
    }
};

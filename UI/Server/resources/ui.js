console.log("Here");

var handleSubmit = function () {
    console.log("Form submitted");
    let inputData = [];


    var title = document.getElementById("Role").value;
    inputData.push(title);
    // var fullTime = document.querySelector('.fullTime:checked').value;
    // inputData.push(fullTime);
    var workerPos = document.getElementById("workerPositions").value;
    inputData.push(workerPos);
    inputData.push(document.querySelector('.newEmp:checked').value);
    inputData.push(document.querySelector('.continueEmp:checked').value);
    inputData.push(document.querySelector('.change:checked').value);
    //inputData.push(document.querySelector('.concurrentEmp:checked').value);
    inputData.push(document.querySelector('.changeEmp:checked').value);
    inputData.push(document.querySelector('.petition:checked').value);
    inputData.push(document.getElementById('employer').value);
    inputData.push(document.querySelector('.agent:checked').value);
    inputData.push(document.querySelector('.entity:checked').value);

    inputData.push(document.getElementById('salary').value);
    inputData.push(document.getElementById('salaryUnit').value);
    inputData.push(document.getElementById('prevailing').value);
    inputData.push(document.getElementById('prevailingUnit').value);
    inputData.push(document.getElementById('worksiteLocations').value);

    //inputData.push(document.querySelector('.lc:checked').value);
    inputData.push(document.querySelector('.h1b_dep:checked').value);
    //inputData.push(document.querySelector('.violator:checked').value);

    inputData.push(document.querySelector('.suport:checked').value);
    inputData.push(document.getElementById('basis').value);
    
    console.log("fullTime "+inputData.length);

    //console.log("Server Connection"+number+" "+otp);
    var url = new URL("http://localhost:9000/server");
    url.search = new URLSearchParams({inputData : inputData });
    url = url.toString();
    console.log("URL "+url);
    fetch(url,{
        })
    .then(response => response.json())
    .then(data =>{
        console.log(data);
        console.log("Data "+JSON.stringify(data));
        console.log("Type "+typeof(data));
        data = JSON.parse(data);
        let outcome = data["outcome"];

        document.getElementById("agentForm").style.display = 'none';
        document.getElementById("outcome").style.display = "block";
        
        if(outcome == "0"){
            document.getElementById("outcome").innerHTML = "Approved";
        }
        else
            document.getElementById("outcome").innerHTML = "Denied";
    })      
};

var initializor = function () {
    var form = document.getElementById("agentForm");
    function handleForm(event) {
        event.preventDefault();
    }
    if (form)
        form.addEventListener('submit', handleForm);
};

initializor();

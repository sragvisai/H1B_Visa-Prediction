var handleSubmit = function () {
    console.log("Form submitted");
    let inputData = [];


    var title = document.getElementById("role").value;
    inputData.push(title);
    inputData.push(document.getElementById('empName').value);
    inputData.push(document.getElementById('salry').value);
    inputData.push(document.getElementById('prevWage').value);
    inputData.push(document.getElementById('country').value);
    console.log("fullTime "+inputData.length);
    var url = new URL("http://localhost:9000/server");
    url.search = new URLSearchParams({inputData : inputData });
    url = url.toString();
    console.log("URL "+url);
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

        document.getElementById("employeeForm").style.display = 'none';
        document.getElementById("outcome").style.display = "block";
        
        if(outcome == "0"){
            document.getElementById("outcome").innerHTML = "Approved";
        }
        else
            document.getElementById("outcome").innerHTML = "Denied";
    })      
};


var initializor = function () {
    var form = document.getElementById("employeeForm");
    function handleForm(event) {
        event.preventDefault();
    }
    if (form)
        form.addEventListener('submit', handleForm);
};

initializor();

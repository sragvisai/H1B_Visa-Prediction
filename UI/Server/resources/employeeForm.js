var handleSubmit = function () {
    console.log("Form submitted");
    let inputData = [];
    let goAhead = 0;

    try{
        var title = document.getElementById("role").value;
        inputData.push(title);
        inputData.push(document.getElementById('empName').value);
        inputData.push(document.getElementById('salry').value);
        inputData.push(document.getElementById('prevWage').value);
        inputData.push(document.getElementById('country').value);
        inputData.push(document.querySelector('.degree:checked').value);
        if(title == "" || document.getElementById('empName')== "" || document.getElementById('salry') =="" || document.getElementById('prevWage') == ""
        || document.getElementById('country') == "" )
        throw 'Input ERROR';
        else
        goAhead = 1;
    }
    catch{
        alert("Please enter/select values for every field");
    }
    
    console.log("fullTime "+inputData.length);
    if(goAhead == 1){
    try{
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
            
            if(outcome == "Approved"){
                document.getElementById("outcome").innerHTML = "Application is Approved";
            }
            else if (outcome == "Denied-R")
                document.getElementById("outcome").innerHTML = "Application is Denied as Role is not found";
            else if(outcome == "Denied-F") 
                document.getElementById("outcome").innerHTML = "Application is Denied as Employer is not found";
            else if(outcome == "Denied-B")
                document.getElementById("outcome").innerHTML = "Application is Denied as Employer is  Blacklisted";
            else if(outcome == "Denied-C")
                document.getElementById("outcome").innerHTML = "Application is Denied as Country is not found";
            else if(outcome == "Denied-CB")
                document.getElementById("outcome").innerHTML = "Application is Denied as Country is Blacklisted";
            else if(outcome == "Denied-E")
                document.getElementById("outcome").innerHTML = "Application is Denied as applicant doesnot have minimum qualification";
            else if(outcome == "Denied-S")
                document.getElementById("outcome").innerHTML = "Application is Denied as salary is less than prevailing wage";
            
    })      
    }
    catch{
        alert("Internal Server Error , Please try again");
        document.getElementById("employeeForm").style.display = 'none';
    }
}
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
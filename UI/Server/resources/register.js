const displayErrorText = () =>{
        
    document.getElementById("errors").style.display = "block";

    document.getElementById("errors").style.display = "Account already exists";

}

const backToLogin  = () =>{

    document.getElementById("forms").style.display = "none";
    document.getElementById("initialLogin").style.display = "block";

}

const addUser = () =>{

    let userName = document.getElementById("usernameR").value;
    let password = document.getElementById("passwordR").value;
    let retypedPassword = document.getElementById("reTypeR").value;

    console.log("Here "+userName +" "+password+" "+retypedPassword);

    if(password != retypedPassword){
            alert("Passwords do not match");
            clearForm(true);
    }
    else{
            let inputData = [];
            inputData.push(userName);
            inputData.push(password);
            var url = new URL("http://localhost:9000/addUser");
            url.search = new URLSearchParams({inputData : inputData });
            url = url.toString();
            console.log("URL "+url);
            fetch(url,{
                })
                .then(response => response.json())
                .then(data =>{
                    console.log("Data "+data);

                    if(data === "alreadyExists")
                    {
                            console.log("User Exists");
                            displayErrorText();
                    }
                    else{
                            //displaySuccessText(true);
                            displaySelection();  
                            alert("You have successfully been added");
                    }
                })
    }
}

var initializor = function () {
    var form = document.getElementById("stripe-login");
    function handleForm(event) {
        event.preventDefault();
    }
    if (form)
        form.addEventListener('submit', handleForm);
};

initializor();
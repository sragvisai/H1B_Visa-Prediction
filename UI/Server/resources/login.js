
const loadLogin = () => {
        document.getElementById("initialLogin").style.display="none";
        document.getElementById("forms").style.display = "block";
        document.getElementById("loginPage").style.display = "block";
        document.getElementById("register").style.display = "none";
}

const loadRegister = () => {
        document.getElementById("initialLogin").style.display="none";
        document.getElementById("forms").style.display = "block";
        document.getElementById("register").style.display = "block";
        document.getElementById("loginPage").style.display = "none";
}

const clearForm = (isRegister) => {
        if(isRegister){
                document.getElementById("usernameR").innerHTML= "";
                document.getElementById("passwordR").innerHTML= "";
                let retype = document.getElementById("reType");
                if(retype)
                        retype.innerHTML = "";
        }
        else{
                document.getElementById("userName").innerHTML= "";
                document.getElementById("password").innerHTML="";
        }
        
        
}

const backToLogin  = () =>{

        document.getElementById("forms").style.display = "none";
        document.getElementById("initialLogin").style.display = "block";

}

// const displaySuccessText = () => {

//         document.getElementById("success").style.display = "block";
//         document.getElementById("success").innerHTML="Successfully created an account , will redirect in few seconds";

// }
const displayErrorText = (isLogin) =>{
        
        document.getElementById("errors").style.display = "block";

        if(isLogin)
                document.getElementById("errors").innerHTML="Account already exists";
        else
                document.getElementById("errors").style.display = "Invalid username or passsword";

}

//allow the user to choose between the agent Form and Employer form

const displaySelection = () =>{
        var url = new URL("http://localhost:9000/selection");
        window.location.href = url;
}

const validateUser = () =>{
        let passwd = document.getElementById('password').value;
        let userName = document.getElementById('userName').value;
        let inputData = [];
        inputData.push(userName);
        inputData.push(passwd);

        var url = new URL("http://localhost:9000/validateUser");
        url.search = new URLSearchParams({inputData : inputData });
        url = url.toString();
        console.log("URL "+url);
        fetch(url,{
            })
            .then(response => response.json())
            .then(data =>{
                console.log("Data "+data);

                if(data === "Invalid"){
                        clearForm();
                        displayErrorText(false);
                }
                else{
                        clearForm();
                        //alert("You are a valid user");
                        displaySelection();    
                }
            })
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
                                clearForm(true);
                                displayErrorText(true);
                        }
                        else{
                                clearForm(true);
                                //displaySuccessText(true);
                                displaySelection();  
                                alert("You have successfully been added");
                        }
                    })
        }
}

var initializor = function () {
        var form = document.getElementById("loginPage");
        var regForm = document.getElementById("register");
        function handleForm(event) {
            event.preventDefault();
        }
        if (form)
            form.addEventListener('submit', handleForm);
        if(regForm)
        regForm.addEventListener('submit',handleForm);
};
    
initializor();

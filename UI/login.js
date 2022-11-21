
const loadLogin = () => {
        document.getElementById("initialLogin").style.display="none";
        document.getElementById("forms").style.display = "block";
        document.getElementById("loginPage").style.display = "block";
}

const loadRegister = () => {
        document.getElementById("initialLogin").style.display="none";
        document.getElementById("forms").style.display = "block";
        document.getElementById("register").style.display = "block";
}

const clearForm = (isRegister) => {
        if(isRegister){
                document.getElementById("userNameR").innerHTML= "";
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

const displayErrorText = (isLogin) =>{

        if(isLogin)
                document.getElementById("errorText").style.display = "block";
        else
                document.getElementById("errorTextReg").style.display = "block";

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
                        alert("You are a valid user");
                        
                }
            })
}

const addUser = () =>{

        let userName = document.getElementById("userNameR").value;
        let password = document.getElementById("passwordR").value;
        let retypedPassword = document.getElementById("reTypeR").value;

        console.log("Here "+userName +" "+password+" "+retypedPassword);

        if(password != retypedPassword){
                alert("Passwords do not match");
                clearForm();
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
                                clearForm();
                                displayErrorText(true);
                        }
                        else{
                                clearForm();
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
           form.addEventListener('submit',handleForm);
    };
    
initializor();

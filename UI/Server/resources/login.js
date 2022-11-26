
const loadLogin = () => {
        document.getElementById("initialLogin").style.display="none";
        document.getElementById("forms").style.display = "block";
        document.getElementById("loginPage").style.display = "block";
        document.getElementById("register").style.display = "none";
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
                        displayErrorText(false);
                }
                else{
                        //alert("You are a valid user");
                        displaySelection();    
                }
            })
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

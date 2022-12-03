const handleSubmit = () => {
    var selectedValue = document.getElementById('formChosen').value;
    console.log("Selected Value "+selectedValue);
    if(selectedValue == "Agent")
    {
        var url = new URL("http://localhost:9000/agentForm");
        window.location.href = url;
    }
    else
    {
        var url = new URL("http://localhost:9000/employeeForm");
        window.location.href = url;
    }
}

const initializor = () =>{
    var form = document.getElementById("app-cover");
        function handleForm(event) {
            event.preventDefault();
        }
        if (form)
            form.addEventListener('submit', handleForm);
}

initializor();
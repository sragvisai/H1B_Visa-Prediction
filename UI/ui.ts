console.log("Here");

const handleTheSubmit = () =>{
    console.log("Form submitted");
    var title = document.getElementById("Role")?.nodeValue;
    console.log(title);
}


const initializor = () =>{
    var form = document.getElementById("agentForm");
    function handleForm(event : any) { 
        event.preventDefault(); 
    } 
    if(form)
        form.addEventListener('submit', handleForm);
}

initializor();
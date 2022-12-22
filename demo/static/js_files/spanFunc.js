let span = document.querySelector(".login .footer p span");
span.addEventListener("click", goToRegister);
span.style.cursor= "pointer"

function goToRegister(){
    document.querySelector(".login").style.display = "none";
    document.querySelector(".register").style.display = "block";
    let needLogIn = document.querySelector(".need_log_in");
    if(needLogIn){
        document.querySelector(".need_log_in").style.display = "none";
    }

}
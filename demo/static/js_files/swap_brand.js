let buttons = document.querySelectorAll(".car-logo");

for (let button of buttons){
    button.addEventListener("click", swapBrand);
}

function swapBrand(value){
    let button = value.target.parentElement;
    let buttonName = button.name;
    let divs = document.querySelectorAll(".cars .mercedes,.bmw,.toyota,.audi");
    console.log(button.classList);
    for(let div of divs){
        if(div.style.display !== "none"){
            div.style.display = "none";
            break;
        }
    }

    for(let btn of buttons){
        for(let className of btn.classList){
            if(className === "active"){
                btn.classList.remove("active");
                break;
            }
        }
    }
     button.classList.add("active");


    if (buttonName === "mercedes"){
        document.querySelector(".mercedes").style.display = "flex";
    }else if(buttonName === "bmw"){
        document.querySelector(".bmw").style.display = "flex";
    }else if(buttonName === "audi"){
        document.querySelector(".audi").style.display = "flex";
    }
    else{
        document.querySelector(".toyota").style.display = "flex";
    }
}


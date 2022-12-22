let cart = document.querySelector(".cart");
let items = document.getElementsByClassName("items");

if(items.length > 0){
    let p = document.querySelector(".nothing");

    if (items[0].children.length - 1 === 2) {
        p.style.height = `50px`
    } else if (items[0].children.length - 1 === 3) {
        p.style.height = '0px';
        console.log("HI");
    }
}


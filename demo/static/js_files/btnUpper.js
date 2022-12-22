document.querySelector(".footer__btn").addEventListener("click", scrollTop);
let rootElement = document.documentElement;
function scrollTop(){
    rootElement.scrollTo({
        top:0,
        behavior: "smooth",
    })
}
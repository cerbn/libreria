inputsearch = document.getElementById("inputSearch");

document.getElementById("inputSearch").addEventListener("keyup", buscador_interno);

function buscar(){

    mayus = inputSearch.value.toUpperCase();
    li = box_search.getElementsByTagName("li");

    //Recorrer elementos "li"
    for (let i = 0; i < li.length; i++) {
        
        a = li[i].getElementsByTagName("a")[0];
        textValue = a.textContent || a.innerText;

        if(textValue.toUpperCase().indexOf(filter) > -1){
            li[i].style.display = "";
            box_search.style.display="block";

            if(inputSearch.value === ""){
                box_search.style.display= "none";
            }
        }else{
            li[i].style.display = "none";
        }
        
    }

}
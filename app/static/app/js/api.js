$(document).ready(function(){
    $("#enviar").click(function(){
        $.get("https://chroniclingamerica.loc.gov/search/titles/results/?terms=oakland&format=json&page=5",
            function(data){
            // En data se capturan todos los datos provenientes desde el servivio
            $.each(data.items, function(i, item){
            //Por cada elemento agregaremos una nueva fila en la tabla categorias
            $("#categoria").append("<tr><td>"+item.id+"</td>"+
                                    "<td>"+item.title+"</td>"+
                                    "<td>"+item.subject+"</td>"+
                                  "<td>"+item.city+"</td></tr>");
                                  
        });
    });
});
})
function cargarPlato(id) {
    const settings = {
        async: true,
        crossDomain: true,
        url: `https://the-mexican-food-db.p.rapidapi.com/${id}`,
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': '3fc7d68b27mshbc216747f913e22p1d91b3jsn27cbbf29c805',
            'X-RapidAPI-Host': 'the-mexican-food-db.p.rapidapi.com'
        }
    };

    $.ajax(settings).done(function (response) { /*solicitud api */
        mostrarCatalogo(response);
    });
}

function mostrarCatalogo(plato) { /*funcion para mostrar el catalogo  */
    const catalogoDiv = $('.catalogo'); /*buscar catalogo Dentro Div */
    const html = `
        <div class="item">
            <h3>${plato.title}</h3>  
            <img src="${plato.image}" alt="Foto de ${plato.title}">
            <p>${plato.description}</p>
        </div>
    `; /*title rescata el titulo, image la imagen y description la descripcion del alimento  */
    catalogoDiv.append(html); /*mostrar los platos  */
}

for (let i = 1; i <= 5; i++) { /*contador o for, cumple la funcion de remplazar el ${id} en el url para conseguir los distintos platillos*/
    cargarPlato(i);
}

const settings = {
	async: true,
	crossDomain: true,
	url: 'https://the-mexican-food-db.p.rapidapi.com/',
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'eefd68c301msh0471799391e3283p1dc96ejsnc91d9cf508b2',
		'X-RapidAPI-Host': 'the-mexican-food-db.p.rapidapi.com'
	}
};


$.ajax(settings).done(function (response) {
    console.log(response);
    console.log(response.title);

    $.each(response, function(i, item) {
        $("#Producto").append(`<tr> <!-- Este es el inico de un producto-->
        <td width="75">
          <td>
            <img src=${item.image} class="carrito">
          </td>
          <td class="desc">
            <h3> 
                ${item.title}
            </h3>
                <a href="#" class="text-muted"><i class="fa fa-trash"></i> Eliminar producto</a>
            </div>
        </td>
        </td>
        <td> 
          $2.990 c/u             
        </td>
        <td width="40"> <!-- cuantos productos quieres--> 
          <input type="text" class="form-control" placeholder="1">
        </td>
        <td>
          <h4>
              $2.990 <!-- precio final-->
          </h4>
      </td>
      </tr><!--Final del producto-->          `);
    });
});
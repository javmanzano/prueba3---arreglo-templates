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
        $("#Lista").append(`<div class="col mb-4">
        <div class="card">
            <img src="${item.image}" class="card-img-top" alt="...">
            <div class="card-body">
            <h5 class="card-title">${item.title}</h5>
            </div>
        </div>
        </div>`);
    });
});
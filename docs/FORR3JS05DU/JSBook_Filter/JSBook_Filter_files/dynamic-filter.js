(function() {

	// Sækja krækjur í HTML
	const $slider = $("#slider")//document.getElementById("slider");
	const table = document.getElementById("rates");// hérna sæki ég staðsetningu töflunar í HTML-inu
	const $min = $('#value-min');// Hérna sæki ég min staðsetninguna og það þarf að vera jQery breyta vegna þess að hún ver í gegnum listenerinn sem breytir henni þegar sliderinn hreyfist
	const $max = $('#value-max');// Hérna sæki ég max staðsetninguna og það þarf að vera jQery breyta vegna þess að hún ver í gegnum listenerinn sem breytir henni þegar sliderinn hreyfist

	// STORE EACH PERSON AS AN OBJECT IN AN ARRAY
	let people = [
		{                                              // Each person is an object
			name: 'Casey',                               // It holds name and rate
			rate: 60
		},
		{
			name: 'Camille',
			rate: 80
		},
		{
			name: 'Gordon',
			rate: 75
		},
		{
			name: 'Nigel',
			rate: 120
		},
		{
			name: 'Casey',
			rate: 10
		},
		{
			name: 'Camille',
			rate: 35
		},
		{
			name: 'Gordon',
			rate: 95
		},
		{
			name: 'Nigel',
			rate: 145
		}
	];

	let rows = [];// Þetta geymir allar raðirnar fyrir töfluna sem er stýrt af sliderinum 
	function makeRows() {// Þetta fall býr til raðir fyrir alla í arrayinum people (alla)
		people.forEach(person => {
			let row = buaTilElement("tr");
			buaTilElement("td", person.name, row);
			buaTilElement("td", person.rate, row);
			rows.push({
				person: person,
				element: row
			});
		});
	}

	function appendRows() {
		let tbody = buaTilElement("tbody");
		rows.forEach(row => {
			tbody.appendChild(row.element);
		});
		table.appendChild(tbody);
	}

	function update(min, max) {
		rows.forEach(row => {
			if (row.person.rate >= min && row.person.rate <= max) {
				row.element.hidden = false;
			} else {
				row.element.hidden = true;
			}
		});
	}

	let buaTilElement = (element, texti = false, foreldri = false) => {
		let item = document.createElement(element);
		
		if (texti !== false) {
			let texta_element = document.createTextNode(texti);
			item.appendChild(texta_element);
		}
		if (foreldri !== false) {
			foreldri.appendChild(item);
		} else {
			return item;
		}
	}

	function init() {
		$slider.noUiSlider({
			range: [0, 150],
			start: [65, 90],
			handles: 2,
			margin: 20,
			connect: true,
			serialization: {
				to: [$min, $max],
				resolution: 1
			}
		}).change(() => { update($min.val(), $max.val()); });
		makeRows();
		appendRows();
		update($min.val(), $max.val());
	}

	init();
}());
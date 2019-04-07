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
		people.forEach(person => {// Þetta keyrir einu sinni fyrir hvern í arrayinum people
			let row = buaTilElement("tr");
			buaTilElement("td", person.name, row);
			buaTilElement("td", person.rate, row);
			rows.push({// Þetta bætir objectinum sem er verið að búa til í arrayin rows
				person: person,
				element: row
			});
		});
	}

	function appendRows() {// Þetta fall bætir röðunum sem er búið að búa til í makeRows í töflu og setir töfluna á skjáinn
		let tbody = buaTilElement("tbody");
		rows.forEach(row => {// Þetta keyrir einu sinni fyrir hvern hlut í rows
			tbody.appendChild(row.element);// Þetta bætir hlutunum sem voru búnir til í makeRows við tbody
		});
		table.appendChild(tbody);// Þetta bætir tbody við töfluna table
	}

	function update(min, max) {// Þetta tékkar á hverja röð og ef hún er ekki á milli talnana min og max þá er hún falin, annars er hún birt
		rows.forEach(row => {// Þetta keyrir einu sinni fyrir hvern hlut í rows
			if (row.person.rate >= min && row.person.rate <= max) {// Þetta keyrir ef röðin er á milli min og max
				row.element.hidden = false;// Þetta sýnir röðina sem er verið að fara í gegnum
			} else {
				row.element.hidden = true;// Þetta felur röðina sem er verið að fara í gegnum
			}
		});
	}

	let buaTilElement = (element, texti = false, foreldri = false) => {// Þetta fall býr til element en það þarf ekki endilega að senda inn neitt nema hvernig hlut þér langar í
		let item = document.createElement(element);// hérna er hluturinn búinn til
		
		if (texti !== false) {// Þetta keyrir ef það var sendur texti með
			let texta_element = document.createTextNode(texti);// Hérna er textinn búin til
			item.appendChild(texta_element);// Hérna er bætt textanum undir hlutin sem er verið að búa til
		}
		if (foreldri !== false) {// Þetta keyrir ef það var sent foreldri með
			foreldri.appendChild(item);// Hérna er bætt hlutnum við foreldrið sem var sent inn
		} else {
			return item;// Hérna er skilað hlutnum ef það var ekki send neitt foreldri með
		}
	}

	function init() {
		$slider.noUiSlider({// Hérna er sliderinn búin til með JQuery
			range: [0, 150],
			start: [65, 90],
			handles: 2,
			margin: 20,
			connect: true,
			serialization: {
				to: [$min, $max],
				resolution: 1
			}
		}).change(() => { update($min.val(), $max.val()); });// Þetta keyrir fallið update með gildunum á $min og $max breytunum
		makeRows();
		appendRows();
		update($min.val(), $max.val());
	}

	init();
}());
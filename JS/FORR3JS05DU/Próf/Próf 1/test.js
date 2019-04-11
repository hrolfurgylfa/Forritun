// Prototype
function Book(nafn) {
	this.nafn = nafn;
}
let Book.prototype.faNafn = function() {
	console.log(this.nafn);
}




// Búðu til object sem geymir upplýsingar um þig; nafn, kennitala, heimilisfang og netfang.
eg = {
	nafn: "Hrólfur",
	kennitala: "2308037390",
	heimilisfang: "Haldórsgata 57",
	netfang: "hrolfur@hrolfur.is"
}

// Skrifaðu kóðann fyrir eftirfarandi DOM tré (sjá mynd)  e. text og e. attribute  má vera tómt.
<!Doctype HTML>
<html>
	<body>
		<div class="">
			<h1 class="">Texti</h1>
			<h2>Texti</h2>
			<ul>
				<li id=""><em>Texti</em>Texti</li>
				<li id="">Texti</li>
				<li id="">Texti</li>
				<li id="">Texti</li>
			</ul>
			<script id=""></script>
		</div>
	</body>
</html>

// Notaðu smið ( e. function constructor ) sem geymir upplýsingar um þig; nafn, kennitala, heimilisfang og tvö netföng. Netföngin eiga að vera í fylki.

function eg(nafn, kennitala, heimilisfang, netfang1, netfang2) {
    this.nafn = nafn;
	this.kennitala = kennitala;
	this.heimilisfang = heimilisfang;
	this.netfong = [netfang1, netfang2];
}
Book.prototype.getName = function() {
    console.log(this.nafn);
}

// Afhverju er getElementById() fljótleglegasta aðferðin?
getElementByID er fljótlegasta aðferðin til þess að krækja í HTML vegna þess að þegar vafrinn finnur fyrsta ID-ið á DOM trénu hættir vafrinn að leita að því en með því að leita að class eða nafni(<div>) þá er ekki hætt að leita fyrr en það er búið að fara í gegnum allt DOM tréð.

//Komdu með kóðadæmi sem sprengir staflann (e. stack overflow).
let a = strengur => {
	strengur += "a";
	b(strengur);
}
let b = strengur => {
	strengur += "b";
	a(strengur);
}
a("");

// Hvað birtist í console?
let area = ( function () { 
                 let width = 3;
                 let height = 2;
                 return width * height; 
            } )();

area;

// Búðu til klasa (class) User sem hefur nafn og netfang. Klasinn hefur einnig get og set aðferð fyrir nafn.
class User() {
	constructor(nafn, netfang) {
		this.nafn = nafn;
		this.netfang = netfang;
	}
	get() {
		return this.nafn;	
	}
	set(nafn) {
		this.nafn = nafn;
	}
}

// Notaðu  filter aðferðin með fylkinu tolur og birtu tölur í console sem eru stærri en 10 en minni en 50.
let tolur = [12, 92, 4, 14];

console.log(filter(tolur,tala => if (tala > 10 && tala < 50) {return;}));

// Útskýrðu eftirfarandi kóða línu fyrir línu útfrá raunkeyrslu (e. runtime) JavaScript þýðandans (Hvað er keyrt fyrst og hvað gerir sá kóði, hvað gerist svo næst osfrv.)
function a(callBack){     
  callBack(); 
} 
function b(){     
  console.log('Hello world!'); 
} 
a(b);


a(b);// fallið a keyrt og fallið b sent inn með
{ // nafninu á falli b breytt í callBack á meðan forritið er inni í falli a
	callBack();// Fallið b keyrt inni í fallinu a
	{
		console.log('Hello world!'); // consolin prenntar út hello world
	}// Farið aftur í fall a
}// Farið út úr falli a sem er síðasta fallið í stack-anum

// Búðu til object sem geymir upplýsingar um hótel og aðferð.
let hotel = {
	nafn = "Hótel Hreins",
	fjoldi_herbergja = 20,
	fjoldi_herbergja_bokud = 1,
	sundlaug = false,
	fjoldi_lausra_herbergja = () => return this.fjoldi_herbergja - this.fjoldi_herbergja_bokud;
}

// Object that creates de Dropdown bar

alberta = ["Calgary","Edmonton Area"];
britishc = ["Greater Vancouver Area","Kelowna","Victoria"];
manitoba = ["Winnipeg"];
nova = ["Halifax"];
ontario = ["Barrie","Hamilton","Ottawa/ Gatineua Area", "Toronto"];
quebec = ["Greater Montr\u00e9al","Qu\u00e9bec City"];
sas = ["Regina Area"];

function Dropdown(object){

    this.options = object;

    window.getparent = function(element){
        var id = element.closest('.dropdown').parentElement.id;
        console.log(window.dropdowns[id])
        return window.dropdowns[id];
    }

    this.init = function(){
        // Searching the id

        this.element = document.getElementById(this.options.id);

        //Creating the base html

        var value = this.options.val;
        var phrase = this.options.phrase;
        var html = '<h2>' + phrase + '</h2>'+'<div class = "dropdown"><div class = "dropdown_value" id = "NULL">'+ value + '</div>'
                        + '<div class = "dropdown_arrow"> ↧</div><div class = "dropdown_panel"><div class = "dropdown_items"></div></div>';
        this.element.innerHTML = html;

        // Store a hash of dropdowns

        if (!window.dropdowns) window.dropdowns ={};
        window.dropdowns[this.options.id] = this;

        // Get elements

        this.panel = this.element.querySelector('.dropdown_panel');
        this.items = this.element.querySelector('.dropdown_items');
        this.arrow = this.element.querySelector('.dropdown_arrow');
        this.value = this.element.querySelector('.dropdown_value');

        //Populate dropdown items
        var data = this.options.data;
        var html = "";
        if (this.options.id != "dd2"){
            data.forEach((element,i) => {
                html += '<div class = "dropdown_item" id = '+ i +' onmousedown =  "var self = getparent(this); self.clicked(this)"> '+ element +' </div>'
            });
        }
        else{
            data.forEach((element,i) => {
                html += '<div class = "dropdown_item" id = '+ i +' onmousedown =  "var self = getparent(this); self.clicked(this)"> '+ element +' </div>'
            });
        }
        console.log(html);
        this.items.innerHTML = html;

        //Events
        var self = this;
        this.element.addEventListener('mousedown', (e)=>{
                    if (self.isVisible){
                        if  (e.target.className == "dropdown_item")
                            self.hide();
                    }
                    else
                        self.show();
        });
    }

    this.init();

    this.clicked = function(element){
        event.stopPropagation();
        this.hide();

        var newval = element.innerHTML;
        this.value.innerHTML = newval;
        this.value.id = element.id;
    }
    this.show = function(){
        this.isVisible = true;
        this.items.style.transform = 'translate(0,0%)';
        this.arrow.style.transform = 'rotate(180deg)';
        this.panel.style.height = '400%' ;
    }

    this.hide = function(){
        this.isVisible = false;
        this.items.style.transform = 'translate(0,-100%)';
        this.arrow.style.transform = 'rotate(0deg)';
        this.panel.style.height = '100%' ;
    }

    return this;
}


var menu = new Dropdown({
    id: "dd1",
    phrase: "Choose state",
    val:"Location",
    data:   ["Alberta",
    "British Columbia",
    "Manitoba",
    "Nova Scotia",
    "Ontario",
    "Qu\u00e9bec",
    "Regina Area"]
});

var menu2 = new Dropdown({
    id: "dd2",
    phrase: "Choose City",
    val:"City",
    data:['-']
});


const button = document.getElementById('dd1');
const div2 = button.firstChild.nextSibling;
let drop = div2.firstChild;

function hi(){
    let value = drop.innerHTML;
    //let value =  div.querySelector('.dropdown_value');
    console.log(value)
}

// This function selects the correct menu according
// to the state we select.
observer = new MutationObserver(function(mutationsList, observer) {
    var list;
    let value = drop.id;
    value = String(value)
    while (dd2.hasChildNodes())
        dd2.firstChild.remove()
    switch(value){
        case "0":
            console.log("1");
            list = alberta.slice();
            break;
        case "1":
            list = britishc.slice();
            break;
        case "2":
            list = manitoba.slice();
            break;
        case "3":
            list = nova.slice();
            break;
        case "4":
            list = ontario.slice();
            break;
        case "5":
            list = quebec.slice();
            break;
        case "6":
            list = sas.slice();
            break;
        default:
            console.log('hi')
    }
    var menu2 = new Dropdown({
        id: "dd2",
        phrase: "Choose City",
        val:"City",
        data:list
    });
});

observer.observe( drop, {characterData: false, childList: true, attributes: false});

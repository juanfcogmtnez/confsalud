// tree data
var data;
data = [{
  text: "Products",
  data: {},
  children: [{
    text: "Fruit",
    data: {}, 
    children:[
      {text: "Apple", data: {price: 0.1, quantity: 20}},
      {text: "Banana", data: {price: 0.2, quantity: 31}},
      {text: "Grapes", data: {price: 1.99, quantity: 34}},
      {text: "Mango", data: {price: 0.5, quantity: 8}},
      {text: "Melon", data: {price: 0.8, quantity: 4}},
      {text: "Pear", data: {price: 0.1, quantity: 30}},
      {text: "Strawberry", data: {price: 0.15, quantity: 32}}
    ],
    'state': {'opened': true}
  }, {
    text: "Vegetables",
    data: {}, 
    children:[
      {text: "Aubergine", data: {price: 0.5, quantity: 8}},
      {text: "Broccoli", data: {price: 0.4, quantity: 22}},
      {text: "Carrot", data: {price: 0.1, quantity: 32}},
      {text: "Cauliflower", data: {price: 0.45, quantity: 18}},
      {text: "Potato", data: {price: 0.2, quantity: 38}}
    ]
  }],
  'state': {'opened': true}
}];

// load jstree
$("div#jstree").jstree({
  plugins: ["table","dnd","contextmenu","sort"],
  core: {
    data: data
  },
  // configure tree table
  table: {
    columns: [
      {width: 200, header: "Name"},
      {width: 150, value: "price", header: "Price", format: function(v) {if (v){ return '$'+v.toFixed(2) }}},
      {width: 150, value: "quantity", header: "Qty"}
    ],
    resizable: true,
    draggable: true,
    contextmenu: true,
    width: 500,
    height: 300
  }
});
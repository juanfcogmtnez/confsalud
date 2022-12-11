$.ajax({url: "/titulo", success: function(result){
  titulo = JSON.parse(result);
  console.log(titulo);
  longo = titulo.length;
  cons = $("#menu2nd").text();
  for (let i=0;i< longo;i++){
      option = '<a class="dropdown-item" href="/todos/'+titulo[i]+'/'+cons+'">'+titulo[i]+'</a>';
      $("#selbase").append(option);
  }
}});


$.ajax({url: "/cons", success: function(result){
  titulo = JSON.parse(result);
  console.log(titulo);
  longo = titulo.length;
  proy = $("#menu1st").text();
  for (let i=0;i< longo;i++){
      option = '<a class="dropdown-item" href="/todos/'+proy+'/'+titulo[i]+'">'+titulo[i]+'</a>';
      $("#selbuild").append(option);
  }
}});


$.ajax({url: "/datatemp/plane", success: function(result){
console.log(result);
if (result=="ok"){
$("#plane").show();
}
}});

function guardatemp(par){
  $('#jstree2').jstree('open_all');
  list = document.getElementById('jstree2').getElementsByTagName('li');
  nombre = list[0].children[1].children[2].innerHTML;
  file = [];
  for(let i = 0;i<list.length;i++){
    ident = list[i].id;
    obj = "#"+ident;
    parent = $(obj).parent().parent().attr('id');
    if (parent == "jstree2" || parent == "jstree"){
      parent = "#";
    }
    console.log('parent',parent);
    console.log('ident',ident);
    contenido = list[i].children[1].children;
    console.log('contenido',contenido);
    texto = '';
    for (let x=1;x<contenido.length;x++){
      texto = texto + contenido[x].outerHTML;
    }
    console.log('texto',texto);
    dict = {'id':ident,'parent':parent,'texto':texto};
    file.push(dict);
  }
  console.log("file",nombre,file);
  
  if (nombre == 'blanco' || nombre == 'Blanco'){
    alert("El nombre del proyecto no puede ser "  +nombre + "\n Por favor cambie el nombre del proyecto");
  }
  else{
    $('#otherModal').modal('show');
    $('#otherModal').modal({backdrop: 'static', keyboard: false});
    $("#omtit").text("Espere mientras se guardan los datos");
    $.ajax({
      type: "POST",
      contentType: "application/json; charset=utf-8",
      url: "/guardatemp",
      data: JSON.stringify({"file":file,"nombre":nombre}),
      dataType: "json"
    });
  proy = $("#menu1st").text();
  if (par=='si'){
  window.location.assign("/todos/"+proy+"/"+nombre);
}
}
}


$('#jstree').jstree({
  "core" : {
    "animation" : 0,
    "check_callback" : true,
    "themes" : { "stripes" : true },
    'data' : {
      'url' : function (node) {
          proy = $("#menu1st").text();
          console.log("proy:",proy);
          return node.id === '#' ?
            '/static/json/'+proy+'.json' : '/static/json/'+proy+'.json' ;
      },
      'data' : function (node) {
        console.log('node',node.li_attr);
        return { 'id' : node.id ,'name':node.name,'parent':node.parent};
      }
    }
  },
  "plugins" : [
     "search","contextmenu","dnd","crrm"
  ],
                  "search": {
                    "case_sensitive": false,
                    "show_only_matches": true
                }
});

    $('#jstree2').jstree({
      "core" : {
        "animation" : 0,
        "check_callback" : true,
        "themes" : { "stripes" : true },
        'data' : {
          'url' : function (node) {
              cons = $("#menu2nd").text();
              console.log("proy:",cons);
              return node.id === '#' ?
                '/static/json/temp/'+cons+'.json' : '/static/json/temp/'+cons+'.json' ;
          },
          'data' : function (node) {
            console.log(node);
            return { 'id' : node.id ,'name':node.name,'parent':node.parent};
          }
        }
      },
      "plugins" : [
        "search","contextmenu","dnd","crrm"
      ],
                      "search": {
                        "case_sensitive": false,
                        "show_only_matches": true
                    },
                    
    });
    
      $("#jstree2").on("select_node.jstree", function (e, data) {
          console.log("data-selected",data.selected);
          obj = data.selected
          lista = document.getElementById(data.selected).children[1].children;
          console.log(lista);
          console.log('lista',lista);
          $('#modal-body').html('');
          $('#modal-body').append('<input id="hideid" type="hidden" value="'+data.selected+'">');
          for (let i=1; i<lista.length;i+=2){
            $('#modal-body').append('<label style="font-weight:bold">'+$(lista[i]).text()+'</label><input type="text" class="form-control" id="name" value="'+$(lista[i+1]).text()+'">');
          }
          title = $(lista[2]).text();
          console.log(title);
          $('#tit').text(title);
          $('#myModal').modal('toggle');
      });

        $('#guardarmodal').click(function(){
          listamodal = $('#modal-body').children();
          obj = listamodal[0].defaultValue;
          console.log(obj);
          obj = '#'+obj;
          lista = $(obj).children().children();
          console.log(lista);
          for (let i=1; i<lista.length;i+=2){
            console.log(lista[i]);
            console.log(listamodal[i]);
            $(lista[i]).text($(listamodal[i]).text());
            $(lista[i+1]).text($(listamodal[i+1]).val());
          }
          guardatemp('si');
          $('#myModal').modal('toggle');
        })
      
   $("#btpl").keyup(function () {
          var searchString = $(this).val();
          $('#jstree').jstree('search', searchString);
    });

    $("#bbuild").keyup(function () {
      var searchString = $(this).val();
      $('#jstree2').jstree('search', searchString);
  });

  $("#borramodal").click(function(){
    var obj = $("#hideid").val();
    console.log(obj);
    $('#jstree2').jstree().delete_node(obj);
    guardatemp();
  });

  function guardadef(){
    guardatemp('no');
    $('#jstree2').jstree('open_all');
    list = document.getElementById('jstree2').getElementsByTagName('li');
    nombre = list[0].children[1].children[2].innerHTML;
    file = [];
    for(let i = 0;i<list.length;i++){
      ident = list[i].id;
      obj = "#"+ident;
      parent = $(obj).parent().parent().attr('id');
      if (parent == "jstree2"){
        parent = "#";
      }
      console.log('parent',parent);
      console.log('ident',ident);
      contenido = list[i].children[1].children;
      console.log('contenido',contenido);
      texto = '';
      for (let x=1;x<contenido.length;x++){
        texto = texto + contenido[x].outerHTML;
      }
      console.log('texto',texto);
      dict = {'id':ident,'parent':parent,'texto':texto};
      file.push(dict);
    }
    console.log("file",nombre,file);
    $.ajax({url: "/titulo", success: function(result){
      titulo = JSON.parse(result);
      console.log("temps",titulo);
      repetido = "";
      for (let y=1;y<titulo.length;y++){
        if (nombre.toLowerCase() == titulo[y].toLowerCase()){
          alert("El nombre del proyecto no puede ser "  +nombre + "\n Por favor cambie el nombre del proyecto");
          repetido = "si";

        }
      }
      if (repetido != "si"){
        $('#otherModal').modal('show');
        $('#otherModal').modal({backdrop: 'static', keyboard: false});
        $("#omtit").text("Espere mientras se guardan los datos");
        $.ajax({
          type: "POST",
          contentType: "application/json; charset=utf-8",
          url: "/guardadef",
          data: JSON.stringify({"file":file,"nombre":nombre}),
          dataType: "json",
        });
      cons = $("#menu2nd").text();
      window.location.assign("/todos/"+nombre+"/"+cons);
    }
    }}); 



  }
  
  function planeb(){
    obj = $("#menu2nd").text();
    $('#otherModal').modal('show');
    $('#otherModal').modal({backdrop: 'static', keyboard: false});
    $("#omtit").text("Espere mientras se genera el archivo");
    $.get("/planeb/"+obj, function(data){
      console.log(data);
      if (data=="ok"){
        $('#otherModal').modal('hide');
        window.open("/static/datatemp/temp.xlsx",target="_blank");
      }
    });
    

}

function planabc(){
  obj = $("#menu2nd").text();
  $('#otherModal').modal('show');
  $('#otherModal').modal({backdrop: 'static', keyboard: false});
  $("#omtit").text("Espere mientras se genera el archivo");
  $.get("/planabc/"+obj, function(data){
    console.log(data);
    if (data=="ok"){
      $('#otherModal').modal('hide');
      window.open("/static/databc/temp.xlsx",target="_blank");
    }
  });
  

}

  function planep(){
    obj = $("#menu1st").text();
    planespacios(obj);
  }
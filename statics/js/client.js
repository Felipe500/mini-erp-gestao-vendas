$(document).ready(function(){
    update_list_client(1);

 });
$(function(){
  $('#datepicker').datepicker();
});


function update_list_client(page=1, on_delete=false){
    var number_page = page;
    var count_itens = parseInt($('#id_page_itens').val());
    let url = ''
    query =  $("#id_query").val();
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);

    console.log("page: ", number_page);
    console.log("itens page: ", $('#id_page_itens').val());

    if (urlParams.has('page')){
        number_page = urlParams.get('page')
    }
    if (count_itens==1 && number_page>1 && on_delete==true){
        number_page = number_page - 1;
        console.log("page: ", number_page);
    }
    if (query!==''){
        url = '/clientes/list_client/?query='+query+'&page='+number_page
        console.log("exist query: ", query);
    } else {
        url = '/clientes/list_client/?page='+number_page
    }

    $.ajax({
        type: 'GET',
        url: url,
        data: {},
        success: function(data){
                $("#list_clients").html(data);
                console.log("sucesso: ");
            },
        error: function (response, status, error) {
                console.log("error: ");
                if (response.status == 403){
                    $('#container_page').empty();
                    $('#container_page').html("<h3 class='header_text'> Acesso Não Autorizado</h3>");
                } else {
                    $('#container_page').empty();
                    $('#container_page').html("<h3 class='header_text'> Erro Interno </h3>");  
                }
        }
    });
}


function modal_delete_client(id_client, name_client, count_itens){
    let link_delete = id_client;
    console.log(link_delete);

    $.ajax({
        type: 'GET',
        url: '/clientes/delete/'+id_client+'/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Confirmação!');
            $('.modal-body').empty();
            $('.modal-body').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Deletar Cliente");

            $("#button_action").removeClass().addClass('btn btn-danger')
            $('#button_action').attr('onclick','delete_client('+ link_delete+')').unbind('click');
        },
        error: function (xhr, status, error) {
            if (xhr.status == 403){
                $('#title_modal').empty();
                $('#title_modal').append('Você não tem permissão!');
                $("#button_action").removeClass().addClass('hidden')
            }
             console.log(xhr.status);
             console.log(error);
        }
    });
}

function delete_client(id){
    var number_page = parseInt($('#id_page_index').val());
    var token = $('input[name="csrfmiddlewaretoken"]');
    $.ajax({
        method: "POST",
        url: '/clientes/delete/'+id+'/',
        data: $('#client_form_'+id).serialize(),

        success: function (data) {
            if (data.deleted) {
                update_list_client(number_page, true);
            }
        }
     });
}


function view_client(id_client){
    $.ajax({
        type: 'GET',
        url: '/clientes/view_client/'+id_client+'/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Dados do Cliente');
            $('.modal-body').empty();
            $('.modal-body').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Editar Cliente");
            $("#button_action").removeClass().addClass('btn btn-warning text-white d-none')
            $('#button_action').attr('onclick',"location.href='/clientes/update/"+id_client+"/'").unbind('click');
            $('#id_birth_date').val($('#id_birth_date').val());
        }
    });
}


function view_update_client(id_client, name_client){
    $.ajax({
        type: 'GET',
        url: '/clientes/update/'+id_client+'/',
        data: {},
        success: function(data, statuscode){
            $('#title_modal').empty();
            $('#title_modal').append('Editar Cliente - '+name_client);
            $('.modal-body').empty();
            $('.modal-body').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Editar");
            $("#button_action").removeClass().addClass('btn')
            $("button_action").css("background-color", "#fd7700");
            $('#button_action').attr('onclick','update_client('+ id_client+')').unbind('click');
        }
    });
}

function update_client(id_client){
    var number_page = parseInt($('#id_page_index').val());
    if (isNaN(number_page)) {
        number_page = 1;
    }
    $.ajax({
        method: "POST",
        url: '/clientes/update/'+id_client+'/',
        data: $('#client_form_'+id_client).serialize(),

        success: function (data) {
            if (data.updated) {
                console.log("atualizado com sucesso!");
                update_list_client(number_page);
                $('#modal_client').modal('hide');
            } else {
                console.log("error ao atualizar!");
                $('.modal-body').empty();
                $('.modal-body').html(data);

            }
        }
     });
}

function view_create_client(){
    $.ajax({
        type: 'GET',
        url: '/clientes/create/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Adicionar Novo Cliente');
            $('.modal-body').empty();
            $('.modal-body').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Adicionar");
            $("#button_action").removeClass().addClass('btn btn-primary text-white')
            $('#button_action').attr('onclick','create_client()').unbind('click');
        }
    });
}

function create_client(){
    var number_page = parseInt($('#id_page_index').val());
    if (isNaN(number_page)) {
        number_page = 1;
    }
    $.ajax({
        method: "POST",
        url: '/clientes/create/',
        data: $('#client_form_0').serialize(),

        success: function (data) {

            if (data.created) {
                console.log("atualizado com sucesso!");
                update_list_client(number_page);
                $('#modal_client').modal('hide');
            } else {
                console.log("error ao cadastrar!");
                $('.modal-body').empty();
                $('.modal-body').html(data);

            }
        }
     });
}
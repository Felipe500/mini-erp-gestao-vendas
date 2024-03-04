function modal_create_product(){
    $.ajax({
        type: 'GET',
        url: '/produtos/create/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Adicionar Novo Produto');
            $('#body_modal_view').empty();
            $('#body_modal_view').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Adicionar");
            $('#button_action').removeAttr('style');
            $("#button_action").removeClass().addClass('btn btn-primary text-white')
            $('#button_action').attr('onclick','create_product()').unbind('click');
        }
    });
}

function modal_delete_product(id_product, name_product){
    let link_delete = id_product;
    console.log(id_product);

    $.ajax({
        type: 'GET',
        url: '/produtos/delete/'+id_product+'/',
        data: {},
        success: function(data){
                $('#title_modal').empty();
                $('#title_modal').append('Confirmação!');
                $('#button_action').empty();
                $('#button_action').append("Deletar");
                $("#button_action").removeClass().addClass('btn btn-danger')
                $('#body_modal_view').empty();
                $('#body_modal_view').html(data);
                $('#button_action').removeAttr("onclick");
                $('#button_action').removeAttr('style');
                $('#button_action').attr('onclick','delete_product('+ id_product+')').unbind('click');
        }
    });

}

function modal_update_product(id_product, name_client){
    $.ajax({
        type: 'GET',
        url: '/produtos/update/'+id_product+'/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Editar Produto - '+name_client);
            $('#body_modal_view').empty();
            $('#body_modal_view').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Editar");
            $("#button_action").removeClass().addClass('btn')
            $("#button_action").css({"background-color": "#ffc107", "color": "white"});
            $('#button_action').attr('onclick','update_product('+ id_product+')').unbind('click');
        }
    });
}

function modal_view_product(id_product){
    $.ajax({
        type: 'GET',
        url: '/produtos/view_product/'+id_product+'/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Dados do Produto');
            $('#body_modal_view').empty();
            $('#body_modal_view').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Editar Cliente");
            $('#button_action').removeAttr('style');
            $("#button_action").removeClass().addClass('btn btn-warning text-white d-none')
            $('#button_action').attr('onclick','update_client('+ id_product+ ')').unbind('click');
            console.log("deu certo: ");
        }
    });
}

function create_product(){
    var number_page = parseInt($('#id_page_index').val());
    $.ajax({
        method: "POST",
        url: '/produtos/create/',
        data: $('#product_form_0').serialize(),

        success: function (data) {

            if (data.created) {
                console.log("atualizado com sucesso!");
                update_list_products(number_page, true);
                $('#modal_view').modal('hide');
            } else {
                console.log("error ao cadastrar!");
                $('#body_modal_view').empty();
                $('#body_modal_view').html(data);

            }
        }
     });
}

function delete_product(id){
    var number_page = parseInt($('#id_page_index').val());
    $.ajax({
        method: "POST",
        url: '/produtos/delete/'+id+'/',
        data: $('#product_form_'+id).serialize(),
        success: function (data) {
            if (data.deleted) {
                console.log('deletado com sucesso');
                update_list_products(number_page, true);
                $('#modal_view').modal('hide');
            } else {
                console.log("error ao atualizar!");
                $('#body_modal_view').empty();
                $('#body_modal_view').html(data);

            }
        }
     });
}

function update_product(id_client){
    var number_page = parseInt($('#id_page_index').val());
    var token = $('input[name="csrfmiddlewaretoken"]');
    $.ajax({
        method: "POST",
        url: '/produtos/update/'+id_client+'/',
        data: $('#product_form_'+id_client).serialize(),

        success: function (data) {
            if (data.updated) {
                console.log("atualizado com sucesso!");
                update_list_products(number_page, true);
                $('#modal_view').modal('hide');
            } else {
                console.log("error ao atualizar!");
                $('#body_modal_view').empty();
                $('#body_modal_view').html(data);

            }
        }
     });
}


function update_list_products(page=1, on_delete=false){
    var number_page = page;
    console.log("page: ", number_page);
    let url = '';
    query =  $("#id_query").val();
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    var count_itens = parseInt($('#id_page_itens').val());
    console.log("itens page: ", $('#id_page_itens').val());

    $("#id_search").hide();
    $("#loading_search").show();
    console.log('query > ', query)

    if (count_itens == 1 && number_page>1 && on_delete==true){
        number_page = number_page - 1;
        console.log("new page itens: ", number_page);
    }
    if (query!==''){
        url = '/produtos/list_products/?query='+query+'&page='+number_page
        console.log("exist: ", urlParams);
    } else {
        url = '/produtos/list_products/?page='+number_page
    }

    $.ajax({
        type: 'GET',
        url: url,
        data: {},
        success: function(data){
            $("#list_products").html(data);
            $("#loading_search").hide();
            $("#id_search").show();
        }
    });
}


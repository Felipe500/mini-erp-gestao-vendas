function modal_create_category(){
    $.ajax({
        type: 'GET',
        url: '/produtos/category_create/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Adicionar Nova Categoria');
            $('#body_modal_view').empty();
            $('#body_modal_view').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Adicionar");
            $('#button_action').removeAttr('style');
            $("#button_action").removeClass().addClass('btn btn-primary text-white')
            $('#button_action').attr('onclick','create_category()').unbind('click');
        }
    });
}

function modal_delete_category(id_category, name_category){
    let link_delete = id_category;
    console.log(id_category);

    $.ajax({
        type: 'GET',
        url: '/produtos/category_delete/'+id_category+'/',
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
                $('#button_action').attr('onclick','delete_category('+ id_category+')').unbind('click');
        }
    });

}

function modal_update_category(id_category, name_category){
    $.ajax({
        type: 'GET',
        url: '/produtos/category_update/'+id_category+'/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Editar Produto - '+name_category);
            $('#body_modal_view').empty();
            $('#body_modal_view').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Editar");
            $("#button_action").removeClass().addClass('btn')
            $("#button_action").css({"background-color": "#ffc107", "color": "white"});
            $('#button_action').attr('onclick','update_category('+ id_category+')').unbind('click');
        }
    });
}


function create_category(){
    var number_page = parseInt($('#id_page_index').val());
    $.ajax({
        method: "POST",
        url: '/produtos/category_create/',
        data: $('#category_form_0').serialize(),

        success: function (data) {

            if (data.created) {
                console.log("atualizado com sucesso!");
                update_list_category(number_page, true);
                $('#modal_view').modal('hide');
            } else {
                console.log("error ao cadastrar!");
                $('#body_modal_view').empty();
                $('#body_modal_view').html(data);

            }
        }
     });
}

function delete_category(id){
    var number_page = parseInt($('#id_page_index').val());
    $.ajax({
        method: "POST",
        url: '/produtos/category_delete/'+id+'/',
        data: $('#category_form_'+id).serialize(),
        success: function (data) {
            if (data.deleted) {
                console.log('deletado com sucesso');
                update_list_category(number_page, true);
                $('#modal_view').modal('hide');
            } else {
                console.log("error ao atualizar!");
                $('#body_modal_view').empty();
                $('#body_modal_view').html(data);

            }
        }
     });
}

function update_category(id_client){
    var number_page = parseInt($('#id_page_index').val());
    var token = $('input[name="csrfmiddlewaretoken"]');
    $.ajax({
        method: "POST",
        url: '/produtos/category_update/'+id_client+'/',
        data: $('#category_form_'+id_client).serialize(),

        success: function (data) {
            if (data.updated) {
                console.log("atualizado com sucesso!");
                update_list_category(number_page, true);
                $('#modal_view').modal('hide');
            } else {
                console.log("error ao atualizar!");
                $('#body_modal_view').empty();
                $('#body_modal_view').html(data);

            }
        }
     });
}


function update_list_category(page=1, on_delete=false){
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
        url = '/produtos/category_products/?query='+query+'&page='+number_page
        console.log("exist: ", urlParams);
    } else {
        url = '/produtos/category_products/?page='+number_page
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


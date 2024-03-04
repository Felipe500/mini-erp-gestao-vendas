function update_list_stock(page=1){
    var number_page = page;
    let url = ''
    query =  $("#id_query").val();
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    var count_itens = parseInt($('#id_page_itens').val());
    console.log("itens page: ", $('#id_page_itens').val());
    console.log('query > ', query)


    if (query!==''){
        url = '/produtos/stock_products/?query='+query+'&page='+number_page
        console.log("exist: ", urlParams);
    } else {
        url = '/produtos/stock_products/?page='+number_page
    }
    console.log("url: ", url);
    $.ajax({
        type: 'GET',
        url: url,
        data: {},
        success: function(data){
                $("#list_stock").html(data);
            }
    });
}

function modal_update_stock(id_stock, name_product){
    $.ajax({
        type: 'GET',
        url: '/produtos/update_stock/'+id_stock+'/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Alterar Estoque Produto');
            $('#body_modal_view').empty();
            $('#body_modal_view').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Editar");
            $("#button_action").removeClass().addClass('btn')
            $("#button_action").css({"background-color": "#ffc107", "color": "white"});
            $('#button_action').attr('onclick','update_stock_product('+ id_stock+')').unbind('click');
        }
    });
}

function modal_add_stock(id_stock, name_product){
    $.ajax({
        type: 'GET',
        url: '/produtos/add_stock/'+id_stock+'/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Adicionar Entrada de Produto');
            $('#body_modal_view').empty();
            $('#body_modal_view').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Salvar");
            $("#button_action").removeClass().addClass('btn')
            $("#button_action").css({"background-color": "rgba(62, 187, 36, 0.72)", "color": "white"});
            $('#button_action').attr('onclick','add_stock_product('+ id_stock+')').unbind('click');
        }
    });
}

function modal_output_stock(id_stock, name_product){
    $.ajax({
        type: 'GET',
        url: '/produtos/output_stock/'+id_stock+'/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Saída de Produto');
            $('#body_modal_view').empty();
            $('#body_modal_view').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Salvar");
            $("#button_action").removeClass().addClass('btn')
            $("#button_action").css({"background-color": "rgba(62, 187, 36, 0.72)", "color": "white"});
            $('#button_action').attr('onclick','output_stock_product('+ id_stock+')').unbind('click');
        }
    });
}

function update_stock_product(id_stock){
    var number_page = parseInt($('#id_page_index').val());
    var token = $('input[name="csrfmiddlewaretoken"]');
    $.ajax({
        method: "POST",
        url: '/produtos/update_stock/'+id_stock+'/',
        data: $('#stock_form_'+id_stock).serialize(),

        success: function (data) {
            if (data.updated) {
                console.log("atualizado com sucesso!");
                update_list_stock(number_page, true);
                $('#modal_view').modal('hide');
            } else {
                console.log("error ao atualizar!");
                $('.modal-body').empty();
                $('.modal-body').html(data);

            }
        }
     });
}

function add_stock_product(id_stock){
    var number_page = parseInt($('#id_page_index').val());
    $.ajax({
        method: "POST",
        url: '/produtos/add_stock/'+id_stock+'/',
        data: $('#stock_form_'+id_stock).serialize(),

        success: function (data) {
            if (data.updated) {
                console.log("atualizado com sucesso!");
                update_list_stock(number_page, true);
                $('#modal_view').modal('hide');
            } else {
                console.log("error ao atualizar!");
                $('.modal-body').empty();
                $('.modal-body').html(data);

            }
        }
     });
}

function output_stock_product(id_stock){
    var number_page = parseInt($('#id_page_index').val());
    $.ajax({
        method: "POST",
        url: '/produtos/output_stock/'+id_stock+'/',
        data: $('#stock_form_'+id_stock).serialize(),

        success: function (data) {
            if (data.updated) {
                console.log("atualizado com sucesso!");
                update_list_stock(number_page, true);
                $('#modal_view').modal('hide');
            } else {
                console.log("error ao atualizar!");
                $('.modal-body').empty();
                $('.modal-body').html(data);

            }
        }
     });
}

function calculator_new_stock(new_stock, type='sum'){
    console.log(new_stock.value);

    if (new_stock.value == ""){
        $('#'+new_stock.id).val('0')
     }
     if ((new_stock.value[0] == 0) &&  (new_stock.value.length > 1 )){
        $('#'+new_stock.id).val(new_stock.value.substring(1))
     }
     if (type=='sum'){
         var total = parseInt($('#current_value').html()) + parseInt(new_stock.value);
         $('#new_value').html(parseInt(new_stock.value));
         $('#total_value').html(total);

     } else {
        var total = parseInt($('#current_value').html()) - parseInt(new_stock.value);
         $('#new_value').html(parseInt(new_stock.value));
         $('#total_value').html(total);

     }


}
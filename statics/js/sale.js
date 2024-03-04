
function update_list_vendas(page=1){
    var number_page = page;
    var count_itens = parseInt($('#id_page_itens').val());
    console.log("itens page: ", $('#id_page_itens').val());
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);


    $("#id_search").hide();
    $("#loading_search").show();

    if (count_itens == 1 && number_page>1){
        number_page = number_page - 1;
        console.log("new page itens: ", number_page);
    }
    url = '/vendas/lista/?page='+number_page

    $.ajax({
        type: 'GET',
        url: url,
        data: {},
        success: function(data){
            $("#list_vendas").html(data);
        }
    });
}


function update_header_venda(id_venda){
    $.ajax({
        type: 'POST',
        url: '/vendas/update-header/'+id_venda+'/',
        data: $('#update_header_venda_'+id_venda).serialize(),
        success: function(data){
            if (data.updated) {
                    location.reload()
            } else {
                    $('#form_header_venda').empty();
                    $('#form_header_venda').html(data);
            }
        }
    });
}

function alter_status(id, status){
    $.ajax({
        method: "POST",
        url: '/vendas/alter-status/'+id+'/',
        data: {'status': status,
        'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
         },
        success: function (data) {
            if (data.updated) {
                console.log("status alterado com sucess!");
                $('#modal_view').modal('hide');
                 location.reload()
            } else {
                console.log("status nao alterado. error !");
                $('#val_error').show();
            }
        }
     });
}

function alter_status_list(id, status){
    $.ajax({
        method: "POST",
        url: '/vendas/alter-status/'+id+'/',
        data: {'status': status,
        'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
         },
        success: function (data) {
            if (data.updated) {
                console.log("status alterado com sucess!");
                $('#modal_view').modal('hide');
                 update_list_vendas(1);
            } else {
                console.log("status nao alterado. error !");
                $('#val_error').show();
            }
        }
     });
}

function update_list_itens(value){
    $.ajax({
        type: 'GET',
        url: '/vendas/items-venda/?venda_id=' + value,
        data: {},
        success: function(data){
                $("#list_products").html(data);
                console.log("dados: ", data);
            }
    });
}


function add_item_venda(id_venda){
    $.ajax({
        type: 'POST',
        url: '/vendas/item-venda/add/'+id_venda+'/',
        data: $('#form_add_item_venda_'+id_venda).serialize(),
        success: function(result){
            if (result['result']=="error"){
                $("#div_mensagem").removeClass().addClass('alert alert-warning alert-dismissible fade show')
                $("#div_mensagem").empty();
                $('#div_mensagem').append(result['mensagem'])
                $("#div_mensagem").css("display", "block").
                css("background", "#fbf276c9").css("color", "#d24500");
            } else {
                update_list_itens(id_venda);
                $("#total_venda").empty();
                $('#total_venda').append(result['total_venda']);
                $("#div_mensagem").empty();
                $("#div_mensagem").removeClass().addClass('alert alert-success alert-dismissible fade show')
                $('#div_mensagem').html(result['mensagem'])
                $("#div_mensagem").css("display", "block").
                css("background", "rgba(0, 219, 96, 0.51)").css("color", "rgb(0, 0, 0)");
                setTimeout(function() {
                    console.log(result['result']);
                    $("#div_mensagem").css("display", "none");
                }, 2000);
            }
        }
    });
}


function process_response(produtos){
    func_select = document.getElementById('id_produto_list');
    func_select.innerHTML = "";
    var list_produtos = [];
    produtos.forEach(function(produto){
        var option = document.createElement("option");
        option.text = produto.fields.descricao;
        option.value = produto.pk;
        func_select.add(option);

        list_produtos.push({
            value: produto.pk,
            label: produto.fields.descricao,
        });
    });

    console.log(list_produtos)
    select_produtos_list.clearChoices();
    select_produtos_list.setChoices(
          list_produtos,
          'value',
          'label',
          false,
    );
}


function products_by_category(categoria_id){
    console.log(categoria_id);
    $.ajax({
        type: 'GET',
        url: '/produtos/products_by_category/'+categoria_id,
        data: {},
        success: function(result){
            process_response(result);
            console.log(result)
            $("#mensagem").text('Funcionarios carregados');
        }
    });
}

function modal_view_edit_item(id_item, desc_item){
    $.ajax({
        type: 'GET',
        url: '/vendas/item-venda/update/'+id_item+'/',
        data: {},
        success: function(data){
            $('#title_modal_edit_item').empty();
            $('#title_modal_edit_item').append('Item: '+desc_item);
            $('#body_modal_edit_item').empty();
            $('#body_modal_edit_item').html(data);
            $('#button_action_edit_item').removeAttr("onclick");
            $('#button_action_edit_item').empty();
            $('#button_action_edit_item').append("Editar Item da venda");
            $('#button_action_edit_item').removeAttr('style');
            $("#button_action_edit_item").removeClass().addClass('btn btn-warning text-white')
            $('#button_action_edit_item').attr('onclick','update_edit_item('+ id_item+ ')').unbind('click');
            console.log("deu certo: ");
        }
    });
}

function modal_view_delete_item(id_item, name_product){
    console.log(id_item);

    $.ajax({
        type: 'GET',
        url: '/vendas/item-venda/delete/'+id_item+'/',
        data: {},
        success: function(data){
                $('#title_modal_edit_item').empty();
                $('#title_modal_edit_item').append('Confirmação!');
                $('#body_modal_edit_item').empty();
                $('#body_modal_edit_item').append("Deletar");
                $('#body_modal_edit_item').empty();
                $('#body_modal_edit_item').html(data);
                $("#button_action_edit_item").removeClass().addClass('btn btn-danger')
                $('#button_action_edit_item').removeAttr("onclick");
                $('#button_action_edit_item').removeAttr('style');
                $('#button_action_edit_item').attr('onclick','delete_item('+ id_item+')').unbind('click');
        }
    });

}

function delete_item(id_item){
    $.ajax({
        method: "POST",
        url: '/vendas/item-venda/delete/'+id_item+'/',
        data: $('#item_delete_form_'+id_item).serialize(),
        success: function (data) {
            if (data.deleted) {
                console.log('deletado com sucesso');
                $('#total_venda').empty();
                $('#total_venda').html(data.total_venda);
                update_list_itens(data.id_venda);
                $('#modal_edit_item').modal('hide');
            } else {
                console.log("error ao atualizar!");
                $('#body_modal_view').empty();
                $('#body_modal_view').html(data);

            }
        }
     });
}

function update_edit_item(id_item){
    $.ajax({
        method: "POST",
        url: '/vendas/item-venda/update/'+id_item+'/',
        data: $('#edit_item_form_'+id_item).serialize(),
        success: function (data) {
            if (data.updated) {
                console.log("item atualizado com sucesso!");
                update_list_itens(data.id_venda);
                $('#input_qted_itens_'+id_item).val(data.qted)
                $('#total_venda').html(data.total_venda);
                $('#modal_edit_item').modal('hide');
            } else {
                console.log("error ao atualizar!");
                $('#body_modal_edit_item').empty();
                $('#body_modal_edit_item').html(data);
            }
        }
     });
}


function modal_payment(id){
    $.ajax({
        type: 'GET',
        url: '/vendas/form_pagamento/'+id+'/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Realizar Pagamento');
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


function post_payment(id){
    $.ajax({
        method: "POST",
        url: '/vendas/form_pagamento/'+id+'/',
        data: $('#payment_form_'+id).serialize(),
        success: function (data) {
            if (data.payment=='success') {
                console.log("pago com sucesso!");
                $('#modal_view').modal('hide');
                location.re
            } else {
                console.log("error ao pagar!");
                $('#val_error').show();
            }
        }
     });
}



function decrement_qted(id){
console.log($('#input_qted_itens_'+id).val());
 if ($('#input_qted_itens_'+id).val() >= 1){
    $.ajax({
        method: "POST",
        url: '/vendas/item-venda/decrement/'+id+'/',
        data: $('#item_qted_form_'+id).serialize(),
        success: function (data) {
            if (data.updated) {
                console.log("editado com sucesso!");
                $('#input_qted_itens_'+id).val(data.qted)
                $('#total_venda').html(data.total_venda);
            } else {
                console.log("error ao editar!");

            }
        }
     });
  }
}


function addition_qted(id){
console.log($('#input_qted_itens_'+id).val());
    if ($('#input_qted_itens_'+id).val() <= 999){
        $.ajax({
        method: "POST",
        url: '/vendas/item-venda/addition/'+id+'/',
        data: $('#item_qted_form_'+id).serialize(),
        success: function (data) {
            if (data.updated) {
                console.log('estoque b- ',data.estoque_baixo);
                $('#input_qted_itens_'+id).val(data.qted)
                $('#total_venda').empty();
                $('#total_venda').html(data.total_venda);
            } else {
                console.log(data['error']);
                $("#div_mensagem").empty();
                $("#div_mensagem").removeClass().addClass('alert alert-warning alert-dismissible fade show')
                $('#div_mensagem').html(data['error'])
                $("#div_mensagem").css("display", "block").
                css("background", "#fbf276c9").css("color", "#d24500");
                setTimeout(function() {
                    $("#div_mensagem").css("display", "none");
                }, 2000);
            }
        }
     });
    }
}


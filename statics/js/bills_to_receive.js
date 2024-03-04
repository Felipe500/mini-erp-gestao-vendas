function update_list_to_receive(page=1, on_delete=false){
    var number_page = page;
    var count_itens = parseInt($('#id_page_itens').val());
    let url = ''
    query =  $("#id_descricao_filter").val();
    start_date = $('#id_start_date_filter').val();
    end_date = $('#id_end_date_filter').val();
    status = $('#id_status_filter').val();
    categoria_filter = $('#id_categoria_filter').val();

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
    console.log("start_date: "+ start_date);
    console.log("start_date: "+ start_date);
    console.log("status: "+ status);
    console.log("categoria_filter: "+ categoria_filter);

    filters = ''
    if (start_date!=''){
        filters += '&start_date='+start_date
    }
    if (end_date!=''){
        filters += '&end_date='+end_date
    }
    if (status!='0'){
        filters += '&status='+status
    }
    if (categoria_filter!='0'){
        filters += '&categoria='+categoria_filter
    }

    url = '/controle_contas/a-receber/list/?page='+number_page+'&query='+query+filters

    $.ajax({
        type: 'GET',
        url: url,
        data: {},
        success: function(data){
                $("#list_contas").html(data);
            }
    });
}


function view_create_bills_receive(){
    $.ajax({
        type: 'GET',
        url: '/controle_contas/a-receber/view_nova_conta/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Adicionar Conta a Receber');
            $('.modal-body').empty();
            $('.modal-body').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Adicionar");
            $("#button_action").removeClass().addClass('btn btn-primary text-white')
            $('#button_action').attr('onclick','create_bills_receive()').unbind('click');
        }
    });
}


function create_bills_receive(){
    var number_page = parseInt($('#id_page_index').val());
    console.log('>',$('#bills_form_0').serialize())
    $.ajax({
        method: "POST",
        url: '/controle_contas/a-receber/criar/',
        data: $('#bills_form_0').serialize(),

        success: function (data) {
            if (data.created) {
                console.log("atualizado com sucesso!");
                update_list_to_receive(number_page);
                $('#modal_view').modal('hide');
            } else {
                console.log("error ao cadastrar!");
                $('.modal-body').empty();
                $('.modal-body').html(data);
            }
        }
     });
}


function view_delete_bills_receive(id, name, count_itens){
    let link_delete = id;
    console.log(link_delete);
    $.ajax({
        type: 'GET',
        url: '/controle_contas/a-receber/view_deletar/'+id+'/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Confirmação!');
            $('.modal-body').empty();
            $('.modal-body').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Deletar");

            $("#button_action").removeClass().addClass('btn btn-danger')
            $('#button_action').attr('onclick','delete_bills_receive('+ id+')').unbind('click');
        }
    });
}


function delete_bills_receive(id){
    var number_page = parseInt($('#id_page_index').val());
    var token = $('input[name="csrfmiddlewaretoken"]');
    $.ajax({
        method: "POST",
        url: '/controle_contas/a-receber/deletar/'+id+'/',
        data: $('#bills_form_'+id).serialize(),

        success: function (data) {
            if (data.deleted) {
                update_list_to_receive(number_page, true);
                 $('#modal_view').modal('hide');
            }
        }
     });
}


function view_update_bills_receive(id){
    $.ajax({
        type: 'GET',
        url: '/controle_contas/a-receber/view_atualizar/'+id+'/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Conta a pagar');
            $('.modal-body').empty();
            $('.modal-body').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Editar");
            $("#button_action").removeClass().addClass('btn btn-warning text-white')
            $('#button_action').attr('onclick','update_bills_receive('+ id+')').unbind('click');
        }
    });
}


function update_bills_receive(id){
    var number_page = parseInt($('#id_page_index').val());
    var token = $('input[name="csrfmiddlewaretoken"]');
    $.ajax({
        method: "POST",
        url: '/controle_contas/a-receber/atualizar/'+id+'/',
        data: $('#bills_form_'+id).serialize(),

        success: function (data) {
            if (data.updated) {
                console.log("atualizado com sucesso!");
                update_list_to_receive(number_page);
                $('#modal_view').modal('hide');
            } else {
                console.log("error ao atualizar!");
                $('#body_modal_view').empty();
                $('#body_modal_view').html(data);
            }
            }
        });
}

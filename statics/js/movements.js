function update_list_movements(page=1, on_delete=false){
    var number_page = page;
    var count_itens = parseInt($('#id_page_itens').val());
    let url = ''
    type =  $("#id_tipo_entrada_filter").val();
    start_date = $('#id_start_date_filter').val();
    end_date = $('#id_end_date_filter').val();

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
    console.log("type: "+ type);

    filters = ''
    if (start_date!=''){
        filters += '&start_date='+start_date
    }
    if (end_date!=''){
        filters += '&end_date='+end_date
    }
    if (type!=''){
        filters += '&type='+type
    }

    url = '/controle_contas/lista_movimentacoes/?page='+number_page+filters

    $.ajax({
        type: 'GET',
        url: url,
        data: {},
        success: function(data){
                $("#list_mov").html(data);
            }
    });
}
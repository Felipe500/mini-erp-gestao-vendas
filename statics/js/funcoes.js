
function maq_card_fees(id){
    $.ajax({
        type: 'GET',
        url: '/vendas/card_fees/'+id+'/',
        data: {},
        success: function(data){
            $('#taxas_maq').empty();
            $('#taxas_maq').html(data);
            console.log("deu certo: ");
        }
    });
}

function payment_methods2(set_this){
        var responseID = $(set_this).val();

        console.log('select meios pg');
        if(responseID =="1"){
            $('#forms-pg').removeClass("hidden");
            $('#forms-pg').addClass("show");

            $('#pg_especie').removeClass("hidden");
            $('#pg_especie').addClass("show");
            $('#pg_especie :input').val(0);

            $('#pg_pix').removeClass("show");
            $('#pg_pix').addClass("hidden");
            $('#pg_pix :input').val(0);

            $('#pg_card').removeClass("show");
            $('#pg_card').addClass("hidden");
            $('#pg_card :input').val(0);
        }
        if(responseID =="2"){
            $('#forms-pg').removeClass("hidden");
            $('#forms-pg').addClass("show");

            $('#pg_especie').removeClass("show");
            $('#pg_especie').addClass("hidden");
            $('#pg_especie :input').val(0);

            $('#pg_pix').removeClass("hidden");
            $('#pg_pix').addClass("show");
            $('#pg_pix :input').val(0);

            $('#pg_card').removeClass("show");
            $('#pg_card').addClass("hidden");
            $('#pg_card :input').val(0);
        }
        if(responseID =="3"){
            $('#forms-pg').removeClass("hidden");
            $('#forms-pg').addClass("show");
            $('#pg_card_input').removeClass("hidden");
            $('#pg_card_input').addClass("show");

            $('#pg_especie').removeClass("show");
            $('#pg_especie').addClass("hidden");
            $('#pg_pix').removeClass("show");
            $('#pg_pix').addClass("hidden");
            $('#pg_card').removeClass("hidden");
            $('#pg_card').addClass("show");
            $('#id_categoria_list').prop('selectedIndex',0);
            maq_card_fees(1)

        }
        if(responseID =="4"){
            $('#forms-pg').removeClass("hidden");
            $('#forms-pg').addClass("show");

            $('#pg_especie').removeClass("hidden");
            $('#pg_especie').addClass("show");
            $('#pg_pix').removeClass("hidden");
            $('#pg_pix').addClass("show");
            $('#pg_card').removeClass("show");
            $('#pg_card').addClass("hidden");
            $('#pg_card :input').val(0);

            console.log($('#pg_card :input').val());
        }

        if(responseID =="5"){
            $('#forms-pg').removeClass("hidden");
            $('#forms-pg').addClass("show");
            $('#pg_card_input').removeClass("hidden");
            $('#pg_card_input').addClass("show");

            $('#pg_especie').removeClass("hidden");
            $('#pg_especie').addClass("show");
            $('#pg_pix').removeClass("show");
            $('#pg_pix').addClass("hidden");
            $('#pg_pix :input').val(0);
            $('#pg_card').removeClass("hidden");
            $('#pg_card').addClass("show");
            $('#id_categoria_list').prop('selectedIndex',0);
            maq_card_fees(1)

        }
        if(responseID =="6"){
            $('#forms-pg').removeClass("hidden");
            $('#forms-pg').addClass("show");

            $('#pg_card_input').removeClass("hidden");
            $('#pg_card_input').addClass("show");
            $('#id_categoria_list').prop('selectedIndex',0);

            $('#pg_especie').removeClass("show");
            $('#pg_especie').addClass("hidden");
            $('#pg_especie :input').val(0);
            $('#pg_pix').removeClass("hidden");
            $('#pg_pix').addClass("show");
            $('#pg_card').removeClass("hidden");
            $('#pg_card').addClass("show");
            $('#id_categoria_list').prop('selectedIndex',0);
            maq_card_fees(1)
        }
        if(responseID =="7"){
            $('#forms-pg').removeClass("hidden");
            $('#forms-pg').addClass("show");

            $('#pg_card_input').removeClass("hidden");
            $('#pg_card_input').addClass("show");
            $('#pg_card_input :input').val(0);
            $('#pg_especie').removeClass("hidden");
            $('#pg_especie').addClass("show");
            $('#pg_especie :input').val(0);
            $('#pg_pix').removeClass("hidden");
            $('#pg_pix').addClass("show");
            $('#pg_pix :input').val(0);
            $('#pg_card').removeClass("hidden");
            $('#pg_card').addClass("show");
        }

        if(responseID =="form-card"){
            $('#form-card').removeClass("hidden");
            $('#form-card').addClass("show");
        }else{
            $('#form-card').removeClass("show");
            $('#form-card').addClass("hidden");
        }

        console.log(responseID);
}


    $(document).ready(function(){
        $('#myselection').on('change', function(){
            var demovalue = $(this).val();
            $("div.myDiv").hide();
            $("#show"+demovalue).show();
        });
    });

function confirmar_pag(total_val, total_centavos){
    var total_pagamento = parseFloat($('#card_input').val()) +
     parseFloat($('#pix_input').val()) +  parseFloat($('#especie_input').val());
     console.log(total_pagamento);

     if (total_pagamento != (parseFloat(total_val+(total_centavos/100), 2))){
        console.log("valor diferente");
     } else{
    console.log("valor igual");
     }
     console.log(parseFloat(total_val+(total_centavos/100), 2));
}


function payment_methods(obj){
        var responseID = $(obj).val();

        console.log(responseID);
        if(responseID =="1"){
            $('#forms-pg').removeClass("hidden");
            $('#forms-pg').addClass("show");

            $('#pg_especie').removeClass("hidden");
            $('#pg_especie').addClass("show");
            $('#pg_especie :input').val(0);

            $('#pg_pix').removeClass("show");
            $('#pg_pix').addClass("hidden");
            $('#pg_pix :input').val(0);

            $('#pg_card').removeClass("show");
            $('#pg_card').addClass("hidden");
            $('#pg_card :input').val(0);
        }
        if(responseID =="2"){
            $('#forms-pg').removeClass("hidden");
            $('#forms-pg').addClass("show");

            $('#pg_especie').removeClass("show");
            $('#pg_especie').addClass("hidden");
            $('#pg_especie :input').val(0);

            $('#pg_pix').removeClass("hidden");
            $('#pg_pix').addClass("show");
            $('#pg_pix :input').val(0);

            $('#pg_card').removeClass("show");
            $('#pg_card').addClass("hidden");
            $('#pg_card :input').val(0);
        }
        if(responseID =="3"){
            $('#forms-pg').removeClass("hidden");
            $('#forms-pg').addClass("show");
            $('#pg_card_input').removeClass("hidden");
            $('#pg_card_input').addClass("show");

            $('#pg_especie').removeClass("show");
            $('#pg_especie').addClass("hidden");
            $('#pg_pix').removeClass("show");
            $('#pg_pix').addClass("hidden");
            $('#pg_card').removeClass("hidden");
            $('#pg_card').addClass("show");
            var id_maq_card = $("#id_maq_card option:first").val();
            console.log('id card ',id_maq_card);
            maq_card_fees(id_maq_card);

        }
        if(responseID =="4"){
            $('#forms-pg').removeClass("hidden");
            $('#forms-pg').addClass("show");

            $('#pg_especie').removeClass("hidden");
            $('#pg_especie').addClass("show");
            $('#pg_pix').removeClass("hidden");
            $('#pg_pix').addClass("show");
            $('#pg_card').removeClass("show");
            $('#pg_card').addClass("hidden");
            $('#pg_card :input').val(0);

            console.log($('#pg_card :input').val());
        }

        if(responseID =="5"){
            $('#forms-pg').removeClass("hidden");
            $('#forms-pg').addClass("show");
            $('#pg_card_input').removeClass("hidden");
            $('#pg_card_input').addClass("show");

            $('#pg_especie').removeClass("hidden");
            $('#pg_especie').addClass("show");
            $('#pg_pix').removeClass("show");
            $('#pg_pix').addClass("hidden");
            $('#pg_pix :input').val(0);
            $('#pg_card').removeClass("hidden");
            $('#pg_card').addClass("show");
            $('#id_categoria_list').prop('selectedIndex',0);
            var id_maq_card = $("#id_maq_card option:first").val();
            console.log('id card ',id_maq_card);
            maq_card_fees(id_maq_card);

        }
        if(responseID =="6"){
            $('#forms-pg').removeClass("hidden");
            $('#forms-pg').addClass("show");

            $('#pg_card_input').removeClass("hidden");
            $('#pg_card_input').addClass("show");
            $('#id_categoria_list').prop('selectedIndex',0);

            $('#pg_especie').removeClass("show");
            $('#pg_especie').addClass("hidden");
            $('#pg_especie :input').val(0);
            $('#pg_pix').removeClass("hidden");
            $('#pg_pix').addClass("show");
            $('#pg_card').removeClass("hidden");
            $('#pg_card').addClass("show");
            $('#id_categoria_list').prop('selectedIndex',0);
            var id_maq_card = $("#id_maq_card option:first").val();
            console.log('id card ',id_maq_card);
            maq_card_fees(id_maq_card);
        }
        if(responseID =="7"){
            $('#forms-pg').removeClass("hidden");
            $('#forms-pg').addClass("show");

            $('#pg_card_input').removeClass("hidden");
            $('#pg_card_input').addClass("show");
            $('#pg_card_input :input').val(0);
            $('#pg_especie').removeClass("hidden");
            $('#pg_especie').addClass("show");
            $('#pg_especie :input').val(0);
            $('#pg_pix').removeClass("hidden");
            $('#pg_pix').addClass("show");
            $('#pg_pix :input').val(0);
            $('#pg_card').removeClass("hidden");
            $('#pg_card').addClass("show");
        }

        if(responseID =="form-card"){
            $('#form-card').removeClass("hidden");
            $('#form-card').addClass("show");
        }else{
            $('#form-card').removeClass("show");
            $('#form-card').addClass("hidden");
        }


    }
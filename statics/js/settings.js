$(document).ready(function(){
            form_change_user();
         });

function form_change_user(){
    $.ajax({
        type: 'GET',
        url: '/settings/change-perfil_user/',
        data: {},
        success: function(data){
            $('#page_config').empty();
            $('#page_config').html(data);
        }
    });
}

function form_change_active_user(id){
    is_active = $('#div_is_active_'+id+ ' input').val()
    data = $('#id_form_user_active_'+id).serialize() + "&is_active=" + is_active;
    $.ajax({
        type: 'POST',
        url: '/settings/control_access/users/active/'+id,
        data: data,
        success: function(data){
            form_control_access();
        }
    });
}

function form_user(id=0){
    if (id == 0){
            $.ajax({
                type: 'GET',
                url: '/settings/control_access/users/create_user',
                data: {},
                success: function(data){
                    $('#page_config').empty();
                    $('#page_config').html(data);
                    console.log($('#id_email'));
            }
        });

    } else {
         $.ajax({
                type: 'GET',
                url: '/settings/control_access/users/'+id,
                data: {},
                success: function(data){
                    $('#page_config').empty();
                    $('#page_config').html(data);
                    console.log($('#id_email'));
            }
        });

    }

}

function create_or_update_user(id=0){
    console.log($('#id_form_user_'+id).serialize())
     console.log(id);
    if (id == 0){
        $.ajax({
            method: "POST",
            url: '/settings/control_access/users/create_user',
            data: $('#id_form_user_'+id).serialize(),
            success: function (data) {
                if (data.created) {
                    console.log("created com sucesso!");
                    form_control_access();
                } else {
                    $('#page_config').empty();
                    $('#page_config').html(data);
                }
            }
         });
    } else {

        $.ajax({
            method: "POST",
            url: '/settings/control_access/users/'+id,
            data: $('#id_form_user_'+id).serialize(),
            success: function (data) {
                if (data.updated) {
                    console.log("atualizado com sucesso!");
                    form_control_access();
                } else {
                    $('#page_config').empty();
                    $('#page_config').html(data);
                }
            }
         });
    }
}

function form_create_group(){
    $.ajax({
        type: 'GET',
        url: '/settings/control_access/groups/create_group',
        data: {},
        success: function(data){
            $('#page_config').empty();
            $('#page_config').html(data);
        }
    });
}

function form_group(id=0){
    if (id == 0){
        $.ajax({
            type: 'GET',
            url: '/settings/control_access/groups/create_group',
            data: {},
            success: function(data){
                $('#page_config').empty();
                $('#page_config').html(data);
            }
        });
    } else {
         $.ajax({
            type: 'GET',
            url: '/settings/control_access/groups/'+id,
            data: {},
            success: function(data){
                $('#page_config').empty();
                $('#page_config').html(data);

            }
        });
    }
}


function create_or_update_group(id=0){
    console.log($('#id_form_create_user').serialize());
     if (id == 0){
            $.ajax({
            method: "POST",
            url: '/settings/control_access/groups/create_group',
            data: $('#id_form_group_'+id).serialize(),
            success: function (data) {
                if (data.created) {
                    console.log("created com sucesso!");
                    form_control_access_groups();
                } else {
                    $('#page_config').empty();
                    $('#page_config').html(data);
                }
            }
         });
     } else {
         $.ajax({
            method: "POST",
            url: '/settings/control_access/groups/'+id,
            data: $('#id_form_group_'+id).serialize(),

            success: function (data) {
                if (data.updated) {
                    console.log("updated com sucesso!");
                    form_control_access_groups();
                } else {
                    $('#page_config').empty();
                    $('#page_config').html(data);

                }
            }
         });
     }
}


function form_control_access(){
    $.ajax({
        type: 'GET',
        url: '/settings/control_access/users',
        data: {},
        success: function(data){
            $('#page_config').empty();
            $('#page_config').html(data);
            console.log( $('#id_email'));
        }
    });
}

function form_control_access_groups(){
    $.ajax({
        type: 'GET',
        url: '/settings/control_access/groups',
        data: {},
        success: function(data){
            $('#page_config').empty();
            $('#page_config').html(data);
        }
    });
}


function form_change_password(){
    $.ajax({
        type: 'GET',
        url: '/settings/alter-password/',
        data: {},
        success: function(data){

            $('#page_config').empty();
            $('#page_config').html(data);

        }
    });
}

function change_password(){
    var number_page = parseInt($('#id_page_index').val());
    $.ajax({
        method: "POST",
        url: '/settings/alter-password/',
        data: $('#id_form_change_password').serialize(),

        success: function (data) {
            console.log("retorno");
            console.log(data);
            if (data.password_changed) {
                console.log("atualizado com sucesso!");
                form_change_password();
                $('#modal_view').modal('hide');
                $(".toast-body").empty();
                $(".toast-body").html("Sua senha foi alterado com sucesso.");
                $("#toast_message").removeClass().addClass('toast align-items-center text-bg-success border-0');
                $("#toast_message").toast('show');
            } else {
                $('#page_config').empty();
                $('#page_config').html(data);
                $(".toast-body").empty();
                $(".toast-body").html("Erro ao alterar sua senha!.");
                $("#toast_message").removeClass().addClass('toast align-items-center text-bg-danger border-0');
                $("#toast_message").toast('show');
                console.log("error ao alterar senha!");

            }
        }
     });
}

function change_user(){
    var number_page = parseInt($('#id_page_index').val());
    var image = $('#id_photo')[0].files[0];
    var data = new FormData();

    data.append('photo', image)
    data.append('name', $('#id_name').val())
    data.append('email', $('#id_email').val())
    data.append('csrfmiddlewaretoken', $('#csrfmiddlewaretoken').val())
    var data2 = new FormData($('#id_form_change_user').get(0));
    $.ajax({
        method: "POST",
        url: '/settings/change-perfil_user/',
        data: data2,
         processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (data) {
            console.log("retorno");
            console.log(data);
            if (data.password_changed) {
                console.log(" 1 atualizado com sucesso!");
                $(".toast-body").empty();
                $(".toast-body").html("O usuário '"+data.user+"' foi alterado com sucesso. ");
                $("#toast_message").removeClass().addClass('toast align-items-center text-bg-success border-0')
                $("#toast_message").toast('show');
            } else {
                $('#page_config').empty();
                $('#page_config').html(data);
                console.log("error ao alterar senha!");

            }
        }
     });
}

function list_machine_card(){
    $.ajax({
        type: 'GET',
        url: '/settings/payments/machine-card/',
        data: {},
        success: function(data){
             console.log("list_maq_card!");
            $('#page_config').empty();
            $('#page_config').html(data);
        }
    });
}

function form_machine_card(){
    $.ajax({
        type: 'GET',
        url: '/settings/payments/machine-card/create/',
        data: {},
        success: function(data){
             console.log("create_maq_card!");
            $('#page_config').empty();
            $('#page_config').html(data);

        }
    });
}

function form_update_machine_card(id){
    $.ajax({
        type: 'GET',
        url: '/settings/payments/machine-card/update/'+id+'/',
        data: {},
        success: function(data){
             console.log("update_maq_card!");
            $('#page_config').empty();
            $('#page_config').html(data);

        }
    });
}

function create_machine_card(){
    console.log($('#id_form_machine_card').serialize());
    $.ajax({
        method: "POST",
        url: '/settings/payments/machine-card/create/',
        data: $('#id_form_machine_card').serializeArray(),

        success: function (data) {
            console.log("retorno");
            if (data.created) {
                console.log("criado com sucesso!");
                list_machine_card();
            } else {
                $('#page_config').empty();
                $('#page_config').html(data);
            }
        }
     });
}

function update_machine_card(id){
    $.ajax({
        method: "POST",
        url:'/settings/payments/machine-card/update/'+id+'/',
        data: $('#id_form_machine_card').serializeArray(),

        success: function (data) {
            console.log("retorno");
            console.log(data);
            if (data.updated) {
                console.log("atualizado com sucesso!");
                list_machine_card();
            } else {
                $('#page_config').empty();
                $('#page_config').html(data);
            }
        }
     });
}

function modal_delete_machine_card(id, name){
    let link_delete = id;
    console.log(id);

    $.ajax({
        type: 'GET',
        url: '/settings/payments/machine-card/delete/'+id+'/',
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
                $('#button_action').attr('onclick','delete_machine_card('+ id+')').unbind('click');
        }
    });

}

function delete_machine_card(id){
    $.ajax({
        method: "POST",
        url: '/settings/payments/machine-card/delete/'+id+'/',
        data: $('#id_form_machine_card').serialize(),
        success: function (data) {
            if (data.deleted) {
                console.log('deletado com sucesso');
                list_machine_card();
                $('#modal_view').modal('hide');
            }
        }
     });
}

function modal_delete_group(id, name){
    let link_delete = id;

    $.ajax({
        type: 'GET',
        url: '/settings/control_access/groups/delete/'+id,
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
                $('#button_action').attr('onclick','delete_group('+ id+')').unbind('click');
        }
    });
}

function delete_group(id){
    $.ajax({
        method: "POST",
        url: '/settings/control_access/groups/delete/'+id,
        data: $('#form_group_'+id).serialize(),
        success: function (data) {
            if (data.deleted) {
                console.log('deletado com sucesso');
                form_control_access_groups();
                $('#modal_view').modal('hide');
            }
        }
     });
}

function modal_delete_user(id){
    $.ajax({
        type: 'GET',
        url: '/settings/control_access/users/delete/'+id,
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
                $('#button_action').attr('onclick','delete_user('+ id+')').unbind('click');
        }
    });
}

function delete_user(id){
    $.ajax({
        method: "POST",
        url: '/settings/control_access/users/delete/'+id,
        data: $('#id_form_user_'+id).serialize(),
        success: function (data) {
            if (data.deleted) {
                console.log('user deletado com sucesso');
                form_control_access();
                $('#modal_view').modal('hide');
            }
        }
     });
}

function toast_hide(){
     $(".toast").toast('hide');
}

function toast_show(){
     $(".toast").toast('show');
}

function previewFile(input){
    var file = $("input[type=file]").get(0).files[0];

    if(file){
        var reader = new FileReader();
        reader.onload = function(){
             $("#img_card").attr("src", reader.result);
        }
        $('#img_card').show();
        reader.readAsDataURL(file);
    }
}
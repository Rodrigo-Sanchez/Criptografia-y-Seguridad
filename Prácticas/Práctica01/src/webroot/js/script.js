$(document).ready(function () {

    // Mostramos el menú cuando cliqueamos en los tres puntos.    
    $('#action_menu_btn').click(function () {
        $('.action_menu').toggle();
    });

    // Variable para crear un WebSocket.
    var websocket = new WebSocket("ws://18.220.235.202:7500/");

    // Enviamos el valor del textarea si cliqueamos el botón de enviar.
    $('#button').click(function () {
        // Obtenemos el campo del nombre de usuario del modal.
        username = $('#username').val();
        // Obtenemos el campo del nombre de usuario del modal.
        message = $('#message').val();
        // Solamente funciona si el campo no es vacío.
        if (message) {
            // Agregamos al árbol DOM el contenido del mensaje.
            $(".msg_card_body").append('<div class="d-flex justify-content-end mb-4">' +
                                            '<div class="msg_cotainer_send">' +
                                                message +
                                                '<span class="msg_time_send">' +
                                                    JSClock() +
                                                '</span>' +
                                            '</div>' +
                                            '<div class="img_cont_msg">' +
                                                '<img src="webroot/img/man04.svg" class="rounded-circle user_img_msg">' +
                                            '</div>' +
                                        '</div>');
            // Creamos el objeto con el tipo de petición al servidor.
            let obj = {"tipo" : "msj_chat"};
            // Agregamos el nombre de usuario destinatario al objeto.
            obj["destino"] = "Jorge";
            // Agregamos el mensaje al objeto.
            obj["msj"] = message;
            // Convierte un objeto a una cadena JSON.
            let json = JSON.stringify(obj);
            // Se envía la cadena al websocket.
            websocket.send(json);
        }
    });

    // Acción al cliquear "Registar usuario".
    $('#register').click(function () {
        // Obtenemos el campo del nombre de usuario del modal.
        username = $('#username').val();
        // Solamente funciona si el campo no es vacío.
        if(username) {
            // Creamos el objeto con el tipo de petición al servidor.
            let obj = {"tipo" : "registro"};
            // Agregamos el nombre de usuario al objeto.
            obj["nombre"] = username;
            // Convierte un objeto a una cadena JSON.
            let json = JSON.stringify(obj);
            // Se envía la cadena al websocket.
            websocket.send(json);
        }
    });

    // Acción al cliquear "Mostrar usuarios conectados".
    $('#users').click(function () {
        // Mandamos un JSON con el tipo de petición para obtener los usuarios.
        websocket.send(JSON.stringify({
            "tipo": "usuarios"
        }));
    });

    // Si recibimos una respuesta del servidor mostramos el contenido.
    websocket.onmessage = function (evt) {
        // Convierte en objeto la cadena JSON recibida.
        var obj = JSON.parse(evt.data);
        console.log(obj);
        switch(obj.tipo) {
            case "msj_nuevo":
                $(".msg_card_body").append('<div class="d-flex justify-content-start mb-4">' +
                                                '<div class="img_cont_msg">' +
                                                    '<img src="webroot/img/man01.svg" class="rounded-circle user_img_msg">' +
                                                '</div>' +
                                                '<div class="msg_cotainer">' +
                                                    obj.msj +
                                                    '<span class="msg_time">' +
                                                        obj.hora +
                                                    '</span>' +
                                                '</div>' +
                                            '</div>');
                break;
            default:
                break;
        }
    }
});

// Función para darle formato a la fecha.
function JSClock() {
    let now = new Date();
    let year = now.getFullYear();
    let day = now.getDate();
    let month = now.getMonth();
    let hour = now.getHours();
    let minutes = now.getMinutes();
    let seconds = now.getSeconds();
    switch(month) {
        case 0:
            month = "Ene";
            break;
        case 1:
            month = "Feb";
            break;
        case 2:
            month = "Mar";
            break;
        case 3:
            month = "Abr";
            break;
        case 4:
            month = "May";
            break;
        case 5:
            month = "Jun";
            break;
        case 6:
            month = "Jul";
            break;
        case 7:
            month = "Ago";
            break;
        case 8:
            month = "Sep";
            break;
        case 9:
            month = "Oct";
            break;
        case 10:
            month = "Nov";
            break;
        case 11:
            month = "Dic";
            break;
    }
    let time = day + " " + month + " " + year + " ";
    time += ((hour > 12) ? ((hour - 12 == 0) ? hour = 12 : (hour - 12)) : ((hour == 0) ? hour = 12 : hour));
    time += ((minutes < 10) ? ":0" : ":") + minutes;
    time += ((seconds < 10) ? ":0" : ":") + seconds;
    return time;
}

// Función para mantener el scroll del chat abajo.
function updateScroll() {
    var element = document.getElementById("msg_card_body");
    element.scrollTop = element.scrollHeight;
}

setInterval(updateScroll, 100);

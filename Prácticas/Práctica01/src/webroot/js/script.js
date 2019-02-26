$(document).ready(function () {

    // Mostramos el menú cuando cliqueamos en los tres puntos.    
    $('#action_menu_btn').click(function () {
        $('.action_menu').toggle();
    });

    // Variable para obtener el textarea del chat.
    message = document.getElementById('message');
    // Variable para crear un WebSocket.
    websocket = new WebSocket("ws://18.220.235.202:7500/");

    // Enviamos el valor del textarea si cliqueamos el botón de enviar.
    $('#button').click(function () {
        if (message.value) {
            alert($("#message").val());

            // websocket.send(JSON.stringify({
            //     "tipo": "msj_chat",
            //     "destino": "Jorge",
            //     "msj": "Hola, criptoamigo."
            // }));

            // websocket.send(message.value);
        }
    });

    $('#register').click(function () {
        if (message.value) {
            websocket.send(JSON.stringify({
                "tipo": "registro",
                "nombre": "Rodd"
            }));
        }
    });

    $('#users').click(function () {
        if (message.value) {
            websocket.send(JSON.stringify({
                "tipo": "usuarios",
            }));
        }
    });

    // Si recibimos una respuesta del servidor mostramos el contenido.
    websocket.onmessage = function (evt) {
        alert(evt.data);
    }
});
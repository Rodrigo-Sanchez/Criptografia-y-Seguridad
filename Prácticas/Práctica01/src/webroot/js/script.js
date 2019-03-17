$(document).ready(function () {

    // Asignamos una llave por defecto.
    window.key = "hola";

    // Mostramos el menú cuando cliqueamos en los tres puntos.    
    $('#action_menu_btn').click(function () {
        $('.action_menu').toggle();
    });

    // Variable para crear un WebSocket.
    var websocket = new WebSocket("ws://18.220.235.202:7500/");

    // Enviamos el valor del textarea si cliqueamos el botón de enviar.
    $('#button').click(function () {
        // Obtenemos el campo del nombre de usuario del modal.
        message = $('#message').val();
        // Solamente funciona si el campo no es vacío.
        if (message) {
            // Agregamos al chat el contenido del mensaje.
            $(".msg_card_body").append(
                '<div class="d-flex justify-content-end mb-4">' +
                    '<div class="msg_cotainer_send">' +
                        message +
                        '<span class="msg_time_send">' +
                            JSClock() +
                        '</span>' +
                    '</div>' +
                    '<div class="img_cont_msg">' +
                        '<img src="webroot/img/man02.svg" class="rounded-circle user_img_msg">' +
                    '</div>' +
                '</div>');
            // Creamos el objeto con el tipo de petición al servidor.
            let obj = {"tipo" : "msj_chat"};
            // Agregamos el nombre de usuario destinatario al objeto.
            obj["destino"] = $(this).attr('data-user');
            // Agregamos el mensaje al objeto.
            obj["msj"] = atob(message);

            // Convierte un objeto a una cadena JSON.
            let json = JSON.stringify(obj);
            // Se envía la cadena al websocket.
            websocket.send(json);
            // Limpiamos el texto recién enviado del textArea.
            $("#message").val('');
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
            // Ocultamos el modal.
            $('#usersModal').modal('hide');
        }
    });

    // Acción al cliquear "Registar usuario".
    $('#sendKey').click(function () {
        // Obtenemos el campo de la llave del usuario del modal.
        keyValue = $('#keyValue').val();
        // Solamente funciona si el campo no es vacío.
        if(keyValue) {
            // Definimos una variable global para la llave introducida.
            window.key = keyValue;
            // Ocultamos el modal.
            $('#keyModal').modal('hide');
        }
    });

    // Acción al cliquear "Mostrar usuarios conectados".
    $('#users').click(function () {
        // Mandamos un JSON con el tipo de petición para obtener los usuarios.
        websocket.send(JSON.stringify({
            "tipo": "usuarios"
        }));
        // Ocultamos el desborde de acciones.
        $(this).parent().parent().toggle();
    });

    // Al cliquear en un usuario conectado nos despliega su chat.
    $(document).on('click', '.contacts li', function () {
        // Obtenemos el nombre de usuario y le quitamos los espacios.
        let username = $(this).find(".username_info").text().replace(/\s/g, '');
        // A todos los chats le quitamos la clase active.
        $(this).parent().children().removeClass('active');
        // Al actual le agregamos la clase active.
        $(this).addClass('active');
        // Limpiamos los mensajes enviados anteriormente.
        $('#msg_card_body').empty();
        // Limpiamos el banner del nombre del chat abierto.
        $('#conversation').empty();
        // Agregamos el nombre del usuario al banner.
        $('#conversation').append(
            '<span>' +
                'Conversación con ' + username + "." +
            '</span>');
        // Le agregamos un atributo especial al botón.
        $('#button').attr('data-user', username);
    });

    // Si recibimos una respuesta del servidor mostramos el contenido.
    websocket.onmessage = function (evt) {
        // Convierte en objeto la cadena JSON recibida.
        var obj = JSON.parse(evt.data);
        // Imprime cada respuesta del servidor en consola.
        console.log(obj);
        switch (obj.tipo) {
            case "msj_nuevo":
                $(".msg_card_body").append(
                    '<div class="d-flex justify-content-start mb-4">' +
                        '<div class="img_cont_msg">' +
                            '<img src="webroot/img/man01.svg" class="rounded-circle user_img_msg">' +
                        '</div>' +
                        '<div class="msg_cotainer">' +
                        btoa(obj.msj) +
                            '<span class="msg_time">' +
                                obj.hora +
                            '</span>' +
                        '</div>' +
                    '</div>');
                break;
            default:
                break;
        }
        switch (obj.peticion) {
            case "usuarios":
                if(obj.ok) {
                    // Como regresa una cadena, quitamos el primer elemento [ y el
                    // útimo elemento ], las comillas simples y separa por comas.
                    userArray = obj.detalles.substr(1).slice(0, -1).replace(/'/gm, '').split(',');
                    // Primero limpiamos la sección anterior de usuarios conectados.
                    $(".contacts").empty();
                    // Para cada usuario imprimimos su respectivo cuadro de conectado.
                    for (let user of userArray) {
                        $(".contacts").append(
                            '<li>' +
                                '<div class="d-flex bd-highlight">' +
                                    '<div class="img_cont">' +
                                        '<img src="webroot/img/man01.svg" class="rounded-circle user_img">' +
                                        '<span class="online_icon"></span>' +
                                    '</div>' +
                                    '<div class="user_info">' +
                                        '<span class="username_info">' + 
                                            user +
                                        '</span>' +
                                        '<p>' +
                                            'Está en línea ahora.' +
                                        '</p>' +
                                    '</div>' +
                                '</div>' +
                            '</li>');
                    }
                }
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
    switch (month) {
        case 0: month = "Ene"; break;
        case 1: month = "Feb"; break;
        case 2: month = "Mar"; break;
        case 3: month = "Abr"; break;
        case 4: month = "May"; break;
        case 5: month = "Jun"; break;
        case 6: month = "Jul"; break;
        case 7: month = "Ago"; break;
        case 8: month = "Sep"; break;
        case 9: month = "Oct"; break;
        case 10: month = "Nov"; break;
        case 11: month = "Dic"; break;
    }
    let time = day + " " + month + " " + year + " ";
    time += (hour > 12) ? ((hour - 12 == 0) ? hour = 12 : (hour - 12)) 
                        : ((hour == 0) ? hour = 12 : hour);
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


class RC4 {
    constructor() {
        this.key = window.key;
    }

    /*
    * Función que implementa el cifrado RC4.
    * @param string key llave para encriptar/descencriptar.
    * @param string string cadena a encriptar/descencriptar.
    * @return string res el resultado de aplicar el método.
    */
    get_byte(key, str) {
        let s = [], j = 0, x, res = '';
        for (let i = 0; i < 256; i++) {
            s[i] = i;
        }
        for (i = 0; i < 256; i++) {
            j = (j + s[i] + key.charCodeAt(i % key.length)) % 256;
            x = s[i];
            s[i] = s[j];
            s[j] = x;
        }
        i = 0;
        j = 0;
        for (let y = 0; y < str.length; y++) {
            i = (i + 1) % 256;
            j = (j + s[i]) % 256;
            x = s[i];
            s[i] = s[j];
            s[j] = x;
            res += String.fromCharCode(str.charCodeAt(y) ^ s[(s[i] + s[j]) % 256]);
        }
        return res;
    }

    /**
     * Función que obtiene un número criptográficamente seguro en el rango [0,1).
     * @returns number 0 o 1 dependiendo si el resultado es mayor/menor que 0.5
     */
    cryptoRandom() {
        return (window.crypto.getRandomValues(new Uint32Array(1))[0] / 0x100000000) > 0.5 ? 1 : 0;
    }

    /**
     * Función para cifrar RC4.
     * @param {*} key 
     * @param {*} message 
     */
    crypt(key, message) {
        // Vector de Inicialización de 5 bytes para cada mensaje cifrado.
        let IV = Array.from(Array(5), () => this.cryptoRandom());
        let G = RC4(IV.concat(key));

        cypher = new Array(message.length);

        for(let i = 0; i < message.length - 1; i++) {
            cypher[i] = message[i] && G.get_byte();
        }

        return IV.concat(cypher);
    }

    /**
     * Función para descifrar RC4.
     * @param {*} key 
     * @param {*} message 
     */
    decrypt(key, cypher) {
        let IV = [];

        // Obtiene los primeros 5 elementos del IV.
        cypher.slice(0, 5).map(i => {
            IV.push(i);
        });

        cypher.splice(0, 5);

        let G = RC4(IV.concat(key));

        message = new Array(cypher.length);
        for(let i = 0; i < message.length - 1; i++) {
            message[i] = cypher[i] && G.get_byte();
        }

        return message;
    }
}
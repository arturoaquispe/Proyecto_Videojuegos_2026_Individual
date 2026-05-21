# ==========================================
# RESACA Y HORIZONTE - SCRIPT EJECUTABLE (ASSETS COMENTADOS)
# ==========================================
define l = Character("Leo", color="#c8a2ff")
define b = Character("Bernard", color="#ff9e5e")
define n = Character("", color="#a0a0a0")

default avoidance = 0        # 0=enfrenta, 1=pospone, 2=huye
default drinking = "moderate" # "controlled", "moderate", "heavy"
default bernard_tie = "close" # "close", "strained", "broken"
default impulse = 0          # 0=cauteloso, 1=contenido, 2=imprudente
default project_status = "touched" # "touched", "delayed", "ignored"

# ==========================================
# INICIO
# ==========================================
label start:
    # scene black with fade
    # play music "rain_window.mp3" fadein 1.0
    n "No es que no quiera hacerlo. Es que no sé ni por dónde empezar."
    n "El proyecto del electivo lleva dos semanas sin tocarlo. El correo sigue ahí."
    jump act1

# ==========================================
# ACTO 1: LA PLAYA (ESCAPE) - PUENTE FUNCIONAL
# ==========================================
label act1:
    # scene bg_dorm_evening with fade
    # play music "lofi_rain.mp3" fadein 1.0
    # show leo desk with dissolve

    n "La laptop abierta. El documento en blanco. El correo del profesor dice: 'Avance obligatorio para el viernes'."
    n "Lo relees. No respondes. Cierras la pestaña."

    menu:
        "Responder 'Ya voy avanzando' y cerrar la laptop.":
            $ avoidance = 1
            $ project_status = "delayed"
            l "Mentira piadosa. Pero al menos cierra la notificación."
            n "El silencio vuelve. El problema sigue ahí."

        "Escribir tres líneas feas y guardarlas.":
            $ avoidance = 0
            $ project_status = "touched"
            l "No está bien, pero ya no está vacío."
            n "Guardar duele menos que mirar la pantalla vacía."

        "Apagar la laptop sin leer el correo.":
            $ avoidance = 2
            $ project_status = "ignored"
            l "Mañana. O pasado. Ya veremos."
            n "La oscuridad gana por hoy."

    # play sound phone_vibrate.mp3
    n "El teléfono vibra. Bernard."
    b "[Mensaje] Cancha pública. 7PM. Trae hielos. Necesito despejarme de la tesis."
    b "[Mensaje] Tú también lo necesitas. No preguntes."

    menu:
        "Responder 'Voy' sin pensarlo.":
            $ drinking = "moderate"
            $ impulse = 0
            l "Voy. La rutina pesa menos que la pregunta."
            n "Te vistes. Las llaves. Las latas. El mismo circuito."

        "Responder '¿Estás bien? Suena pesado lo de la tesis'.":
            $ bernard_tie = "close"
            $ drinking = "controlled"
            l "¿Todo bien? La tesis no te deja ni respirar, ¿no?"
            b "[Audio] Me subo y me bajo de golpe. Hoy quiero solo no pensar."
            n "No es un drama. Es un cansancio real."

        "Proponer: 'Vamos si primero ordeno dos párrafos del proyecto'.":
            $ avoidance = 0
            $ bernard_tie = "close"
            $ impulse = 0
            l "Te llevo a la cancha si me ayudas a revisar lo que tengo. Trato."
            b "[Audio] Negociando como adulto. Me gusta. Dame 20. Paso por ti."
            n "No es heroísmo. Es poner un límite pequeño."

    jump act2

# ==========================================
# ACTO 2: LA RESACA (CONFRONTACIÓN) - INTERCONECTADO
# ==========================================
label act2:
    # scene bg_room_morning with fade
    # play music "morning_static.mp3" fadein 1.0
    # show leo bed with dissolve

    n "Amanece. La boca seca. La luz entra sin permiso."
    n "Teléfono: 4 notificaciones."
    n "2 de la facultad: 'Recordatorio: proyecto electivo'. 'Tutoría cancelada'."
    n "1 de Bernard: 'Cancha 7AM. Trae agua. No seas zombie'."
    n "1 sin nombre: 'Tu avance sigue pendiente'. Lo borras."

    menu:
        "Abrir el documento y escribir aunque sea una página.":
            $ avoidance = 0
            $ project_status = "touched"
            n "No es bueno, pero está escrito. El cursor ya no parpadea en blanco."
            l "Al menos ya no está vacío."

        "Responder el correo con 'Estoy organizando la estructura' y dejarlo.":
            $ avoidance = 1
            $ project_status = "delayed"
            n "Mentira ordenada. Cierras la laptop. El alivio dura tres minutos."
            l "Mañana lo tomo en serio."

        "Apagar el teléfono. Taparte la cabeza con la almohada.":
            $ avoidance = 2
            $ project_status = "ignored"
            n "El silencio gana. El tiempo sigue corriendo."
            l "No puedo con esto hoy."

    jump act2_court

# ==========================================
# ESCENA: CANCHA AMATEUR (ESPEJO EXTERNO)
# ==========================================
label act2_court:
    # scene bg_court_morning with fade
    # play music "ball_bounce_cheap.mp3" fadein 1.0
    # show bernard stretching at center with dissolve
    # show leo walking at left with dissolve

    n "La cancha de la esquina. Aros con malla rota. Tres vecinos ya están jugando 2vs2."
    n "No hay uniforme, ni árbitro, ni entrenador. Solo risas y rebotes torcidos."

    b "Llegaste. Creí que te habías quedado pegado a la cama."
    if avoidance == 0:
        l "Vine. Abrí el documento. No es mucho, pero ya no está en blanco."
        b "Eso suena a que no te estás rindiendo."
        $ bernard_tie = "close"
    elif avoidance == 1:
        l "Vine. El proyecto... lo estoy acomodando. Paso a paso."
        b "Paso a paso está bien. No te exijas de golpe."
        $ bernard_tie = "strained" if drinking == "heavy" else "close"
    else:
        l "Vine porque dijiste. Nada más."
        b "..."
        b "Está bien. Juguemos."
        $ bernard_tie = "strained"

    n "Bernard te pasa una botella de agua. La abres o la dejas."

    menu:
        "Tomar agua. Quedarte cerca de la cancha. Respirar.":
            $ drinking = "controlled"
            n "El agua fría corta la resaca. No cura. Pero ordena."
            l "Hoy no bebo. Solo estoy."

        "Tomar la cerveza que Bernard saca de la mochila.":
            $ drinking = "moderate"
            n "El primer trago quema. El segundo adormece. El tercero calla."
            l "Un par. Solo para bajar el ruido."
            if avoidance == 2:
                $ impulse = 1

        "Pedirle a Bernard si tiene algo más fuerte.":
            $ drinking = "heavy"
            $ impulse = 2
            n "No es sed. Es apagar. El líquido baja rápido. La mente baja más lento."
            l "Necesito que pare. Ya."

    n "Bernard juega. Tú miras o juegas. El balón va y viene. Su energía sube y baja sin aviso."
    b "Hoy la tesis me tiene podrido. Un día avanzo, al otro no entiendo lo que escribí."
    b "¿Tú cómo vas con el electivo?"

    menu:
        "Decir la verdad: 'No sé ni por dónde empezar, pero no quiero dejarlo'." if avoidance <= 1 else "Mentir: 'Va bien. Solo le falta pulir'." if avoidance == 2:
            if avoidance <= 1:
                l "No sé ni por dónde empezar, pero no quiero dejarlo a medias."
                b "Eso es suficiente. No tiene que ser perfecto, solo tiene que avanzar."
                $ bernard_tie = "close"
            else:
                l "Va bien. Solo le falta pulir."
                b "¿Seguro? Suena a que lo estás posponiendo."
                $ bernard_tie = "broken" if drinking == "heavy" else "strained"

        "Cambiar de tema. Hablar de la cancha, de los vecinos, de nada.":
            n "El balón rebota. El tema se desvía. La pregunta queda flotando."
            b "Tú siempre cambiando de marcha. Está bien. No voy a presionarte."

        "Quedarte callado. Asentir. Seguir mirando el juego.":
            $ avoidance = 2 if avoidance < 2 else avoidance
            n "No respondes. El silencio se vuelve pesado. Bernard lo nota."
            b "Si no quieres hablar, está bien. Pero no te pierdas, hermano."

    jump act2_evening

# ==========================================
# ESCENA: NOCHE / PUNTO DE QUIEBRE
# ==========================================
label act2_evening:
    # scene bg_streets_night with fade
    # play music "city_hum.mp3" fadein 1.0
    # show leo standing at center with dissolve

    n "Anochece. La cabeza gira. El cuerpo pide pausa o más ruido."
    n "Bernard te manda un mensaje: '¿Todo bien? No me dejaste claro si vienes a la cancha mañana'."

    if drinking == "heavy" and impulse >= 2:
        menu:
            "Salir a caminar solo. Cruzar la avenida. No mirar.":
                jump path_accident
            "Quedarte en el cuarto. Mezclar lo que queda. Ignorar el teléfono.":
                jump path_overdose
            "Llamar a Bernard. Decirle: 'No estoy bien. Necesito que vengas'." if bernard_tie != "broken":
                jump path_spiral
    elif drinking == "moderate" or avoidance >= 1:
        menu:
            "Abrir el documento. Escribir sin editar. Cerrar y dormir.":
                jump path_resolution
            "Beber un poco más. Posponer hasta mañana.":
                jump path_spiral
            "Salir a caminar. Respirar. Volver sin prisas.":
                jump path_bridge
    else:
        menu:
            "Terminar lo pendiente. Apagar la laptop. Descansar.":
                jump path_resolution
            "Quedarte mirando la pantalla. No tocar el teclado.":
                jump path_bridge
            "Salir. Caminar. Dejar que el aire limpie la cabeza.":
                jump path_choice

    jump act3_fallback

# ==========================================
# ACTO 3: CONVERGENCIA SEGÚN TRAYECTORIA
# ==========================================
label path_resolution:
    # scene bg_library_corner with fade
    # play music "quiet_pages.mp3" fadein 1.0
    n "No es epifanía. Es oficio."
    l "Termino porque ya no quiero cargar con lo pendiente. No por pasión, por honestidad."
    n "El documento se guarda. La pantalla se apaga. El peso se vuelve movimiento."
    jump ending_bridge

label path_bridge:
    # scene bg_library_window with fade
    # play music "hopeful_strings.mp3" fadein 1.0
    n "El título no es el destino. Es el puente."
    l "Termino para poder elegir. No para tener todas las respuestas."
    b "[Audio] Mañana cancha. Trae tu mejor cara de superviviente."
    n "Sonríes. No por el futuro. Por el presente que por fin dejas avanzar."
    jump ending_bridge

label path_choice:
    # scene bg_open_road with fade
    # play music "clear_piano.mp3" fadein 1.0
    n "Por primera vez, el silencio no asusta. Ordena."
    l "Acabo porque finalmente elijo. No por el papel. Por la capacidad de decidir."
    n "No sabes qué viene después. Y eso, por fin, no es miedo."
    n "Es espacio."
    jump ending_choice

label path_spiral:
    # scene bg_dorm_night with fade
    # play music "static_hum.mp3" fadein 1.0
    n "Las latas se acumulan. El documento sigue abierto, pero ya no lo miras."
    n "Bernard te escribe. No respondes. El teléfono se apaga."
    l "Mañana será otro día. O no."
    n "El ciclo se cierra sin drama. Solo con peso que se vuelve rutina."
    jump ending_spiral

label path_accident:
    # scene bg_street_night with fade
    # play music "car_pass.mp3" fadein 1.0
    n "Sales tarde. La cabeza nublada. Cruzas sin mirar."
    n "El freno rechina. El impacto es seco."
    n "No hay música de fondo. Solo el sonido de las llantas y el silencio que sigue."
    jump ending_accident

label path_overdose:
    # scene bg_room_night with fade
    # play music "slow_heartbeat.mp3" fadein 1.0
    n "Una cerveza. Otra. Un trago fuerte. El cuerpo deja de responder."
    n "No es un drama de película. Es un descuido acumulativo."
    n "El teléfono vibra. Nadie contesta."
    jump ending_overdose

label act3_fallback:
    jump path_bridge

# ==========================================
# FINALES (5 VARIANTE CON CAUSALIDAD)
# ==========================================
label ending_spiral:
    "Final: Espiral de postergación"
    n "El proyecto se queda a medias. La resaca se vuelve hábito. Bernard deja de escribir."
    n "No es un final trágico. Es un final que se elige todos los días, sin darse cuenta."
    menu:
        "Reiniciar":
            $ avoidance = 0
            $ drinking = "moderate"
            $ bernard_tie = "close"
            $ impulse = 0
            $ project_status = "touched"
            jump start
    return

label ending_accident:
    "Final: Noche sin retorno"
    n "El impacto no perdona. La calle no juzga. Solo registra."
    n "Nadie supo que esa noche era la última. Solo tú, caminando para olvidar lo que no sabías enfrentar."
    menu:
        "Reiniciar":
            $ avoidance = 0
            $ drinking = "moderate"
            $ bernard_tie = "close"
            $ impulse = 0
            $ project_status = "touched"
            jump start
    return

label ending_overdose:
    "Final: Límite cruzado"
    n "El cuerpo pide pausa. La mente pide más. El equilibrio se rompe."
    n "No fue intencional. Fue acumulativo. Un trago tras otro, hasta que el cuerpo dijo basta."
    menu:
        "Reiniciar":
            $ avoidance = 0
            $ drinking = "moderate"
            $ bernard_tie = "close"
            $ impulse = 0
            $ project_status = "touched"
            jump start
    return

label ending_bridge:
    "Final: Puente, no destino"
    n "El título no es la meta. Es la herramienta."
    n "Terminas para poder caminar. No para saber hacia dónde, sino para poder elegir el paso."
    menu:
        "Reiniciar":
            $ avoidance = 0
            $ drinking = "moderate"
            $ bernard_tie = "close"
            $ impulse = 0
            $ project_status = "touched"
            jump start
    return

label ending_choice:
    "Final: Elección"
    n "Aceptas que no habrá certezas. Y eso, por fin, te libera."
    n "Cierras el ciclo. No porque sea perfecto, sino porque es tuyo."
    menu:
        "Reiniciar":
            $ avoidance = 0
            $ drinking = "moderate"
            $ bernard_tie = "close"
            $ impulse = 0
            $ project_status = "touched"
            jump start
    return

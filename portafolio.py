import streamlit as st  # type: ignore

# Configurar la página
st.set_page_config(page_title="Portafolio - Juan David", page_icon="🚀", layout="wide")

# Barra lateral de navegación
st.sidebar.title("Navegación")
seccion = st.sidebar.radio("Ir a:", ["Inicio", "Sobre mí", "Trayecto académico", "Proyectos", "Contacto"])

# Página de Inicio
if seccion == "Inicio":
    with st.container():
        st.title("🦾 Portafolio de Juan David")

        col1, col2 = st.columns([1, 1])  # Dividimos en dos columnas

        with col1:
            st.subheader("Bienvenido 👋")
            st.write(
                """
                Explora mis proyectos en ingeniería biomédica, diseño CAD, programación y automatización.  
                Me apasiona la tecnología y su aplicación en el sector salud.  
                """
            )
            st.markdown("🔹 **Ingeniería Biomédica**  \n🔹 **Diseño CAD & Impresión 3D**  \n🔹 **Programación en Python & MATLAB**  \n 🔹 **Creación de flujos de trabajo con N8N**")

        with col2:
            try:
                st.video("video.mp4") 
            except Exception as e:
                st.error(f"No se pudo cargar el video: {e}")

        st.divider()  

# Sobre mí
elif seccion == "Sobre mí":
    st.header("🧑‍💻 Sobre mí")

    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            st.image("Imagen.jpeg", caption="Foto de Juan David", width=250)
        except Exception as e:
            st.error(f"No se pudo cargar la imagen: {e}")

    with col2:
        st.write("""
        Soy ingeniero biomédico egresado de la Universidad Antonio Nariño de Colombia.
Elegí esta profesión porque creo firmemente que la ingeniería desempeña un papel esencial en el progreso del sector salud.
Me apasiona combinar el conocimiento técnico con la innovación para desarrollar soluciones que mejoren la calidad de vida de las personas.
Aunque tengo una sólida formación en electrónica, mi principal interés se centra en la informática, el análisis de datos y la aplicación de la inteligencia artificial
        """)

    st.divider()

    # Habilidades y herramientas
    st.subheader("Habilidades y herramientas")

    col1, col2 = st.columns(2)

    with col1:
        try:
            st.image("fusion.png", width=40)
            st.subheader("Fusion360")
            st.write("🔹 Diseño y prototipado de prótesis para impresión 3D.")
            st.progress(75)

            st.image("python.png", width=40)
            st.subheader("Python")
            st.write("🔹 Desarrollo web y automatización de procesos.")
            st.progress(70)

            st.image("streamlit.png", width=40)
            st.subheader("Streamlit")
            st.write("🔹 Creación de aplicaciones web interactivas.")
            st.progress(45)

        except Exception as e:
            st.error(f"No se pudo cargar una imagen: {e}")

    with col2:
        try:
            st.image("revit.jpg", width=40)
            st.subheader("Revit")
            st.write("🔹 Diseño y modelado arquitectónico básico.")
            st.progress(40)

            st.image("Matlab.png", width=40)
            st.subheader("Matlab")
            st.write("🔹 Procesamiento de señales e imágenes médicas.")
            st.progress(70)

            st.image("images.png", width=40)
            st.subheader("N8N")
            st.write("🔹 Creación de flujos de trabajo.")
            st.progress(60)
        
        except Exception as e:
            st.error(f"No se pudo cargar una imagen: {e}")

    st.divider()

    # Sección expandible con más detalles
    with st.expander("Más sobre mis habilidades"):
        st.write("""
        - En **Fusion 360**, desarrollo modelos 3D para prótesis y dispositivos médicos.
        - Con **Python**, estoy creando aplicaciones interactivas y mejorando mi lógica de programación.
        - **Streamlit** me permite construir aplicaciones de datos rápidamente.
        - Uso **Revit** para proyectos interdisciplinarios en ingeniería biomédica.
        - En **Matlab**, trabajo con procesamiento de señales e imágenes médicas.
        - **N8N**, Utilizo el interfaz para crear optimizaciones, mediante el uso de flujos de trabajo.
        """)

    st.subheader("Enfoque profesional")
    st.write("Soy ingeniero con una sólida formación en ingeniería biomédica y un profundo interés en la aplicación de la tecnología para generar impacto social y empresarial. Mi enfoque profesional se orienta hacia el desarrollo y la implementación de soluciones basadas en inteligencia artificial, automatización y análisis de datos, con el propósito de optimizar procesos, mejorar la toma de decisiones y fomentar la innovación en diversos sectores. Me motiva crear sistemas inteligentes y flujos de trabajo eficientes que integren la ingeniería, la informática y la creatividad, contribuyendo al crecimiento sostenible de las organizaciones. Mantengo un compromiso constante con la ética, la responsabilidad social y el aprendizaje continuo, buscando siempre que la tecnología sea una herramienta para el bienestar humano y el progreso colectivo.")

# Trayecto académico
elif seccion == "Trayecto académico":
    st.header("Trayecto académico")
    st.write("🔹Bachiller gimnasio bilingue campestre marie curie")
    st.write("🔹Técnico laboral en habilidades en programación con énfasis en aplicaciones web UNAB")
    st.write("🔹Curso en Tecnovigilacia UAN")
    st.write("🔹Ingeniero biomédico")

# Proyectos
elif seccion == "Proyectos":
    st.header("📂 Proyectos")

    # Diccionario con proyectos y sus imágenes
    proyectos = {
        "Diseño de prótesis en Fusion 360": {
            "descripcion": "Diseñé una prótesis impresa en 3D capaz de realizar movimientos de flexión y extensión de las falanges. Su funcionamiento se basa en una señal electromiográfica que controla un servomotor ",
            "imagen1": "Protesis.jpeg"
        },
        "Diseño de nebulizador en Fusion 360": {
            "descripcion": "Diseñé e imprimí el hardware de un nebulizador portátil.",
            "imagen1": "Neb.jpeg"
        },
        "Diseño de PCB nebulizador": {
            "descripcion": "Diseñé e implementé el software de un nebulizador portátil.",
            "imagen1": "Pcb1.jpeg"
        },
        "Detección de cáncer de pulmón con MATLAB": {
            "descripcion": "Desarrollé un código en MATLAB para analizar imágenes de tomografía computarizada y determinar la presencia de cáncer, diferenciando entre casos benignos y malignos mediante técnicas de procesamiento de imágenes y análisis de características.",
            "imagen1": "Mat1.jpg"
        },
        "Diseño de urgencias en Revit": {
            "descripcion": "Diseñé los planos del área de urgencias, asegurando el cumplimiento de la normatividad establecida para garantizar un entorno seguro, funcional y eficiente en la atención médica.",
            "imagen1": "Revit1.jpg"
        },
        "Optimización de respuestas para ecommerce": {
            "descripcion": "Realicé la optimización y automatización a una tienda de ecommerce, en donde se brinda una respuesta autónoma a los clientes por medio de whatsapp, lo que permite al empleador disminuir tiempo en respuestas a clientes y aumentar las ventas.",
            "imagen1": "n8n.png"
        }
    }   

    for nombre, data in proyectos.items():
        with st.expander(nombre):
            col1, col2 = st.columns(2)

            with col1:
                try:
                    st.image(data["imagen1"], width=300, caption=f"{nombre}")
                except Exception as e:
                    st.error(f"No se pudo cargar la imagen del proyecto: {e}")

            with col2:
                st.write(data["descripcion"])

# Contacto
elif seccion == "Contacto":
    st.header("📩 Contacto")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Conéctate conmigo")
        st.markdown("[💼 **LinkedIn**](https://www.linkedin.com/in/juan-david-0885541b0)")
        st.markdown("📧 **Email**: juandabnm89@gmail.com")
        
        st.divider()
        
        st.markdown("**O envíame un mensaje rápido:**")
        st.link_button("💬 WhatsApp", "https://wa.me/573238071637?text=Hola%20Juan,%20vi%20tu%20portafolio%20en%20ingenier%C3%ADa%20biom%C3%A9dica%20y%20me%20gustar%C3%ADa%20charlar%20sobre%20oportunidades", help="Abre WhatsApp con un mensaje prellenado")
    
    with col2:
        with st.form("contacto_form"):
            nombre = st.text_input("Nombre")
            email = st.text_input("Correo electrónico")
            mensaje = st.text_area("Mensaje")
            enviar = st.form_submit_button("Enviar")

            if enviar:
                # Aquí puedes agregar el código para enviar el mensaje a un backend si lo deseas
                st.success("¡Mensaje enviado! Te respondo pronto. 🚀")
    
    st.divider()
    st.caption("¡Gracias por tu interés! Estoy emocionado por conectar y colaborar en proyectos innovadores. ")
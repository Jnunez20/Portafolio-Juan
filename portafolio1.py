import streamlit as st  # type: ignore

# Configurar la página
st.set_page_config(page_title="Portafolio - Juan David", page_icon="🚀", layout="wide")

# Barra lateral de navegación
st.sidebar.title("Navegación")
seccion = st.sidebar.radio("Ir a:", ["Inicio", "Sobre mí", "Proyectos", "Contacto"])

# Página de Inicio
if seccion == "Inicio":

    
    with st.container():
        st.title("🦾 Portafolio de Juan David")
        
        col1, col2 = st.columns([1, 1])  # Dividimos en dos columnas
        
        with col1:
            st.subheader("Bienvenido 👋")
            st.write(
                """
                Explora mis proyectos en ingeniería biomédica, diseño CAD y programación.  
                Me apasiona la tecnología y su aplicación en el sector salud.  
                """
            )
            st.markdown("🔹 **Ingeniería Biomédica**  \n🔹 **Diseño CAD & Impresión 3D**  \n🔹 **Programación en Python & MATLAB**")

        with col2:
            
            st.video("video.mp4") 
            
        
        st.divider()  

# Sobre mí
elif seccion == "Sobre mí":
    st.header("🧑‍💻 Sobre mí")

    
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("Imagen.jpeg", caption="Foto de Juan David", width=250)

    with col2:
        st.write("""
        Actualmente soy estudiante de **Ingeniería Biomédica** en la Universidad Antonio Nariño de Colombia.  
        Elegí este camino porque considero que la ingeniería tiene un papel fundamental en el área de la salud.  
        Me apasiona la idea de **crear, diseñar, solucionar problemas e innovar** para contribuir al bienestar de las personas y al avance de la medicina.
        """)

    st.divider()

    # Habilidades y herramientas
    st.subheader("Habilidades y herramientas")

    col1, col2 = st.columns(2)

    with col1:
        st.image("fusion.png",width=40)
        st.subheader("Fusion360")
        st.write("🔹 Diseño y prototipado de prótesis para impresión 3D.")
        st.progress(75)

        st.image("python.png",width=40)
        st.subheader("Python")
        st.write("🔹 Desarrollo web y automatización de procesos.")
        st.progress(70)

        st.image("streamlit.png",width=40)
        st.subheader("Streamlit")
        st.write("🔹 Creación de aplicaciones web interactivas.")
        st.progress(45)

    with col2:
        st.image("revit.jpg",width=40)
        st.subheader("Revit")
        st.write("🔹 Diseño y modelado arquitectónico básico.")
        st.progress(40)

        st.image("Matlab.png",width=40)
        st.subheader("Matlab")
        st.write("🔹 Procesamiento de señales e imágenes médicas.")
        st.progress(70)

    st.divider()

    # Sección expandible con más detalles
    with st.expander("Más sobre mis habilidades"):
        st.write("""
        - En **Fusion 360**, desarrollo modelos 3D para prótesis y dispositivos médicos.
        - Con **Python**, estoy creando aplicaciones interactivas y mejorando mi lógica de programación.
        - **Streamlit** me permite construir aplicaciones de datos rápidamente.
        - Uso **Revit** para proyectos interdisciplinarios en ingeniería biomédica.
        - En **Matlab**, trabajo con procesamiento de señales e imágenes médicas.
        """)

    st.subheader(" Enfoque profesional")
    st.write("Mi enfoque profesional está centrado en la integración de la ingeniería con el sector de la salud para desarrollar soluciones innovadoras y accesibles. Como estudiante de Ingeniería Biomédica, busco aplicar mis conocimientos en diseño, programación y análisis de datos para mejorar la calidad de vida de las personas. Me interesa trabajar en el diseño y desarrollo de dispositivos médicos, tecnologías de asistencia y sistemas que optimicen procesos dentro del ámbito sanitario. Estoy comprometido con la investigación y el aprendizaje continuo, y me esfuerzo por combinar la creatividad y el pensamiento crítico para resolver problemas complejos, siempre con un enfoque ético y orientado al bienestar humano.")
    
    

elif seccion == "Proyectos":
    st.header("📂 Proyectos")

    # Diccionario con proyectos y sus imágenes
    proyectos = {
    "Diseño de prótesis en Fusion 360": {
        "descripcion": "Creé un mecanismo de dedos tipo pinza con servomotores.",
        "imagen1": "protesis.jpeg"
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
        "descripcion": "Desarrollé un código en Matlab para identificar cáncer benigno o maligno con imágenes de tomografía computarizada.",
        "imagen1": "Mat1.jpg"
    },
    "Diseño de urgencias en Revit": {
        "descripcion": "Diseñé los planos del área de urgencias junto con la normatividad establecida.",
        "imagen1": "Revit1.jpg"
    },
}   

st.header("Mis Proyectos")

for nombre, data in proyectos.items():
    with st.expander(nombre):
        col1, col2 = st.columns(2)

        with col1:
            st.image(data["imagen1"], width=300, caption=f"{nombre}")

        with col2:
            st.write(data["descripcion"])
            

# Contacto
if seccion == "Contacto":
    st.header("📩 Contacto")
    st.write("Puedes contactarme en [LinkedIn](https://www.linkedin.com/) o por email: juandabnm89@gmail.com")
    
    with st.form("contacto_form"):
        nombre = st.text_input("Nombre")
        email = st.text_input("Correo electrónico")
        mensaje = st.text_area("Mensaje")
        enviar = st.form_submit_button("Enviar")
    
        if enviar:
            st.success("Mensaje enviado. ¡Gracias por contactarme!")

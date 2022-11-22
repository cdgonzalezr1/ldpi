import streamlit as st
import pandas as pd
import os 
import markdown

from datetime import date


st.set_page_config(page_title="Chris Liderazgo por Influencia", page_icon="leader.png", layout="wide", initial_sidebar_state="expanded")

with st.sidebar: 
    
    st.image("leader.png")
    st.title("Chris Liderazgo por Influencia")
    choice = st.radio("Navegación", ["Contesta","Ejecuta"])
    st.info("¡Lidera al equipo de trabajo con metodologías científicas!")

if choice == "Contesta":
    st.title("Inicia una reunión con tu equipo de trabajo y sigue estos pasos:")
    st.markdown("<hr/>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("**Nombre del proyecto**, por ejemplo: 'Selector de transportadoras' o 'Modelo de pricing'")
        project_name = st.text_input("Nombre del proyecto")
    with col2:
        st.write("**Nombre del lider**, por ejemplo: 'Juan Perez' o 'Maria Lopez' o 'Carlos Garcia'")
        leader_name = st.text_input("Nombre del lider")
    with col3:
        st.write("**¿Cuál es el propósito que quieres cumplir?** 'Llevar el ontime al 99%' o 'Aumentar el margen de inelásticos en 7%'")
        purpose = st.text_input("Propósito")
    with col4:
        st.write("**¿Cuál es la métrica que vas evaluar constantemente para cumplir el propósito?**, por ejemplo: 'Ontime' o 'Margen'")
        metric = st.text_input("Métrica")

    st.markdown("<hr/>", unsafe_allow_html=True)

    col5, col6 = st.columns(2)
    with col5:
        st.write("**¿Qué tan solidos o buenos son los conocimientos y habilidades demostrados por la persona con respeto a la tarea?**")
        conocimiento = st.selectbox("Nivel de conocimiento", ["Alto", "Bajo"])
    with col6:
        st.write("**¿Cómo de solidas o buenas son las habilidades transferibles de esa persona?**")
        habilidades = st.selectbox("Nivel de habilidades", ["Alto", "Bajo"])
    with col5:
        st.write("**¿Cómo está la persona de motivada, interesada o entusiasmada?**")
        motivacion = st.selectbox("Nivel de motivación", ["Alto", "Bajo"])
    with col6:
        st.write("**¿Cuánta seguridad o confianza tiene la persona en si misma (respecto a la tarea)?**")
        confianza = st.selectbox("Nivel de confianza", ["Alto", "Bajo"])

    col7, col8, col9 = st.columns(3)
    with col8:
        st.write("")
        st.write("")
        st.write("")

        if st.button("✊🤩👽 Realizar envío y ver resultados para gestionar la reunión 👽🤩✊"):
            if conocimiento == "Bajo" and habilidades == "Bajo" and motivacion == "Alto" and confianza == "Bajo":
                nombre = "Principante entusiasta"
                caracteristicas = "Esperanzado, inexperto, curioso, le falta conocimiento o habilidades transferibles o confianza, nuevo o carente de habilidades, optimista, expectante, ansioso, entusiasta."
                hacer = "Dirigirlo mucho y apoyarlo poco, ante todo dirigirlo, resaltar sus habilidades y educarlo."
                pasos = "Definir, Planificar o asignar prioridades, orientar, enseñar o demostrar y decir como hacer las cosas, comprobar o ejercer control, dar retroalimentación."
                necesidad = "Reconocerle el entusiasmo y las habilidades transferibles, el líder decide, no asignarle cosas ambiguas, darle metas y funciones claras, darle estándares de que es un trabajo bien hecho, ayudarle a establecer prioridades, darle fuentes donde conseguir información, darle planes de como se hace, para cuando y por que, demarcarle los limites. Hablarle y decirle como funcionan las cosas aquí, darle ejemplos, solucionarle sus problemas, no responderle con preguntas."
            if conocimiento == "Bajo" and habilidades == "Alto" and motivacion == "Alto" and confianza == "Bajo":
                nombre = "Principante entusiasta"
                caracteristicas = "Esperanzado, inexperto, curioso, le falta conocimiento o habilidades transferibles o confianza, nuevo o carente de habilidades, optimista, expectante, ansioso, entusiasta."
                hacer = "Dirigirlo mucho y apoyarlo poco, ante todo dirigirlo, resaltar sus habilidades y educarlo."
                pasos = "Definir, Planificar o asignar prioridades, orientar, enseñar o demostrar y decir como hacer las cosas, comprobar o ejercer control, dar retroalimentación."
                necesidad = "Reconocerle el entusiasmo y las habilidades transferibles, el líder decide, no asignarle cosas ambiguas, darle metas y funciones claras, darle estándares de que es un trabajo bien hecho, ayudarle a establecer prioridades, darle fuentes donde conseguir información, darle planes de como se hace, para cuando y por que, demarcarle los limites. Hablarle y decirle como funcionan las cosas aquí, darle ejemplos, solucionarle sus problemas, no responderle con preguntas."
            if conocimiento == "Bajo" and habilidades == "Bajo" and motivacion == "Alto" and confianza == "Alto":
                nombre = "Principiante entusiasta, con confianza en si mismo"
                caracteristicas = "Esperanzado, inexperto, curioso, nuevo o carente de habilidades, optimista, expectante, ansioso, entusiasta."
                hacer = "Dirigirlo mucho y apoyarlo poco, ante todo dirigirlo, resaltar sus habilidades y educarlo."
                pasos = "Definir, Planificar o asignar prioridades, orientar, enseñar o demostrar y decir como hacer las cosas, comprobar o ejercer control, dar retroalimentación."
                necesidad = "Reconocerle el entusiasmo y las habilidades transferibles, el líder decide, no asignarle cosas ambiguas, darle metas y funciones claras, darle estándares de que es un trabajo bien hecho, ayudarle a establecer prioridades, darle fuentes donde conseguir información, darle planes de como se hace, para cuando y por que, demarcarle los limites. Hablarle y decirle como funcionan las cosas aquí, darle ejemplos, solucionarle sus problemas, no responderle con preguntas."
            if conocimiento == "Bajo" and habilidades == "Alto" and motivacion == "Alto" and confianza == "Alto":
                nombre = "Principiante entusiasta, con confianza en si mismo"
                caracteristicas = "Esperanzado, inexperto, curioso, nuevo o carente de habilidades, optimista, expectante, ansioso, entusiasta."
                hacer = "Dirigirlo mucho y apoyarlo poco, ante todo dirigirlo, resaltar sus habilidades y educarlo."
                pasos = "Definir, Planificar o asignar prioridades, orientar, enseñar o demostrar y decir como hacer las cosas, comprobar o ejercer control, dar retroalimentación."
                necesidad = "Reconocerle el entusiasmo y las habilidades transferibles, el líder decide, no asignarle cosas ambiguas, darle metas y funciones claras, darle estándares de que es un trabajo bien hecho, ayudarle a establecer prioridades, darle fuentes donde conseguir información, darle planes de como se hace, para cuando y por que, demarcarle los limites. Hablarle y decirle como funcionan las cosas aquí, darle ejemplos, solucionarle sus problemas, no responderle con preguntas."
            if conocimiento == "Bajo" and habilidades == "Bajo" and motivacion == "Bajo" and confianza == "Bajo":
                nombre = "Aprendiz desilusionado"
                caracteristicas = "Apesumbrado, Confuso, Desmotivado, Desmoralizado, Frustrado, Desilusionado, Desalentado, Destellos de competencia."
                hacer = "Darle mucha dirección y mucho apoyo y ante todo entrenarlo."
                pasos = "Explorar o preguntar, explicar o aclarar, encauzar, compartir retroalimentación, estimular, elogiar."
                necesidad = "Metas claras, aliento, perspectiva, asesoramiento del proceso a seguir, perspectiva, retroalimentación frecuente,  asesoramiento para perfeccionar habilidades, hablemos pero finalmente yo le digo que hacer, elogio del proceso realizado, ayuda para analizar éxitos y fracasos, es aceptable cometer errores, explicarle el por que la tarea es importante."
            if conocimiento == "Bajo" and habilidades == "Alto" and motivacion == "Bajo" and confianza == "Bajo":
                nombre = "Aprendiz desilusionado"
                caracteristicas = "Apesumbrado, Confuso, Desmotivado, Desmoralizado, Frustrado, Desilusionado, Desalentado, Destellos de competencia."
                hacer = "Darle mucha dirección y mucho apoyo y ante todo entrenarlo."
                pasos = "Explorar o preguntar, explicar o aclarar, encauzar, compartir retroalimentación, estimular, elogiar."
                necesidad = "Metas claras, aliento, perspectiva, asesoramiento del proceso a seguir, perspectiva, retroalimentación frecuente,  asesoramiento para perfeccionar habilidades, hablemos pero finalmente yo le digo que hacer, elogio del proceso realizado, ayuda para analizar éxitos y fracasos, es aceptable cometer errores, explicarle el por que la tarea es importante."
            if conocimiento == "Bajo" and habilidades == "Bajo" and motivacion == "Bajo" and confianza == "Alto":
                nombre = "Aprendiz desilusionado"
                caracteristicas = "Apesumbrado, Confuso, Desmotivado, Desmoralizado, Frustrado, Desilusionado, Desalentado, Destellos de competencia."
                hacer = "Darle mucha dirección y mucho apoyo y ante todo entrenarlo."
                pasos = "Explorar o preguntar, explicar o aclarar, encauzar, compartir retroalimentación, estimular, elogiar."
                necesidad = "Metas claras, aliento, perspectiva, asesoramiento del proceso a seguir, perspectiva, retroalimentación frecuente,  asesoramiento para perfeccionar habilidades, hablemos pero finalmente yo le digo que hacer, elogio del proceso realizado, ayuda para analizar éxitos y fracasos, es aceptable cometer errores, explicarle el por que la tarea es importante."
            if conocimiento == "Alto" and habilidades == "Bajo" and motivacion == "Bajo" and confianza == "Alto":
                nombre = "Aprendiz desilusionado, tiene conocimiento pero le falta  motivación "
                caracteristicas = "Competente, Apesumbrado, Confuso necesita resaltar sus habilidades transferibles, Desmotivado con mucha necesidad de motivación, Desmoralizado, Frustrado."
                hacer = "Darle mucha dirección y mucho apoyo y ante todo entrenarlo, dejarlo probar y explorar, resaltar sus habilidades."
                pasos = "Explorar o preguntar, explicar o aclarar, encauzar, compartir retroalimentación, estimular, elogiar."
                necesidad = "Metas claras, aliento, perspectiva, asesoramiento del proceso a seguir, perspectiva, retroalimentación frecuente,  asesoramiento para perfeccionar habilidades, hablemos pero finalmente yo le digo que hacer, elogio del proceso realizado, ayuda para analizar éxitos y fracasos, es aceptable cometer errores, explicarle de por que la tarea es importante, ayudarlo a desarrollar sus habilidades, quitar cosas que se le interponen, dejarlo probar."
            if conocimiento == "Alto" and habilidades == "Bajo" and motivacion == "Bajo" and confianza == "Bajo":
                nombre = "Aprendiz desilusionado, tiene conocimiento pero le falta  motivación "
                caracteristicas = "Competente, Apesumbrado, Confuso necesita resaltar sus habilidades transferibles, Desmotivado con mucha necesidad de motivación, Desmoralizado, Frustrado."
                hacer = "Darle mucha dirección y mucho apoyo y ante todo entrenarlo, dejarlo probar y explorar, resaltar sus habilidades."
                pasos = "Explorar o preguntar, explicar o aclarar, encauzar, compartir retroalimentación, estimular, elogiar."
                necesidad = "Metas claras, aliento, perspectiva, asesoramiento del proceso a seguir, perspectiva, retroalimentación frecuente,  asesoramiento para perfeccionar habilidades, hablemos pero finalmente yo le digo que hacer, elogio del proceso realizado, ayuda para analizar éxitos y fracasos, es aceptable cometer errores, explicarle de por que la tarea es importante, ayudarlo a desarrollar sus habilidades, quitar cosas que se le interponen, dejarlo probar."
            if conocimiento == "Alto" and habilidades == "Bajo" and motivacion == "Alto" and confianza == "Bajo":
                nombre = "Colaborador capaz pero cauteloso, por falta de confianza, motivación o habilidades transferibles"
                caracteristicas = "Tiende a criticarse a si mismo, le falta un poco de motivación, confianza y habilidades transferibles, cauteloso, dudoso, capaz. aporta, inseguro, vacilante, aburrido o apático."
                hacer = "No darle dirección, darle apoyo, felicitarlo mucho y resaltar sus habilidades."
                pasos = "Preguntar o escuchar, dar seguridad, facilitar solución autónoma de problemas, colaborar, estimular retroalimentación, demostrar aprecio."
                necesidad = "Un mentor o entrenador, oportunidad para probar ideas, aliento u asesoría en el proceso a seguir, ayudarle a perfeccionar habilidades, mucho elogio, esta bien cometer errores, poder expresar sus preocupaciones y sentimientos, apoyo y estimulo para desarrollar sus habilidades con el fin de resolver problemas autónomamente, elogio y reconocimiento por niveles superiores de competencia, dejarlo probar ideas, apoyo para desarrollar sus habilidades, eliminación de obstáculos, empujón inicial eliminación de obstáculos para lograr sus metas. un empujón inicial para sobreponerse al habido de dejar las cosas para mañana, es aceptable cometer errores, explicarle de por que la tarea es importante."
            if conocimiento == "Alto" and habilidades == "Bajo" and motivacion == "Alto" and confianza == "Alto":
                nombre = "Colaborador capaz pero cauteloso, por falta de confianza, motivación o habilidades transferibles"
                caracteristicas = "Tiende a criticarse a si mismo, le falta un poco de motivación, confianza y habilidades transferibles, cauteloso, dudoso, capaz. aporta, inseguro, vacilante, aburrido o apático."
                hacer = "No darle dirección, darle apoyo, felicitarlo mucho y resaltar sus habilidades."
                pasos = "Preguntar o escuchar, dar seguridad, facilitar solución autónoma de problemas, colaborar, estimular retroalimentación, demostrar aprecio."
                necesidad = "Un mentor o entrenador, oportunidad para probar ideas, aliento u asesoría en el proceso a seguir, ayudarle a perfeccionar habilidades, mucho elogio, esta bien cometer errores, poder expresar sus preocupaciones y sentimientos, apoyo y estimulo para desarrollar sus habilidades con el fin de resolver problemas autónomamente, elogio y reconocimiento por niveles superiores de competencia, dejarlo probar ideas, apoyo para desarrollar sus habilidades, eliminación de obstáculos, empujón inicial eliminación de obstáculos para lograr sus metas. un empujón inicial para sobreponerse al habido de dejar las cosas para mañana, es aceptable cometer errores, explicarle de por que la tarea es importante."
            if conocimiento == "Alto" and habilidades == "Alto" and motivacion == "Bajo" and confianza == "Alto":
                nombre = "Colaborador capaz pero cauteloso, por falta de motivación."
                caracteristicas = "Tiende a criticarse a si mismo, le falta un poco de motivación, cauteloso, dudoso, capaz. aporta, inseguro, vacilante, aburrido o apático."
                hacer = "No darle dirección, darle apoyo, alentarlo a equivocarse, a probar."
                pasos = "Preguntar o escuchar, dar seguridad, facilitar solución autónoma de problemas, colaborar, estimular retroalimentación, demostrar aprecio."
                necesidad = "Un mentor o entrenador, oportunidad para probar ideas, aliento u asesoría en el proceso a seguir, ayudarle a perfeccionar habilidades, mucho elogio, esta bien cometer errores, poder expresar sus preocupaciones y sentimientos, apoyo y estimulo para desarrollar sus habilidades con el fin de resolver problemas autónomamente, elogio y reconocimiento por niveles superiores de competencia, dejarlo probar ideas, apoyo para desarrollar sus habilidades, eliminación de obstáculos, empujón inicial eliminación de obstáculos para lograr sus metas. un empujón inicial para sobreponerse al habido de dejar las cosas para mañana, es aceptable cometer errores, explicarle de por que la tarea es importante."
            if conocimiento == "Alto" and habilidades == "Alto" and motivacion == "Bajo" and confianza == "Bajo":
                nombre = "Colaborador capaz pero cauteloso"
                caracteristicas = "Tiende a criticarse a si mismo, le falta un poco de motivación, cauteloso, dudoso, capaz. aporta, inseguro, vacilante, aburrido o apático."
                hacer = "No darle dirección, darle apoyo, alentarlo a equivocarse, a probar."
                pasos = "Preguntar o escuchar, dar seguridad, facilitar solución autónoma de problemas, colaborar, estimular retroalimentación, demostrar aprecio."
                necesidad = "Un mentor o entrenador, oportunidad para probar ideas, poder expresar sus preocupaciones y sentimientos, apoyo y estimulo para desarrollar sus habilidades con el fin de resolver problemas autónomamente, elogio y reconocimiento por niveles superiores de competencia, eliminación de obstáculos para lograr sus metas. un empujón inicial para sobreponerse al habido de dejar las cosas para mañana."
            if conocimiento == "Alto" and habilidades == "Alto" and motivacion == "Alto" and confianza == "Bajo":
                nombre = "Colaborador autónomo falto de confianza "
                caracteristicas = "Demuestra competencia e todo momento pero no confía en sus capacidades, inspirado y/o inspira a los demás, experto, autónomo, le cuesta confiar en si mismo, tiene talento, independiente o se dirige a si mismo."
                hacer = "No dirigirlo casi, apoyarlo resto, delegarle cosas."
                pasos = "Permitir o depositar confianza, confirmar, facultar, afirmar, expresar reconocimiento, establecer desafíos"
                necesidad = "Variedad de tareas y desafíos con acompañamiento y asesoría en todo, dejarlo probar ideas, dejarlo compartir preocupaciones y sentimientos, un mentor y colega No un jefe, reconocimiento por las contribuciones hechas, autonomía y autoridad, confianza, oportunidad para compartir los conocimientos y habilidades con los demás, preguntarle usted que haría."
            if conocimiento == "Alto" and habilidades == "Alto" and motivacion == "Alto" and confianza == "Alto":
                nombre = "Colaborador autónomo y confiado"
                caracteristicas = "Su seguridad en si mismo esta justificada, demuestra competencia e todo momento, inspirado y/o inspira a los demás, experto, autónomo, confía en si mismo, tiene talento, independiente o se dirige a si mismo."
                hacer = "No dirigirlo casi, no apoyarlo casi, delegarle cosas."
                pasos = "Permitir o depositar confianza, confirmar, facultar, afirmar, expresar reconocimiento, establecer desafíos."
                necesidad = "Variedad de tareas y desafíos, un mentor y colega No un jefe, reconocimiento por las contribuciones hechas, autonomía y autoridad, confianza, oportunidad para compartir los conocimientos y habilidades con los demás."

            st.balloons()
            df = pd.DataFrame({
                'Nombre': [nombre],
                'Características': [caracteristicas],
                'Hacer': [hacer],
                'Pasos': [pasos],
                'Necesidad': [necesidad],
                'project_name'  : [project_name],
                'leader_name'  : [leader_name],
                'purpose'  : [purpose],
                'metric'  : [metric],
                'conocimiento'  : [conocimiento],
                'habilidades'  : [habilidades],
                'motivacion'  : [motivacion],
                'confianza'  : [confianza],
            })
            if os.path.exists('data.csv'):
                os.remove('data.csv')
            df.to_csv('data.csv', mode='a', header=True, index=False)
            st.markdown("<hr/>", unsafe_allow_html=True)


if choice == "Ejecuta":

        df = pd.read_csv('data.csv', sep=',')
        project_name = str(df['project_name'][0])
        leader_name = str(df['leader_name'][0])
        purpose = str(df['purpose'])[0]
        metric = str(df['metric'][0])
        conocimiento = str(df['conocimiento'][0])
        habilidades = str(df['habilidades'][0])
        motivacion = str(df['motivacion'][0])
        confianza = str(df['confianza'][0])
        nombre = str(df['Nombre'][0])
        caracteristicas = str(df['Características'][0])
        hacer = str(df['Hacer'][0])
        pasos = str(df['Pasos'][0])
        necesidad = str(df['Necesidad'][0])


        st.title("Ejecuta estos pasos en la reunión y documenta todo en el tester:")
        st.write(leader_name+" es un "+nombre+" y se caracteriza por: "+caracteristicas)
       
        st.write("**1.** Reconócele uno de sus atributos positivos de la lista anterior.")
        recognition = st.text_input("¿Qué atributo positivo reconoces en "+leader_name+"?")
       
        st.write("**2.** Muéstrame en el dashboard cómo va la métrica")
        metric_state = st.text_input("Estado de la métrica")

        st.write("**3.** ¿Cuéntame porqué no se esta cumpliendo la métrica?")
        metric_reason = st.text_input("Razón de la métrica")

        st.write("**4.** ¿Qué vas a hacer para mejorar la métrica?")
        metric_action = st.text_input("Acción para mejorar la métrica")

        st.write("**5.** Muéstrame 3 casos random donde fallamos y entendamos por qué sucedió")
        metric_case = st.text_input("Casos random donde fallamos")

        st.write("**6.** Generemos tareas a partir de los hallazgos")
        metric_task = st.text_input("Tareas a partir de los hallazgos")

        st.write("**7.** Partamos en sub tareas y asignemolas al cronograma y al sprint")
        metric_subtask = st.text_input("Sub tareas y asignemolas al cronograma y al sprint")

        st.write("**8.** Aplica los pasos a seguir con "+leader_name)
        st.write("Hacer: "+hacer)
        pasos_aplicados = st.text_input("Pasos aplicados")

        st.write("**9.** Revisemos el código uno a uno y veamos que podemos mejorar, generemos tareas y asignemolas al cronograma y al sprint")
        coding_task = st.text_input("Tareas a partir de los hallazgos coding")

        st.write("**10.** Partir en sub tareas y asignemolas al cronograma y al sprint")
        coding_subtask = st.text_input("Sub tareas y asignemolas al cronograma y al sprint coding")

        st.write("**11.** Revisemos funciones estadísticas y veamos que podemos mejorar, generemos tareas y asignemolas al cronograma y al sprint")
        statistics_task = st.text_input("Tareas a partir de los hallazgos statistics")

        st.write("**12.** Partir en sub tareas y asignemolas al cronograma y al sprint")
        statistics_subtask = st.text_input("Sub tareas y asignemolas al cronograma y al sprint statistics")

        st.write("**13.** Revisemos el dashboard y veamos que podemos mejorar, generemos tareas y asignemolas al cronograma y al sprint")
        dashboard_task = st.text_input("Tareas a partir de los hallazgos dashboard")

        st.write("**14.** Partir en sub tareas y asignemolas al cronograma y al sprint")
        dashboard_subtask = st.text_input("Sub tareas y asignemolas al cronograma y al sprint dashboard")

        st.write("**15.** Revisemos versionado e industrializacion y veamos que podemos mejorar, generemos tareas y asignemolas al cronograma y al sprint")
        versioning_task = st.text_input("Tareas a partir de los hallazgos industrializacion")

        st.write("**16.** Partir en sub tareas y asignemolas al cronograma y al sprint")
        versioning_subtask = st.text_input("Sub tareas y asignemolas al cronograma y al sprint industrializacion")

        st.write("**17.** Revisemos la documentación y veamos que podemos mejorar, generemos tareas y asignemolas al cronograma y al sprint")
        documentation_task = st.text_input("Tareas a partir de los hallazgos documentation")

        st.write("**18.** Partir en sub tareas y asignemolas al cronograma y al sprint")
        documentation_subtask = st.text_input("Sub tareas y asignemolas al cronograma y al sprint documentation")

        st.write("**19.** Revisemos los costos y veamos que podemos mejorar, generemos tareas y asignemolas al cronograma y al sprint")
        costs_task = st.text_input("Tareas a partir de los hallazgos cloud costs")

        st.write("**20.** Partir en sub tareas y asignemolas al cronograma y al sprint")
        costs_subtask = st.text_input("Sub tareas y asignemolas al cronograma y al sprint cloud costs")

        st.write("**21.** Apliquemos las necesidades de "+leader_name)
        st.write("Necesidades: "+necesidad)
        necesidades_aplicadas = st.text_input("Necesidades aplicadas")

        st.write("**22.** Aplica un tester")
        tester = st.text_input("Tester aplicado")

        st.write("**23.** Respiradas agradeciendo "+leader_name)
        agrecimiento = st.text_input("Agradecimiento")
    
        if st.button("Enviar"):
            output = markdown.markdown("""
            # Reunión con """+leader_name+"""
            - Nombre del proyecto: """+project_name+"""
            - Nombre del líder: """+leader_name+"""
            - Fecha de la reunión: """+str(date.today())+"""
            - Propósito de la reunión: """+purpose+"""
            - Metrica: """+metric+"""

            ## 1. Reconócele uno de sus atributos positivos de la lista anterior.
            """+recognition+"""
            ## 2. Muéstrame en el dashboard cómo va la métrica
            """+metric_state+"""
            ## 3. ¿Cuéntame porqué no se esta cumpliendo la métrica?
            """+metric_reason+"""
            ## 4. ¿Qué vas a hacer para mejorar la métrica?
            """+metric_action+"""
            ## 5. Muéstrame 3 casos random donde fallamos y entendamos por qué sucedió
            """+metric_case+"""
            ## 6. Generemos tareas a partir de los hallazgos
            """+metric_task+"""
            ## 7. Partamos en sub tareas y asignemolas al cronograma y al sprint
            """+metric_subtask+"""
            ## 8. Aplica los pasos a seguir con """+leader_name+"""
            Hacer: """+hacer+"""
            Pasos aplicados: """+pasos_aplicados+"""
            ## 9. Revisemos el código uno a uno y veamos que podemos mejorar, generemos tareas y asignemolas al cronograma y al sprint
            """+coding_task+"""
            ## 10. Partir en sub tareas y asignemolas al cronograma y al sprint
            """+coding_subtask+"""
            ## 11. Revisemos funciones estadísticas y veamos que podemos mejorar, generemos tareas y asignemolas al cronograma y al sprint
            """+statistics_task+"""
            ## 12. Partir en sub tareas y asignemolas al cronograma y al sprint
            """+statistics_subtask+"""
            ## 13. Revisemos el dashboard y veamos que podemos mejorar, generemos tareas y asignemolas al cronograma y al sprint
            """+dashboard_task+"""
            ## 14. Partir en sub tareas y asignemolas al cronograma y al sprint
            """+dashboard_subtask+"""
            ## 15. Revisemos versionado e industrializacion y veamos que podemos mejorar, generemos tareas y asignemolas al cronograma y al sprint
            """+versioning_task+"""
            ## 16. Partir en sub tareas y asignemolas al cronograma y al sprint
            """+versioning_subtask+"""
            ## 17. Revisemos la documentación y veamos que podemos mejorar, generemos tareas y asignemolas al cronograma y al sprint
            """+documentation_task+"""
            ## 18. Partir en sub tareas y asignemolas al cronograma y al sprint
            """+documentation_subtask+"""
            ## 19. Revisemos los costos y veamos que podemos mejorar, generemos tareas y asignemolas al cronograma y al sprint
            """+costs_task+"""
            ## 20. Partir en sub tareas y asignemolas al cronograma y al sprint
            """+costs_subtask+"""
            ## 21. Apliquemos las necesidades de """+leader_name+"""
            Necesidades: """+necesidad+"""
            Necesidades aplicadas: """+necesidades_aplicadas+"""
            """)

            st.download_button(
                label="Descargar",
                data=output,
                file_name="reunion_"+leader_name+".md",
                mime="text/markdown",
            )


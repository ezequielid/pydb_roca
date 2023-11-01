from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    conn = pymysql.connect(host='localhost', user='root', password='', db='oct2223')
    cursor = conn.cursor()

    
    consulta = """
    SELECT round(sum(lista1)/(sum(lista1)+sum(lista2)+sum(lista3)+sum(lista4)+sum(lista5)+sum(blancos)+sum(nulos))*100,2) as jxc,
   round( sum(lista2)/(sum(lista1)+sum(lista2)+sum(lista3)+sum(lista4)+sum(lista5)+sum(blancos)+sum(nulos))*100,2) as hxnp,
   round( sum(lista3)/(sum(lista1)+sum(lista2)+sum(lista3)+sum(lista4)+sum(lista5)+sum(blancos)+sum(nulos))*100,2) as uxp,
   round( sum(lista4)/(sum(lista1)+sum(lista2)+sum(lista3)+sum(lista4)+sum(lista5)+sum(blancos)+sum(nulos))*100,2) as lla,
   round( sum(lista5)/(sum(lista1)+sum(lista2)+sum(lista3)+sum(lista4)+sum(lista5)+sum(blancos)+sum(nulos))*100,2) as fdi,
    round(sum(blancos)/(sum(lista1)+sum(lista2)+sum(lista3)+sum(lista4)+sum(lista5)+sum(blancos)+sum(nulos))*100,2) as bla,
  round(  sum(nulos)/(sum(lista1)+sum(lista2)+sum(lista3)+sum(lista4)+sum(lista5)+sum(blancos)+sum(nulos))*100,2) as nul,
    SUM(lista1) AS jxc1,
    SUM(lista2) AS hxnp1,
    SUM(lista3) AS uxp1,
    SUM(lista4) AS lla1,
    SUM(lista5) AS fdi1,
    SUM(blancos) AS bla1,
    SUM(nulos) AS nul1,
    circuito AS circuito
    FROM oct2223.otcpre group by circuito order by circuito
    """

    cursor.execute(consulta)
    data = cursor.fetchall()

    lista_circuitos = {
        6301: '6301 PASO CORDOBA',
        6302: '6302 MOSCONI, LA RIVERA Y LACOSTA',
        6303: '6303 STEFENELLI',
        6304: '6304 PROGRESO Y MALVINAS',
        6305: '6305 B° SAN CAYETANO',
        6306: '6306 B° UNIVERSITARIO',
        6307: '6307 CENTRO',
        6308: '6308 QUINTU PANAL',
        6309: '6309 B° VILLA OBRERA',
        6310: '6310 BAGLIANI',
        6311: '6311 B° LA BARDA',
        6312: '6312 B° NUEVO',
        6313: '6313 B° BELGRANO',
        6314: '6314 CHACRA MONTE',
        6315: '6315 ROMAGNOLI'
    }
    
    datos_preprocesados = []
    
    for fila in data:
        jxc_percent = fila[0]  
        hxnp_percent = fila[1] 
        uxp_percent = fila[2]
        lla_percent = fila[3]
        fdi_percent = fila[4]
        bla_percent = fila[5]
        nul_percent = fila[6]
        jxc1 = fila[7]
        hxnp1 = fila[8]
        uxp1 = fila[9]
        lla1 = fila[10]
        fdi1 = fila[11]
        bla1 = fila[12]
        nul1 = fila[13]
        datos_preprocesados.append({
            'jxc_percent': jxc_percent,
            'hxnp_percent': hxnp_percent,
            'uxp_percent': uxp_percent,
            'lla_percent': lla_percent,
            'fdi_percent': fdi_percent,
            'bla_percent': bla_percent,
            'nul_percent': nul_percent,
            'jxc1': jxc1,
            'hxnp1': hxnp1,
            'uxp1': uxp1,
            'lla1': lla1,
            'fdi1': fdi1,
            'bla1': bla1,
            'nul1': nul1,
            'circuito': fila[-1]  
        })

    if data:
        app.logger.debug("Datos recuperados con éxito: %s", data)
    else:
        app.logger.error("No se pudieron recuperar los datos")

    return render_template('index.html', data=datos_preprocesados, lista_circuitos=lista_circuitos, consulta_sql=consulta)

if __name__ == '__main__':
    app.run(debug=True)

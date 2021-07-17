import pymysql
class conecxion:
    def __init__(self):
        self.connection=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='invernadero-final'
        )
        self.cursor=self.connection.cursor()
        print("Base de Datos conectada")


    def mostrar(self):
        sql='SELECT estado_cosecha_notificacion.id_estado, estado_cosecha_notificacion.nombre_estado,estado_cosecha.id_estado1 from estado_cosecha_notificacion INNER JOIN estado_cosecha WHERE estado_cosecha_notificacion.id_estado=estado_cosecha.id_estado1 AND estado_cosecha_notificacion.id_estado=2'
        try:
            self.cursor.execute(sql)
            datos=self.cursor.fetchall()
            for dato in datos:
                print(dato[1])
                print("--------------------------------")
        except Exception as e:
            raise



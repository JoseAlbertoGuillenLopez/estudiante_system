from conexionBD import *

class Estudiante:
    def __init__(self,nombre,nota):
        self._nombre=nombre
        self._nota=nota
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,otro):
        self._nombre=otro

    @property
    def nota(self):
        return self._nota
    @nota.setter
    def nota(self,otro):
        self._nota=otro

    def imprimir(self):
        return F"El estudiante: {self.nombre} tiene una nota de: {self.nota}"
    def mostrar(self):
        return self._nota
    


    @staticmethod
    def insertar(nombre,nota):
        try:
            cursor.execute(
                "insert into estudiante values(NULL,%s,%s)",(nombre,nota)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from estudiante"
            )
            return cursor.fetchall()
        except:
            return False
        
    @staticmethod
    def actualizar(nombre,nota,id):
        try:
            cursor.execute(
                "update estudiante set nombre=%s, nota=%s where id=%s",(nombre,nota,id)
            )
            conexion.commit()
            if cursor.rowcount>0:
                return True
            else:
                return False   
        except:
            return False
        
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "delete from estudiante where id=%s",(id,)
            )
            conexion.commit()
            if cursor.rowcount>0:
                return True
            else:
                return False   
        except:
            return False


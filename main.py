from estudiante import estudiante
import os

class APP:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        os.system("cls")

    def esperarTecla(self):
        input("Presione cualquier tecla para continuar...")

    def datosEstudiante(self,tipo):
        print(f"Estudiante tipo {tipo}")
        nombre=input("Nombre: ").strip().upper()
        nota=float(input("Nota: "))
        return nombre,nota
    
    def menu_acciones(self,tipo):
        pass
    def menu_estudiante(self,tipo):
        pass

    def respuesta_sql(self,respuesta):
        if respuesta:
            print("Consulta realizada exitosamente")
        else:
            print("Fallo al realizar la consulta")

    def main(self):
        op=True
        while op:
            self.borrarPantalla()
            opcion=input("\t\t:::Menu estuadiantes:::\n1)Insertar\n2)Consultar\n3)Actualizar\n4)Eliminar\n5)Salir \n\nEliga una opcion: ").strip().lower()
            if opcion=="1" or opcion=="insertar":
                self.borrarPantalla()
                nombre,nota=self.datosEstudiante("primaria")
                obj=estudiante.Estudiante(nombre,nota)
                respuesta=estudiante.Estudiante.insertar(obj.nombre,obj.nota)
                input(f"Nombre:{obj.nombre} Nota: {obj.nota}")
                self.respuesta_sql(respuesta)
                self.esperarTecla()
            elif opcion=="2" or opcion=="consultar":
                self.borrarPantalla()
                respuesta=estudiante.Estudiante.consultar()
                if respuesta:
                    print(f"{'ID':<10}{'NOMBRE':<10}{'NOTA':<10}")
                    for i in respuesta:
                        print(F"{i[0]:<10}{i[1]:<10}{i[2]:<10}")
                    self.esperarTecla()
                else:
                    self.borrarPantalla()
                    input("No hay registros para mostrar")
                
            elif opcion=="3" or opcion=="actualizar":
                self.borrarPantalla()
                id=int(input("ID del estudiante: "))
                nombre,nota=self.datosEstudiante("primaria")
                respuesta=estudiante.Estudiante.actualizar(nombre,nota,id)
                self.respuesta_sql(respuesta)
                self.esperarTecla()
            elif opcion=="4" or opcion=="eliminar":
                self.borrarPantalla()
                id=int(input("ID del estudiante: "))
                respuesta=estudiante.Estudiante.eliminar(id)
                self.respuesta_sql(respuesta)
                self.esperarTecla()
            elif opcion=="5" or opcion=="salir":
                self.borrarPantalla()
                input("Saliendo del sistema")
                op=False
            else:
                self.borrarPantalla()
                print("opcion no valida intente de nuevo")
                self.esperarTecla()

        
    

if __name__=="__main__":
    app=APP()
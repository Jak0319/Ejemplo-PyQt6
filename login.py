import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt6.QtGui import QFont

class VentanaInicioSesion(QWidget):
    
    def __init__(self, ventana_principal):
        super().__init__()
        self.ventana_principal = ventana_principal
        self.inicializarUI()
        
    def inicializarUI(self):
        self.setGeometry(100, 100, 350, 350)
        self.setWindowTitle("Inicio de Sesión")
        
        
        # Establecemos el color de fondo de la ventana-------------------------------------------------------------------
        self.setStyleSheet("background-color: black; color: white;")
        
        # Creamos etiquetas y cuadros de texto para usuario y contraseña-------------------------------------------------
        lbl_usuario = QLabel("Usuario:", self)
        self.txt_usuario = QLineEdit(self)
        lbl_usuario.setFont(QFont("Arial",18))  # Línea para modificar el tamaño y tipo de Font---------------------------
        
        lbl_contraseña = QLabel("Contraseña:", self)
        self.txt_contraseña = QLineEdit(self)
        self.txt_contraseña.setEchoMode(QLineEdit.EchoMode.Password)
        lbl_contraseña.setFont(QFont("Arial",18))  # Línea para modificar el tamaño y tipo de Font---------------------------
        
        # Creamos un botón de inicio de sesión-------------------------------------------------------------------------------
        btn_iniciar_sesion = QPushButton("Iniciar Sesión", self)
        btn_iniciar_sesion.clicked.connect(self.iniciar_sesion)
        btn_iniciar_sesion.setFont(QFont("Arial",18))  # Línea para modificar el tamaño y tipo de Font----------------------
        
        # Aplicamos estilos CSS al botón-------------------------------------------------------------------------------------
        btn_iniciar_sesion.setStyleSheet("background-color: blue; color: white;")
        
        # Creamos un layout vertical para organizar los campos y el botón----------------------------------------------------
        layout = QVBoxLayout()
        layout.addWidget(lbl_usuario)
        layout.addWidget(self.txt_usuario)
        layout.addWidget(lbl_contraseña)
        layout.addWidget(self.txt_contraseña)
        layout.addWidget(btn_iniciar_sesion)
        
        # Establecemos el layout en la ventana----------------------------------------------------------------------------
        self.setLayout(layout)
        
        self.show()
        
    def iniciar_sesion(self):
        # Verificar el usuario y la contraseña-----------------------------------------------------------------------------
        usuario = self.txt_usuario.text()
        contraseña = self.txt_contraseña.text()
        
        # Aquí validamos los datos de inicio de sesión---------------------------------------------------------------------
        
        # Comparamos el usuario y la contraseña con valores fijos----------------------------------------------------------
        if usuario == "jeff" and contraseña == "123":
            
            # Si el inicio de sesión es exitoso, mostramos la ventana principal y cerramos la ventana de inicio de sesión---
            self.ventana_principal.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")

class VentanaPrincipal(QWidget):
    
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        
    def inicializarUI(self):
        self.setGeometry(100, 100, 350, 350)
        self.setWindowTitle("Formulario - Registro")
        
        # Establecemos el color de fondo de la ventana--------------------------------------------------------------------------
        self.setStyleSheet("background-color: black; color: white;")
        
        # Etiquetas y cuadros de texto para nombre, dirección, teléfono y correo------------------------------------------------
        lbl_nombre = QLabel("Nombre:", self)
        self.txt_nombre = QLineEdit(self)
        lbl_nombre.setFont(QFont("Arial",12))  # Línea para modificar el tamaño y tipo de Font----------------------------------
        
        lbl_direccion = QLabel("Dirección:", self)
        self.txt_direccion = QLineEdit(self)
        lbl_direccion.setFont(QFont("Arial",12))  # Línea para modificar el tamaño y tipo de Font--------------------------------
        
        lbl_telefono = QLabel("Teléfono:", self)
        self.txt_telefono = QLineEdit(self)
        lbl_telefono.setFont(QFont("Arial",12))  # Línea para modificar el tamaño y tipo de Font---------------------------------

        lbl_correo = QLabel("Correo:", self)
        self.txt_correo = QLineEdit(self)
        lbl_correo.setFont(QFont("Arial",12))  # Línea para modificar el tamaño y tipo de Font-----------------------------------
        
        #Botón de envío----------------------------------------------------------------------------------------------------------
        self.btn_enviar = QPushButton("Enviar", self)
        self.btn_enviar.setFont(QFont("Arial",12))  # Línea para modificar el tamaño y tipo de Font------------------------------
        
        # Aplicamos estilos CSS al botón----------------------------------------------------------------------------------------
        self.btn_enviar.setStyleSheet("background-color: blue; color: white;")
        
        #Layout vertical para organizar los campos y el botón-------------------------------------------------------------------
        layout = QVBoxLayout()
        layout.addWidget(lbl_nombre)
        layout.addWidget(self.txt_nombre)
        layout.addWidget(lbl_direccion)
        layout.addWidget(self.txt_direccion)
        layout.addWidget(lbl_telefono)
        layout.addWidget(self.txt_telefono)
        layout.addWidget(lbl_correo)
        layout.addWidget(self.txt_correo)
        layout.addWidget(self.btn_enviar)
        
        # Establecemos el layout en la ventana----------------------------------------------------------------------------------
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_inicio_sesion = VentanaInicioSesion(VentanaPrincipal())
    sys.exit(app.exec())

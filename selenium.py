#DOCUMENTAÇÃO SELENIUM http://selenium-python.readthedocs.io/locating-elements.html#locating-elements-by-class-name

from selenium import webdriver

face = webdriver.Chrome()
face.get("SITE QUE TENHA QUE AUTENTICAR")

login = face.find_element_by_id('ID DO CAMPO DE LOGIN') #Pode ser ID, tag_name, class_name, entre outros...
senha = face.find_element_by_id('ID DO CAMPO DE SENHA') #Mesma coisa que o de cima
login.send_keys("USUÁRIO")
senha.send_keys("SENHA")
entrar = face.find_element_by_id("ID DO BOTÃO ENTRAR") #Mesmo que os demais acima
entrar.submit()
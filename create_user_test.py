import sender_stand_request
import data

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


response_health = sender_stand_request.get_health()
print(user_response.status_code)
print(response_health.json())


def positive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    assert users_table_response.text.count(str_user) == 1
    print("assert del '2 letter' automatizado correcto")
def negative_assert_simbol(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"]== "Has introducido un nombre de usuario no válido. " \
                                         "El nombre solo puede contener letras del alfabeto latino, "\
                                         "la longitud debe ser de 2 a 15 caracteres."
def negative_assert_no_fisrtname(user_body):
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

# Prueba 1 Usuario con 2 letras MANUAL
def test_create_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aa")
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1
    print("assert del '2 letter' manual correcto")
print("prueba 1 correcta")
# Prueba 2 usuario 15 letras
def test_create_user_15_letter_in_first_name_get_success_response():
    possitive_assert("Aaaaaaaaaaaaaaa")
print("prueba 2 correcta")
# Prueba 3 usuario 1 letras
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_simbol("A")
print("prueba 3 correcta")
# Prueba 4 usuario 16 letras
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_simbol("Aaaaaaaaaaaaaaaa")
print("prueba 4 correcta")
# Prueba 5 usuario space en letras
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_simbol("A Aaa ")
print("prueba 5 correcta")
# Prueba 6 usuario simbolos en letras
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_asssert_symbol("\"№%@\",")
print("prueba 6 correcta")
# Prueba 7 usuario números tipo string en letras
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_simbol("123")
print("prueba 7 correcta")
# Prueba 8 usuario inexistente
def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_fisrtname(user_body)
print("prueba 8 correcta")
# Prueba 9 usuario vacio
def create_user_empty_first_name_get_error_response():
    user_body = get_user_body("")
    negative_assert_nofirst_name(user_body)
print("prueba 9 correcta")
# Prueba 10 usuario tipo int-numeros
def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body("12")
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
print("prueba 10 correcta")

#PUESTO POR MI
print("no hubo errores aqui :)")

test_create_user_2_letter_in_first_name_get_success_response()
positive_assert('Bb')

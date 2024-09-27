import sender_stand_request
import data

# Función de prueba positiva
def positive_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body= name
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    user_response= sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    assert user_response.json()["name"] == name["name"]

# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert(name):
    # El nombre del kit se guarda en la variable kit_body
    kit_body = name
    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

# Prueba 1. Un Kit Name creado con exito y contiene 1 caracter
def test_1_create_user_1_letter_in_kit_name_get_success_response():
    positive_assert(data.kit_body_1)

# Prueba 2. Un Kit Name creado con exito y contiene 511 caracter
def test_2_create_user_511_letter_in_kit_name_get_success_response():
    positive_assert(data.kit_body_2)

# Prueba 3. Error. Un Kit Name contiene 0 caracter
def test_3_create_user_0_letter_kit_name_get_error_response():
    negative_assert(data.kit_body_3)

# Prueba 4. Error. Un Kit Name contiene 512 caracter
def test_4_create_user_512_letter_kit_name_get_error_response():
    negative_assert(data.kit_body_4)

# Prueba 5. Un Kit Name creado con exito y contiene caracteres especiales
def test_5_create_user_has_special_symbol_in_kit_name_get_success_response():
    positive_assert(data.kit_body_5)

# Prueba 6. Un Kit Name creado con exito y contiene espacios
def test_6_create_user_has_space_in_kit_name_get_success_response():
    positive_assert(data.kit_body_6)

# Prueba 7. Error. El parámetro Kit Name contiene un string de dígitos
def test_7_create_user_has_number_in_first_name_get_error_response():
    positive_assert(data.kit_body_7)

# Prueba 8. Error. El parámetro contiene un string vacío
def test_8_create_user_empty_kit_name_get_error_response():
    negative_assert(data.kit_body_8)

# Prueba 9. Error. El tipo del parámetro Kit Name: número
def test_9_create_user_number_type_kit_name_get_error_response():
    negative_assert(data.kit_body_9)
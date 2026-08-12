from app.modules.usuarios.enums.rol_usuario import RolUsuario
from app.modules.usuarios.models.usuario import Usuario
from app.modules.usuarios.value_objects.password import Password

ADMIN_EMAIL = "admin@test.com"
USUARIO_EMAIL = "usuario@test.com"
PASSWORD = "ClaveSegura123"


def crear_usuario(
    db_session,
    email: str,
    rol: RolUsuario,
    activo: bool = True,
) -> Usuario:

    usuario = Usuario(
        nombre_completo="Usuario de prueba",
        email=email,
        password_hash=Password.hash(PASSWORD),
        rol=rol,
        activo=activo,
    )

    db_session.add(usuario)
    db_session.commit()
    db_session.refresh(usuario)

    return usuario


def login(
    client,
    email: str,
    password: str,
):
    return client.post(
        "/auth/login",
        json={
            "email": email,
            "password": password,
        },
    )


def test_login_exitoso(client, db_session):

    crear_usuario(db_session, ADMIN_EMAIL, RolUsuario.ADMIN)

    response = login(client, ADMIN_EMAIL, PASSWORD)

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["access_token"]
    assert data["usuario"]["email"] == ADMIN_EMAIL
    assert data["usuario"]["rol"] == "ADMIN"


def test_login_password_incorrecta(client, db_session):

    crear_usuario(db_session, ADMIN_EMAIL, RolUsuario.ADMIN)

    response = login(client, ADMIN_EMAIL, "ClaveIncorrecta")

    assert response.status_code == 401
    assert response.json()["success"] is False


def test_login_email_inexistente(client):

    response = login(client, "noexiste@test.com", PASSWORD)

    assert response.status_code == 401


def test_login_usuario_inactivo(client, db_session):

    crear_usuario(
        db_session,
        ADMIN_EMAIL,
        RolUsuario.ADMIN,
        activo=False,
    )

    response = login(client, ADMIN_EMAIL, PASSWORD)

    assert response.status_code == 403


def test_endpoint_protegido_sin_token(client):

    response = client.get("/productos")

    assert response.status_code == 401


def test_endpoint_protegido_con_token_valido(client, db_session):

    crear_usuario(db_session, USUARIO_EMAIL, RolUsuario.USUARIO)

    token = login(client, USUARIO_EMAIL, PASSWORD).json()["data"]["access_token"]

    response = client.get(
        "/productos",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200


def test_token_invalido(client):

    response = client.get(
        "/productos",
        headers={"Authorization": "Bearer token-invalido"},
    )

    assert response.status_code == 401


def test_auth_me(client, db_session):

    crear_usuario(db_session, USUARIO_EMAIL, RolUsuario.USUARIO)

    token = login(client, USUARIO_EMAIL, PASSWORD).json()["data"]["access_token"]

    response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json()["data"]["email"] == USUARIO_EMAIL


def test_endpoint_admin_con_usuario_normal(client, db_session):

    crear_usuario(db_session, USUARIO_EMAIL, RolUsuario.USUARIO)

    token = login(client, USUARIO_EMAIL, PASSWORD).json()["data"]["access_token"]

    response = client.patch(
        "/productos/1/desactivar",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 403


def test_endpoint_admin_con_admin(client, db_session):

    crear_usuario(db_session, ADMIN_EMAIL, RolUsuario.ADMIN)

    token = login(client, ADMIN_EMAIL, PASSWORD).json()["data"]["access_token"]

    response = client.get(
        "/usuarios",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200


def test_crear_usuario_duplicado(client, db_session):

    crear_usuario(db_session, ADMIN_EMAIL, RolUsuario.ADMIN)
    crear_usuario(db_session, USUARIO_EMAIL, RolUsuario.USUARIO)

    token = login(client, ADMIN_EMAIL, PASSWORD).json()["data"]["access_token"]

    response = client.post(
        "/usuarios",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "nombre_completo": "Duplicado",
            "email": USUARIO_EMAIL,
            "password": PASSWORD,
            "rol": "USUARIO",
        },
    )

    assert response.status_code == 409
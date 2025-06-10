"""Basic connection example.
"""

import redis
import atividades
r = redis.Redis(
    host='redis-16566.c278.us-east-1-4.ec2.redns.redis-cloud.com',
    port=16566,
    decode_responses=True,
    username="default",
    password="gKEDcsp2osQrzVI0BkDp3X4iD1yg0l9m",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

def registrar_acesso(recurso: str):
    total = r.incr(f'contador:{recurso}')
    print(f"A página '{recurso}' foi acessada {total} vezes.")
USUARIOS_ONLINE_KEY = "usuarios_online"

def usuario_conectou(user_id: str):
    r.sadd(USUARIOS_ONLINE_KEY, user_id)
    print(f"Usuário {user_id} está agora online.")


def usuario_saiu(user_id: str):
    r.srem(USUARIOS_ONLINE_KEY, user_id)
    print(f"Usuário {user_id} saiu e foi removido do online.")

def listar_usuarios_online():
    online = r.smembers(USUARIOS_ONLINE_KEY)
    print(" Usuários atualmente online:")
    for uid in online:
        print(f" - {uid}")


def adicionar_seguidor(usuario_id: str, seguidor_id: str):
    # seguidor_id começa a seguir usuario_id
    r.sadd(f"seguidores:{usuario_id}", seguidor_id)
    r.sadd(f"seguindo:{seguidor_id}", usuario_id)
    print(f" {seguidor_id} agora segue {usuario_id}")

def remover_seguidor(usuario_id: str, seguidor_id: str):
    r.srem(f"seguidores:{usuario_id}", seguidor_id)
    r.srem(f"seguindo:{seguidor_id}", usuario_id)
    print(f" {seguidor_id} parou de seguir {usuario_id}")

def amigos_em_comum(user1: str, user2: str):
    seguidores_user1 = f"seguidores:{user1}"
    seguidores_user2 = f"seguidores:{user2}"
    comum = r.sinter(seguidores_user1, seguidores_user2)
    print(f" Amigos em comum entre {user1} e {user2}: {comum}")
    return comum

def listar_contatos_unicos(user_id: str):
    seguidores = f"seguidores:{user_id}"
    seguindo = f"seguindo:{user_id}"
    uniao = r.sunion(seguidores, seguindo)
    print(f" Todos contatos únicos de {user_id}: {uniao}")
    return uniao

def quem_nao_tesegue_de_volta(user_id: str):
    seguindo = f"seguindo:{user_id}"
    seguidores = f"seguidores:{user_id}"
    diff = r.sdiff(seguindo, seguidores)
    print(f" Quem {user_id} segue, mas não te segue de volta: {diff}")
    return diff


registrar_acesso("home")

usuario_conectou("user_1")
usuario_conectou("user_2")
listar_usuarios_online()
usuario_saiu("user_1")
listar_usuarios_online()

adicionar_seguidor("alice", "bob")
adicionar_seguidor("alice", "carol")
adicionar_seguidor("dave", "alice")
adicionar_seguidor("bob", "alice")
remover_seguidor("alice", "carol")

amigos_em_comum("alice", "bob")
listar_contatos_unicos("alice")
quem_nao_tesegue_de_volta("alice")

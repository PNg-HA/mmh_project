import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL 

server = Flask(__name__)
jwt_secret = '7b8c6ef87a5d4e3e2b1a0d9c8b7a6f5e'

# config
server.config["MYSQL_HOST"] = 'localhost'
server.config["MYSQL_USER"] = 'auth_user'
server.config["MYSQL_PASSWORD"] = 'Auth123'
server.config["MYSQL_DB"] = 'auth'

mysql = MySQL(server)

@server.route("/register", methods=['POST'])
def register():
    auth = request.authorization
    if not auth:
        return "missing information", 400
    
    #insert into database
    cur = mysql.connection.cursor()
    res = cur.execute(
        "INSERT INTO user (username, password) VALUES (%s, %s)", (auth.username, auth.password,)
    )
    mysql.connection.commit()

    if res > 0:
        return "success for registration", 201
    return "error for registration", 500

@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401

    # check db for username and password
    cur = mysql.connection.cursor()
    res = cur.execute(
        "SELECT * FROM user WHERE username=%s", (auth.username,)
    )

    if res > 0:
        user_row = cur.fetchone()
        id =  user_row[0]
        username = user_row[1]
        password = user_row[2]

        if auth.username != username or auth.password != password:
            return "invalid credentials", 401
        else:
            return createJWT(id, jwt_secret, True)
    else:
        return "invalide credentials", 401


@server.route("/validate", methods=["POST"])
def validate():
    encoded_jwt = request.headers["Authorization"]

    print(encoded_jwt)

    if not encoded_jwt:
        return "missing credentials", 401

    try:
        decoded = jwt.decode(
            encoded_jwt, jwt_secret, algorithms=["HS256"]
        )
    except:
        return "not authorized", 403

    return decoded, 200


def createJWT(id, secret, authz):

    payload =         {
            "id": id,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz,
        }

    return jwt.encode(
        payload,
        secret,
        algorithm="HS256",
    )

context = ('./certificate.crt', './private_key.key')

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000, debug=True)

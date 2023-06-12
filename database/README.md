Command to deploy MYSQL server:
  1. Put the working directory of CMD (CLI, Terminal) in the folder.
  2. Type "docker build ."
  3. Type "docker images" to see the new mysql image ID. For example, that ID is "ef...".
  4. Type "docker run -p <unused-port>:3306 <mysql-image-ID>. For example: docker run -p 3310:3306 ef.

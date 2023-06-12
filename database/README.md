Command to deploy MYSQL server:
  1. Put the working directory of CMD (CLI, Terminal) in the folder.
  2. Type "docker build ."
  3. Type "docker images" to see the new mysql image ID. For example, that ID is "e7...".
  4. Type "docker run -p <unused-port>:3306 <mysql-image-ID>. For example: docker run -p 3310:3306 e7.
  
To access the mysql: Follow the picture belowed:
  ![image](https://github.com/PNg-HA/mmh_project/assets/93396414/7205d52d-2238-46c5-bba9-75aa480b1b40)

This repo contains the source code for XMeme project for the Stage-2B of Crio Winter of Doing Externship program. 
The code for frontend and backend is contained in separate directories with the respective names.
1. The backend is capable of receiving the posted meme inputs from frontend and store in database, as well as fetching the list of memes from backend and sending to the frontend.
2. SQLite database is used locally and postgres for the deployed backend.
3. URL for frontend - https://xmeme-amit-frontend.netlify.app/
	for backend - https://xmeme-amit-backend.herokuapp.com/memes
4. Tech stack used - Python-flask for backend 
		   - React for frontend
5. The endpoint for updating a meme is implemented only at the backend presently. The front-end does not contains any edit button yet.
6. Note that image-url validation is implemented at the backend before meme submission. Other URL's will give a 400 Error Code.
7. Duplicate meme records are not allowed and result in a 409 Error Code if tried out.
8. There is also a dark-mode toggle on the application frontend.
9. The Dockerfile is present in the root directory of the project. Note that it utilizes the boot.sh script too, which contains commands to run the server.
10. The install.sh, server_run.sh and sleep.sh are also present in the root directory with instructions as required. 
11. The scripts as well as the Dockerfile is tested on an EC2 instance with the same configurations as crio's submission module mentioned.
12. The https version of frontend is deployed on netlify. 
13. For the backend, both http and https versions exist and are deployed on heroku.
14. The documentation for the API is implemented using Swagger and is present at https://xmeme-amit-backend.herokuapp.com/swagger-ui/ 
15. Note that the swagger docs are implemented on port 8081 along with the application backend.
16. The complete source code has been deployed on the gitlab repo provided by crio.


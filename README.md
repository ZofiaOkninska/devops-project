# Project description

This is a project with Dockerized simple web page.

## Functionality 

If you run the python app, the web page would be hosted locally at the port 5000.
The web page greets you when you provide your name in the url like:
`localhost:5001/hello/<your name>`

## Building and running the docker image

You can build the image and then run it to see the results in the browser. 
Remember to redirect port outside of the container to be able to do so.

Steps: 

1. Build the image: 
`docker build --file Dockerfile --tag project_web_app:1.0.0 .`
2. Run with port redirection: 
`docker run --rm -it -p <your desired port>:5001 project_web_app:1.0.0`
3. Test url in the browser: 
`localhost:<your desired port>/hello/<your name>`
or via linux tool lynx:
`lynx localhost:<your desired port>/hello/<your name>`
# flaskapp

This is just a toy project to play with Flask and various web components.

## How do I build this thing?

Well, you first require python. Then navigate to src, then
`pip install -r requirements.txt` to install the application's requirements.

## How do I run this thing?

If all all goes well...after `python app.py`, you should be rocking!

## Can we run with Docker? YES!

    docker build -t flaskapp .

    docker run -d -p 5000:5000 flaskapp

    Navigate to http://<docker-machine ip (your env)>:5000

## How do I contribute?

Simply fork this project, make your changes, and submit a pull request!!!

## Licensing

MIT

@ECHO OFF

docker build . -f Dockerfile -t spotify-api:latest
docker image prune -f

@REM Go to `https://developer.spotify.com/dashboard` to get these values for your app 
docker run -p 8888:8888^
 -e SPOTIPY_CLIENT_ID="MY-CLIENT-ID"^
 -e SPOTIPY_CLIENT_SECRET="MY-CLIENT-SECRET"^
 -e SPOTIPY_REDIRECT_URI="http://localhost:8888/callback/"^
 -it --rm spotify-api


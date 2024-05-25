@ECHO OFF

docker build . -f Dockerfile -t ics-cal-viewer:latest
docker run^
 --mount type=bind,source=C:\Users\xhamy\Desktop\xhamyd@gmail.com.ical\,destination=/home/docker-user/python-scripts/ics_files/^
 -it ics-cal-viewer
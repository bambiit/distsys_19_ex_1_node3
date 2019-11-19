FROM python:3.7
ADD node3.py /

EXPOSE 8003
CMD [ "python", "./node3.py" ]
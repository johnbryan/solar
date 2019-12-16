FROM python:3
ADD solar.py /
CMD [ "python", "./solar.py" ]

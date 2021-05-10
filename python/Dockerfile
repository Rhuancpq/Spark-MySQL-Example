FROM openjdk:8-slim
COPY --from=python:3.6 . .

WORKDIR /app

COPY . ./

RUN pip3 install -r requirements.txt

# ENTRYPOINT [ "python3", "script.py" ]

ENTRYPOINT ["tail", "-F", "/dev/null"]
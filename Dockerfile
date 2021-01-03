FROM python:3.6-slim
MAINTAINER sweb@mail.ru
COPY . /tests_for_jenkins
WORKDIR /tests_for_jenkins
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null
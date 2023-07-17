FROM python:3.11-slim
WORKDIR /app
COPY *.p* requirements.txt ./
COPY util/ ./util
COPY pages/ ./pages
RUN pip3 install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=8080", "--server.address=0.0.0.0"]


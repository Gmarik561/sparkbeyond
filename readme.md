The problem 

As an AI-tech company specializing in messaging platforms, we are developing a solution
using Python and Celery. Your task involves processing a set of text documents.



answer 

build the image localy


docker compose up .

if dont want to use docker compose
 docker build -t my_fastapi_app .     
 docker run -d -p 8000:80 my_fastapi_app


to see the result of the most common words in the articles 


http://localhost:8000/common-words/?folder_path=/app/articles&num_articles=4&top_n=10


kubectl apply -f deployment.yaml -f service.yaml -f ingress.yaml






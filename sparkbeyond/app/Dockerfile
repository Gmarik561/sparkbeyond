FROM python:3.8

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the application code
COPY app.py /app/
COPY process_articles.py /app/
COPY articles/. /app/articles
# Set the environment variable for folder_path
ENV FOLDER_PATH /app/articles
# Expose port 80
EXPOSE 80

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

# 1. Use the official lightweight Python image
FROM python:3.9-slim

# 2. Set the folder where our code will live inside the container
WORKDIR /app

# 3. Copy our list of libraries into the container
COPY requirements.txt .

# 4. Install the libraries (Flask, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all our files (app.py, templates folder, etc.) into the container
COPY . .

# 6. Tell the container to start our Python app when it launches
CMD ["python", "app.py"]
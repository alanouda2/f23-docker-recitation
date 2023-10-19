# specifies the Parent Image from which you are building.
FROM python:3.9

# specify the working directory for the image
WORKDIR /code

# TODO

# Copy the requirements file into the container at /code
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . /code/

# Expose the port on which your FastAPI application will run. By default, FastAPI runs on port 8000.
EXPOSE 8000

# Specify the command to run your FastAPI application. You can use uvicorn to run your FastAPI app.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
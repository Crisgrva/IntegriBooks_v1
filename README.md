# Integribooks

Integribooks is an application for managing books. This README provides the necessary instructions to run the application using Docker, execute Python unit tests, and how to import and run the Postman collection.

## Prerequisites

Make sure you have the following programs installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.x](https://www.python.org/downloads/)
- [Postman](https://www.postman.com/downloads/)

## Running the application with Docker Compose

To easily run the application using `docker-compose`, follow these steps:

1. Clone the application repository:

    ```bash
    git clone https://github.com/your_username/integribooks.git
    cd integribooks
    ```

2. Start the services using `docker-compose`:

    ```bash
    docker-compose up --build
    ```

3. Access the application in your browser at [http://localhost](http://localhost).

4. Access the api swagger in your browser at [http://localhost:5001/apidocs](http://localhost:5001/apidocs).

## Running Python Unit Tests

To run the Python unit tests:

1. Enter the container where the application is running (if using Docker Compose):

    ```bash
    docker exec -it flask_api /bin/bash
    ```

2. Once inside the container, run the tests with:

    ```bash
    pytest
    ```

    This will execute all the unit tests defined in the application's test files.

## Importing the Collection to Postman

Follow these steps to import the Postman collection:

1. Open Postman and click **Import** at the top left.
2. Select the `Flask Books API Collection.postman_collection.json` file from the repository.
3. The collection should now appear in your list of Postman collections.

## Running Postman Tests

To run the tests from the imported collection:

1. Select the **Flask Books API Collection** in Postman.
2. Click the **Run** button to open the collection in the Collection Runner.
3. Configure the environment (if necessary) and start the tests by clicking **Start Test**.

This will execute all the tests defined in the Postman collection.

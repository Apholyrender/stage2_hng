
# CRUD Application Documentation

Welcome to the documentation for our CRUD (Create, Read, Update, Delete) application. This documentation provides an overview of the CRUD operations, setup instructions for Windows, Linux, and macOS users, and includes a section on UML diagrams.

Here is a **[link](https://hng-stage-2-95a5.onrender.com/api)** to a live version of this application.

## Setup

 Follow the instructions below to setup the application on your local machine.

### Windows

1. **Install Python:** Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Clone the Repository:** Use `git clone` to clone the application [repository](https://github.com/blacdev/HNG_Stage_Two.git).

3. **Install Dependencies:** Navigate to the project directory and run the following command to install required packages:

            pip install -r requirements.txt

### Linux & macOS

1. **Install Python:** Most Linux distributions and macOS come with Python pre-installed. You can verify by running `python --version`.

2. **Clone the Repository:** Use `git clone` to clone the application [repository](https://github.com/blacdev/HNG_Stage_Two.git).

3. **Install Dependencies:** Navigate to the project directory and run the following command to install required packages:

          pip install -r requirements.txt

## Database Setup

The application uses MongDB as its database. You can download and install MongoDB from [mongodb.com](https://www.mongodb.com/try/download/community).

After installing MongoDB, you add the following environment variables to your system:

    DATABASE_URI: The URI for your MongoDB database.
    DATABASE_NAME: The name of your MongoDB database.
    COLLECTION_NAME: The name of your MongoDB collection.

## Running the Application

After setting up the application, you can run it by running the following command in the project directory:

    python app.py

## Testing

You can run a test uisng postman:

- Go to **[Postman link](https://documenter.getpostman.com/view/16477483/2s9YC31uAS)** and click on import to postman. If you do not have postman installed on your system, fork the collection and run it on postman web

![Alt text](https://camo.githubusercontent.com/aa806d089441f9448c22448dc78f39b2fa5f4226cc34777b51e8619141235c24/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f616d6f73737061726b2f696d6167652f75706c6f61642f76313639343339353230362f436170747572655f6362746a74692e706e67)

- Click on the dropdown of the collection then click on `Run collection`

## API Documentation

Click the **[link](https://github.com/blacdev/HNG_Stage_Two/blob/staging/DOCUMENTATION.md)** to read the api documentation.

## UML Diagrams

We have provided UML diagrams for a visual representation of our application's structure. You can find the UML diagrams in the link below.

**[UML Diagrams](https://drive.google.com/file/d/1OBUdOP8uOIFK4KRb7FYqgTAUAhnLNm6-/view?usp=sharing)**

## E-R Diagram

We have provided an E-R diagram for a visual representation of our application's database structure. You can find the E-R diagram in the link below.

**[E-R Diagram](https://dbdiagram.io/d/64fdd89102bd1c4a5e4a2aa6)**

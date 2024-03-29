# Project Title: Custom Block Starter Package

## Introduction
The Custom Block Components Starter Package is a project designed to facilitate the creation of customized block components for various functionalities such as PdfOcr, Split Pdf, etc. This starter package provides a foundational structure and essential files to make the development of these components easy and efficient. The project structure includes the following components:

### File Structure
```bash
├── README.md
├── client.py
├── deployment
│   ├── Dockerfile
│   └── entrypoint.sh
├── main.py
├── requirements.txt
├── structure.json
├── testdata
│   └── single_pdf.pdf
└── unittests
    └── __init__.py
```

#### `client.py`
client.py serves as a connection checker for the block with the server. It allows users to verify the connectivity of the block.
```bash
####Import the ClientRunner class from the augmatrix.block_service module.
# This class is used to create a client instance that can communicate with a specified server.
from augmatrix.block_service.client_runner import ClientRunner

def main():
    """
    The main function where we initialize the client, prepare inputs and properties,
    and make a function call to the server using the Augmatrix SDK.
    """
    
    # Initialize the client with the server's URL.
    # Replace 'http://0.0.0.0:8082/' with the actual server URL you wish to communicate with.
    client = ClientRunner(url='http://0.0.0.0:8082/')

    # Define the inputs to be sent to the server.
    # These inputs can vary based on the server's expected parameters.
    inputs = {
        "name": "Arya"  # Example input, in this case, a name.
    }

    # Define additional properties or arguments for the function call.
    # These properties can be used to modify the behavior of the called function.
    properties = {
        "message": "Welcome to Augmatrix SDK!"  # Example property to send a welcome message.
    }
    
    # If the server requires authentication, credentials can be provided here.
    # This example uses an empty dictionary as a placeholder.
    credentials = {}

    # Make the function call with the specified structure, inputs, properties, and credentials.
    # 'structure.json' should be the path to a JSON file defining the function call structure.
    # This example assumes 'structure.json' is correctly formatted and located in the same directory.
    outputs = client.call_function(
        structure="structure.json",
        inputs=inputs,
        func_args=properties,
        credentials=credentials
    )

    # Print the outputs returned from the server after the function call.
    print(outputs)

# Checks if the script is being run directly and, if so, calls the main function.
# This is a common Python idiom to make the script executable as a standalone script
# or allow it to be imported without executing the main function automatically.
if __name__ == "__main__":
    main()
```

#### `main.py`
the main.py files acts as server file responsible for the central hub for managing and executing the block components.
"This Python code appears to be defining a class `StarterTask` that inherits from `ServiceRunner`, and then instantiates a `ServerManager` with an instance of `StarterTask` and starts a server. Here's the breakdown of the code along with its documentation:
```bash
import io
from typing import Dict, List, Tuple
from augmatrix.block_service.service_runner import ServerManager, ServiceRunner

class StarterTask(ServiceRunner):
    def __init__(self, logger: object) -> None:
        """
        Initializes the StarterTask object.

        Parameters:
        logger (object): The logger to use for logging messages.
        """
        self.logger = logger
        super().__init__(structure_json_path='./structure.json')

    def run(self, inputs, properties, credentials):
        """
        Runs the StarterTask.

        Parameters:
        inputs (object): Input data for the task.
        properties (Dict): Properties passed to the task.
        credentials (Dict): Credentials passed to the task.

        Returns:
        Dict: A dictionary containing the result of the task.
        """
        message = 'Hi '+inputs.name + f", {properties['message']}"

        return {'message': message}

if __name__ == "__main__":
    ServerManager(StarterTask(logger=None)).start(
        host="0.0.0.0",
        port=8082
    )
```

Documentation:
- `StarterTask` class:
  - `__init__(self, logger: object) -> None`: Initializes the StarterTask object.
    - Parameters:
      - `logger (object)`: The logger to use for logging messages.
  - `run(self, inputs, properties, credentials) -> Dict`: Runs the StarterTask.
    - Parameters:
      - `inputs (object)`: Input data for the task.
      - `properties (Dict)`: Properties passed to the task.
      - `credentials (Dict)`: Credentials passed to the task.
    - Returns:
      - `Dict`: A dictionary containing the result of the task.

- `if __name__ == "__main__":` block:
  - Instantiates a `ServerManager` with an instance of `StarterTask` and starts a server.
  - Parameters:
    - `host (str)`: The hostname or IP address on which the server will listen.
    - `port (int)`: The port on which the server will listen.

This code seems to be a part of a larger system for managing services and servers. The `StarterTask` class appears to be a task that can be run within this system, and it communicates with the outside world via the `run()` method. The `ServerManager` is then used to manage and run this task as a server.


#### `deployment/`
- `Dockerfile`: This Dockerfile includes the basic installations required for the specified block. It provides a standardized environment for running the block in a Docker container.
```bash
FROM ubuntu:latest

# Set the timezone without interaction
ENV DEBIAN_FRONTEND=noninteractive

# Update the package repository and install necessary packages
RUN apt-get update && \
    apt-get install -y \
    python3-dev \
    python3-pip \
    python3-virtualenv \
    curl \
	git \
    screen && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata 
# Set the timezone without interaction
ENV TZ=UTC

# Copy all files local to image to created Directory 
RUN mkdir /app
COPY ./ /app/.
COPY /deployment/entrypoint.sh .

# Install Python packages which is requirement.txt file
RUN pip3 install -r /app/requirments.txt

# Set permissions and convert line endings
RUN chmod +x entrypoint.sh && \
    sed -i -e 's/\r$//' entrypoint.sh

# Set the entrypoint to run 
ENTRYPOINT ["./entrypoint.sh"]

# Default command to make image alive
CMD ["sleep", "infinity"]
```
- `entrypoint.sh`: A script that runs the block process in the background inside the Docker image.

#### `requirements.txt`
This file contains the necessary Python installations required for the project. Additional installations can be added based on the specific needs of the project, and they can be installed using pip or Python.

#### `structure.json`
A JSON file outlining the data format, project structure, and package details. It serves as documentation for developers working on the project.

#### `testdata/`
- `single_pdf.pdf`: Sample test data provided for testing and experimentation with the block components.

#### `unittests/`
This folder contains the test cases for the project. The code must pass these test cases for approval, ensuring the reliability and functionality of the block components.

The provided structure aims to create a cohesive and organized foundation for building customized block components. Developers can extend this framework by adding specific functionalities and dependencies as per the project requirements. The inclusion of test cases emphasizes the importance of code quality and functionality verification.
## Docker Image Building and Pushing to Docker Hub

### Building the Docker Image
To build the Docker image, follow these steps:

1. Navigate to the root of the project where the `Dockerfile` is located.
2. Open a terminal and run the following command:
   ```bash
   docker build -f deployment/Dockerfile -t <your-image-name>:<tag.
   ```
   Replace  `your-image-name`, and `tag` with appropriate values.

### Pushing the Docker Image to Docker Hub
To push the Docker image to Docker Hub, execute the following steps:

1. Log in to your Docker Hub account using the command:
   ```bash
   docker login registry.augmatrix.ai 
   ```
2. Tag you Docker image with respect to the  docker registry 
	```bash 
	docker tag <your-image-name>:<tag registry.augmatrix.ai/<your-image-name>:<tag>>
	```
3. Push the built image using the following command:

   ```bash
   docker push registry.augmatrix.ai/<your-image-name>:<tag>
   ```
   Ensure you replace the placeholders with your actual Docker Hub username, image name, and tag.

Now, your Docker image is available on Docker Hub and can be pulled by others.

## Usage
[Provide instructions on how to use your project, including any configuration settings or environment variables that need to be set.]

## License
[Specify the license under which your project is distributed. For example, MIT License, Apache License, etc.]

## Acknowledgments
[List any external libraries, tools, or resources that you used or were inspired by during the development of this project.]

Feel free to customize the README further based on the specifics of your project.

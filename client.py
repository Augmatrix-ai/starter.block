from augmatrix.block_service.client_runner import ClientRunner

def main():
    # Initialize the client with the server's URL
    client = ClientRunner(url='http://0.0.0.0:8082/')

    inputs = {
        "name": "Arya"
    }

    properties = {
        "message": "Welcome to Augmatrix SDK!"
    }
    
    credentials = {}

    # Call the function with the specified inputs, properties, and credentials
    outputs = client.call_function(
        structure="structure.json",
        inputs=inputs,
        func_args=properties,
        credentials=credentials
    )

    print(outputs)

if __name__ == "__main__":
    main()

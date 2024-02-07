import io
from typing import Dict, List, Tuple
from augmatrix.block_service.service_runner import ServerManager, ServiceRunner

class StarterTask(ServiceRunner):
    def __init__(self, logger: object) -> None:
        """
        Initializes the SplitPDFTask object.

        Parameters:
        logger (object): The logger to use for logging messages.
        """
        self.logger = logger
        super().__init__(structure_json_path='./structure.json')

    def run(self, inputs, properties, credentials):
        message = 'Hi '+inputs.name + f", {properties['message']}"

        return {'message': message}

if __name__ == "__main__":
    ServerManager(StarterTask(logger=None)).start(
        host="0.0.0.0",
        port=8082
    )

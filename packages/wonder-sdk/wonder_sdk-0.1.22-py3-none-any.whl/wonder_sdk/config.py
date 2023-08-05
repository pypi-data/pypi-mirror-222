import os

class EnvironmentTypes:
    """
    A class that defines possible environment types.
    """
    production = 'production'
    staging = 'staging'

class WonderSdkConfig:
    """
    A class used to configure the WonderSDK.

    Attributes
    ----------
    environment_types : EnvironmentTypes
        An instance of the EnvironmentTypes class.
    environment : str
        The application environment, either 'production' or 'staging'.
    project_id : str
        The ID of the project.
    subscription_name : str
        The name of the subscription.
    process_count : int
        The number of processes to run.
    collection_name : str
        The name of the collection. It depends on the environment type.
    """

    def __init__(
            self,
            environment=None,
            project_id=None,
            subscription_name=None,
            process_count=None,
            production_collection_name=None,
            staging_collection_name=None,
        ) -> None:
        """
        Constructs all the necessary attributes for the WonderSdkConfig object.

        Parameters
        ----------
        environment : str, optional
            The application environment, either 'production' or 'staging'.
            Defaults to 'staging' if not provided.
        project_id : str, optional
            The ID of the project. If not provided, will be fetched from
            the environment variable "PROJECT_ID".
        subscription_name : str, optional
            The name of the subscription. If not provided, will be fetched from
            the environment variable "SUBSCRIPTION_NAME".
        process_count : int, optional
            The number of processes to run. Defaults to 1 if not provided.
        production_collection_name : str, optional
            The name of the production collection. If not provided, will be fetched from
            the environment variable "COLLECTION_NAME".
        staging_collection_name : str, optional
            The name of the staging collection. If not provided, will be fetched from
            the environment variable "COLLECTION_NAME".
        """

        self.environment_types = EnvironmentTypes()

        self.environment = environment if environment else os.environ.get('ENVIRONMENT', self.environment_types.staging)

        self.project_id = project_id if project_id else os.environ.get('PROJECT_ID', default=None)

        self.subscription_name = subscription_name if subscription_name else os.environ.get('SUBSCRIPTION_NAME', default=None)

        self.process_count = process_count if process_count else int(os.environ.get('PROCESS_COUNT', default=1))

        if self.environment == self.environment_types.production:
            self.collection_name = production_collection_name if production_collection_name else os.environ.get('COLLECTION_NAME', default=None)
        elif self.environment == self.environment_types.staging:
            self.collection_name = staging_collection_name if staging_collection_name else os.environ.get('COLLECTION_NAME', default=None)
import googleapiclient.discovery

def initialize_google_api_client():
    # Here, define the API name and version
    # and any other parameters needed to initialize the client
    api_name = 'gmail'
    api_version = 'v1'
    # Initialize and return the Google API client
    return googleapiclient.discovery.build(api_name, api_version)
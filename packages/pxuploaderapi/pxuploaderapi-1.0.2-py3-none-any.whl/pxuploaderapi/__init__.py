import pickle

class EcommerceUploaderAPI():
    def __init__(self, path):
        self.path = path
        # Get the uploader object from the path
        with open(self.path, "rb") as f:
            self.uploader_dict = pickle.load(f)

    def getName(self) -> str:
        return self.getUploader()["name"]
    
    def getUUID(self) -> str:
        return self.getUploader()["uuid"]
    
    def getFields(self) -> dict:
        return self.getUploader()["fields"]

    def getUploader(self) -> dict:
        return self.uploader_dict
    
    def getTestOptions(self) -> dict:
        return self.getUploader()["test_options"]
    
    def getDeployOptions(self) -> dict:
        return self.getUploader()["deploy_options"]
    
    def getGithubOptions(self) -> dict:
        return self.getUploader()["github_options"]


        
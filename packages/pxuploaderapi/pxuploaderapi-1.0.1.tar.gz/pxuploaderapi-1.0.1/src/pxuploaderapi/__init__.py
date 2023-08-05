import pickle

class Uploader:
    """
    Each Uploader object represents a separate inventory uploader.

    This class stores the metadata and configurations for the inventory uploader.
    Test Options are used to determine how the uploader will run in testing mode.
    Deploy Options are used to determine how the uploader will be deployed.
    Github Options are used to push and pull from the Github repositories.
    """

    class TestOptions:
        """
        Stores the options for running the uploader in testing mode.
        """
        def __init__(self, exe_path, headless:bool, send_email:bool, testing_flag:bool, show_console:bool):
            self.exe_path = exe_path
            self.headless = headless
            self.send_email = send_email
            self.testing_flag = testing_flag
            self.show_console = show_console

        def toDict(self):
            """Returns a dictionary representation of the test options."""
            return {
                "exe_path": self.exe_path,
                "headless": self.headless,
                "send_email": self.send_email,
                "testing_flag": self.testing_flag,
                "show_console": self.show_console
            }

    class DeployOptions:
        """
        Stores the options for deploying the uploader.
        """
        def __init__(self, icon_file:str, py_file:str, exe_name:str, exe_paths:set, console_based:bool):
            self.icon_file = icon_file
            self.py_file = py_file
            self.exe_name = exe_name
            self.exe_paths = exe_paths
            self.console_based = console_based

        def toDict(self):
            """Returns a dictionary representation of the deploy options."""
            return {
                "icon_file": self.icon_file,
                "py_file": self.py_file,
                "exe_name": self.exe_name,
                "exe_paths": self.exe_paths,
                "console_based": self.console_based
            }

    class GithubOptions:
        """
        Stores the options for pushing and pulling from the Github repository.
        """
        def __init__(self, repo_url:str, local_path:str, branch:str):
            self.repo_url = repo_url
            self.local_path = local_path
            self.branch = branch

        def toDict(self):
            """Returns a dictionary representation of the Github options."""
            return {
                "repo_url": self.repo_url,
                "local_path": self.local_path,
                "branch": self.branch
            }

    def __init__(self, name, uuid):
        self.name = name
        self.uuid = uuid
        self.fields = {}
        self.custom_actions = {}  # A mapping of the name of the action to the executable path.
        self.test_options = self.TestOptions("", True, True, True, True)
        self.deploy_options = self.DeployOptions("", "", "", set(), False)
        self.github_options = self.GithubOptions("", "", "")
        self.process_reference = None
        self.running = False

    def toDict(self):
        """Returns a dictionary representation of the uploader."""
        return {
            "name": self.name,
            "uuid": self.uuid,
            "fields": self.fields,
            "custom_actions": self.custom_actions,
            "test_options": self.test_options.toDict(),
            "deploy_options": self.deploy_options.toDict(),
            "github_options": self.github_options.toDict()
        }

    def setName(self, name):
        """Sets the name of the uploader."""
        self.name = name

class EcommerceUploaderAPI():
    def __init__(self, path):
        self.path = path
        # Get the uploader object from the path
        with open(self.path, "rb") as f:
            self.uploader = pickle.load(f)

    def getUploader(self) -> Uploader:
        return self.uploader
    
    def getTestOptions(self) -> dict:
        return self.getUploader().test_options.toDict()
    
    def getDeployOptions(self) -> dict:
        return self.getUploader().deploy_options.toDict()
    
    def getGithubOptions(self) -> dict:
        return self.getUploader().github_options.toDict()

        
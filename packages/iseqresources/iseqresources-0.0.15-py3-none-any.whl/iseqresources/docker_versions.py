from utils import utils
from packaging import version

class DockerVersions():
    def __init__(self, docker_versions_path: str, tools_path: str, gitlab_token: str) -> None:
        self.docker_versions_path = docker_versions_path
        self.tools_path = tools_path
        self.gitlab_token = gitlab_token


    def _cut_first_v_if_exists(self, ver: str) -> str:
        return ver[1:] if ver.startswith('v') else ver

    
    def _generate_docker_versions(self, tools_list: list) -> dict:
        """Convert tools to name: version pairs"""
        docker_versions_dict = {}
        
        for tool in tools_list:
            if tool.get('newest_version'):
                ver = tool.get('newest_version').split(" (")[0]
                ver = self._cut_first_v_if_exists(ver)
                name = tool['name'].upper() + "_VER"

                docker_versions_dict[name] = f"{ver}"
            else:
                ver = tool.get('current_version', '')
                ver = self._cut_first_v_if_exists(ver)
                name = tool['name'].upper() + "_VER"

                docker_versions_dict[name] = f"{ver}"

        return docker_versions_dict


    def update_docker_versions(self) -> None:
        """Verify gitlab token, convert tools to name: version pairs and save it as .json"""
        if not self.gitlab_token and self.tools_path.startswith("https://"):
            self.gitlab_token = utils.get_gitlab_token()

        tools_list = utils.load_json(self.tools_path, self.gitlab_token)
        docker_versions_dict = self._generate_docker_versions(tools_list)
        utils.save_json(self.docker_versions_path, docker_versions_dict)

import yaml
from .tools import get_project_path,sep
class GetConf:
    def __init__(self):
        with open(get_project_path()+sep(["config","environment.yaml"],add_sep_before=True), 'r', encoding='utf-8') as env_file:
            self.env = yaml.load(env_file, Loader=yaml.SafeLoader)

    def get_username_password(self,user):
        return self.env["user"][user]["username"],self.env["user"][user]["password"]
    def get_url(self):
        return self.env["url"]

# if __name__ == '__main__':
#     print(GetConf().get_username_password("william"))

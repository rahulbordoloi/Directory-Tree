import os
from typing import List
import platform


class DirectoryPathTree:
    def __init__(self) -> None:
        self.tree_map_dir = dict()
        # self.tree_map_files = dict()

    def do_dfs(self, source, level):
        print("├─" + "──"*level*3 + "├─" + "{}".format(source))
        # print("──"*level*5 + f"{self.tree_map_files[source]}")
        for node in self.tree_map_dir[source]:
            self.do_dfs(node, level+1)

    def display_tree_directory(self, dir_path : str = os.getcwd(), exclude : List = [".git", ".idea", ".vscode"]):
        try:
            exclude = set(exclude)
            DELEMETER = '\\' if platform.system().lower() == 'windows' else '/'
            source = dir_path.split(DELEMETER)[-1]
            for root,dirs,files in os.walk(dir_path, topdown=True): 
                dirs[:] = [include for include in dirs if include not in exclude]
                self.tree_map_dir[root.split(DELEMETER)[-1]] = dirs
                # self.tree_map_files[root.split(DELEMETER)[-1]] = files

            self.do_dfs(source=source, level=0)
        except Exception as msg:
            print(f"Exception Occurred! Failed to Generate Tree:: {msg}")





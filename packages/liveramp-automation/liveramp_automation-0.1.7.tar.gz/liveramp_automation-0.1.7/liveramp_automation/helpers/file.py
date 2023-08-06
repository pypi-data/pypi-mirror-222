import configparser
import json
import os

import yaml
from liveramp_automation.utils.log import Logger


class FileHelper:

    @staticmethod
    def read_json_report(path) -> dict:
        with open(path, 'r') as file:
            # Read all the content of the json file
            json_string = file.read()
            data = json.loads(json_string)
        return data

    @staticmethod
    def read_init_file(file_path, file_name, file_mode="r") -> dict:
        try:
            full_path = os.path.join(file_path, file_name)
            with open(full_path, mode=file_mode) as file:
                data_dict = {}
                current_module = None
                for line in file:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if line.startswith("[") and line.endswith("]"):
                        current_module = line[1:-1].strip()
                        data_dict[current_module] = {}
                    else:
                        if "=" in line:
                            key, value = line.split("=", 1)
                            key = key.strip()
                            value = value.strip()
                            if current_module:
                                data_dict[current_module][key] = value
            return data_dict
        except FileNotFoundError:
            Logger.error(f"File '{file_name}' not found in the specified path: '{file_path}'.")
            return None
        except PermissionError:
            Logger.error(f"Permission denied to read the file '{file_name}' in the specified path: '{file_path}'.")
            return None
        except Exception as e:
            Logger.error(f"An error occurred while reading the file: {e}")
            return None

    @staticmethod
    def load_env_yaml(path,file_prefix, env):
        # This method is to read the resources accroding to different envrionments
        file_name = path+"/"+file_prefix+".{env}.yaml".format(env)
        with open(file_name) as f:
            return yaml.safe_load(f)

    @staticmethod
    def deal_testcase_json(file_path):
        with open(file_path, "r") as file:
            item = json.load(file)
        nodeid = item["nodeid"]
        outcome = item["outcome"]
        groupName = nodeid.split("/")[1]
        testcase = {}
        testcase["groupName"] = groupName
        testcase["className"] = nodeid.split("/")[2].split("::")[0]
        testcase["caseName"] = nodeid.split("/")[-1].split("::")[-1]
        if outcome.upper() == "failed".upper():
            flag = 0
            errorMessage = str(item["call"]["crash"])
        else:
            flag = 1
            errorMessage = None
        testcase["flag"] = flag
        testcase["errorMessage"] = errorMessage
        testcase["duration"] = float(item["call"]["duration"])
        return testcase

    @staticmethod
    def read_junit_xml_report(path):
        import xml.etree.ElementTree as ET
        tree = ET.parse(path)
        # Get the root element of the XML tree
        root = tree.getroot()
        # Get the values of the errors, failures, skipped, and tests attributes from the testsuite element
        testsuite = root.find('testsuite')
        errors = int(testsuite.get('errors'))
        failures = int(testsuite.get('failures'))
        skipped = int(testsuite.get('skipped'))
        tests = int(testsuite.get('tests'))
        if errors == 0 and failures == 0 and tests > 0:
            Logger.info("All test cases run sucessfully")
        elif errors == 0 and failures != 0 and tests > 0:
            Logger.info("Some test cases run failed")
        elif errors != 0:
            Logger.info("Some scripts have issues and please check")

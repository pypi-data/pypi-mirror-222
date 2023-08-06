def dq_searching_rules(category_rule=None, table_name=None, rule_id=None, static_id=None, sequence="001"):
    from spark_generated_rules_tools.utils import BASE_DIR
    import os
    import json
    import ast
    import sys

    is_windows = sys.platform.startswith('win')
    json_resource_rules = os.path.join(BASE_DIR, "utils", "resource", "rules.json")

    if is_windows:
        json_resource_rules = json_resource_rules.replace("\\", "/")

    with open(json_resource_rules) as f:
        default_rules = json.load(f)
    rules_config = default_rules.get("rules_config", None)
    hamu_dict = dict()
    id_key_dict = dict()
    rs_dict = dict()
    for k, v in rules_config.items():
        for key_name, value_name in v.items():
            rules_version = value_name[0].get("rules_version")
            rules_class = str(value_name[0].get("rules_class"))
            rules_columns = value_name[0].get("rules_columns")
            rules_description = value_name[0].get("rules_name")
            if rules_version == rule_id:
                for rule_name, rule_dtype in rules_columns[0].items():
                    if rule_dtype[1] == "True":
                        id_key_dict[rule_name] = "Mandatory"
                    if rule_dtype[0] == "Boolean" and rule_dtype[2] == "True":
                        rules_value = True
                    elif rule_dtype[0] == "Boolean" and rule_dtype[2] == "False":
                        rules_value = False
                    elif rule_dtype[0] == "Double" and rule_dtype[2] == "100":
                        rules_value = ast.literal_eval(rule_dtype[2])
                    elif rule_dtype[0] == "String" and rule_dtype[2] in ("None", ""):
                        rules_value = ""
                    elif rule_dtype[0] == "Array[String]" and rule_dtype[2] in ("None", ""):
                        rules_value = ["default"]
                    elif rule_dtype[0] == "Dict" and rule_dtype[2] in ("None", ""):
                        rules_value = dict()
                    else:
                        rules_value = rule_dtype[2]
                    rs_dict[rule_name] = rules_value
                if static_id:
                    rs_dict["id"] = static_id
                else:
                    rule_id = str(rule_id).replace("-1", "").replace("-2", "").strip()
                    rs_dict["id"] = f"PE_{category_rule}_{table_name}_{rule_id}_{sequence}"
                hamu_dict["class"] = rules_class
                hamu_dict["config"] = rs_dict
    return hamu_dict, id_key_dict


def dq_generated_dataframe_info(namespace=None,
                                table_name=None,
                                periodicity=None,
                                target_path_name=None,
                                hamu_list=None,
                                hamu_type=None):
    import sys
    import os
    import json
    from pyhocon import ConfigFactory
    from pyhocon import HOCONConverter
    from spark_generated_rules_tools import get_color, get_color_b
    is_windows = sys.platform.startswith('win')
    dir_hocons_mvp_name = os.getenv('pj_dq_dir_mvp_name')
    dir_hocons_mvp_filename = ""
    table_dict = dict()
    table_list = list()
    if table_name not in table_dict.keys():
        physical_target_name = str(str(target_path_name).split("/")[-1])
        uuaa_tag = "".join(table_name.split("_")[2:])
        physical_target_name_extension = str(physical_target_name.split(".")[-1])
        table_dict[table_name] = dict(hammurabi=dict())
        table_dict[table_name]["hammurabi"]["dataFrameInfo"] = dict()
        table_dict[table_name]["hammurabi"]["dataFrameInfo"]["cutoffDate"] = "${?REPROCESS_DATE}"
        table_dict[table_name]["hammurabi"]["dataFrameInfo"]["frequencyRuleExecution"] = periodicity
        table_dict[table_name]["hammurabi"]["dataFrameInfo"]["physicalTargetName"] = f"{physical_target_name}"
        table_dict[table_name]["hammurabi"]["dataFrameInfo"]["targetPathName"] = f"{target_path_name}"
        table_dict[table_name]["hammurabi"]["dataFrameInfo"]["uuaa"] = namespace

        if hamu_type == "staging":
            dir_hocons_mvp_filename = os.path.join(dir_hocons_mvp_name, f"{table_name}", "staging.conf")
            table_dict[table_name]["hammurabi"]["dataFrameInfo"]["subset"] = "cutoff_date='${?DATE}'"
            table_dict[table_name]["hammurabi"]["Input"] = dict()

            table_dict[table_name]["hammurabi"]["Input"]["options"] = dict(delimiter="|", castMode="notPermissive", charset="UTF-8")
            table_dict[table_name]["hammurabi"]["Input"]["paths"] = [f"{target_path_name}"]
            table_dict[table_name]["hammurabi"]["Input"]["schema"] = dict(path="${ARTIFACTORY_UNIQUE_CACHE}/artifactory/${SCHEMAS_REPOSITORY}"
                                                                               f"/schemas/pe/{namespace}"
                                                                               f"/raw/{uuaa_tag}/latest/{uuaa_tag}.input.schema")
            if physical_target_name_extension == "csv":
                table_dict[table_name]["hammurabi"]["Input"]["type"] = "csv"
            if physical_target_name_extension == "dat":
                table_dict[table_name]["hammurabi"]["Input"]["type"] = "fixed"

        if hamu_type == "raw":
            dir_hocons_mvp_filename = os.path.join(dir_hocons_mvp_name, f"{table_name}", "raw.conf")
            table_dict[table_name]["hammurabi"]["dataFrameInfo"]["subset"] = "cutoff_date='${?DATE}'"
            table_dict[table_name]["hammurabi"]["Input"] = dict()
            table_dict[table_name]["hammurabi"]["Input"]["applyConversions"] = False
            table_dict[table_name]["hammurabi"]["Input"]["paths"] = [f"{target_path_name}"]
            table_dict[table_name]["hammurabi"]["Input"]["schema"] = dict(path="${ARTIFACTORY_UNIQUE_CACHE}/artifactory/${SCHEMAS_REPOSITORY}"
                                                                               f"/schemas/pe/{namespace}"
                                                                               f"/raw/{uuaa_tag}/latest/{uuaa_tag}.output.schema")
            table_dict[table_name]["hammurabi"]["Input"]["type"] = "avro"

        if hamu_type == "master":
            dir_hocons_mvp_filename = os.path.join(dir_hocons_mvp_name, f"{table_name}", "master.conf")
            table_dict[table_name]["hammurabi"]["dataFrameInfo"]["subset"] = "cutoff_date='${?REPROCESS_DATE}'"
            table_dict[table_name]["hammurabi"]["Input"] = dict()
            table_dict[table_name]["hammurabi"]["Input"]["paths"] = [f"{target_path_name}"]
            table_dict[table_name]["hammurabi"]["Input"]["schema"] = dict(path="${ARTIFACTORY_UNIQUE_CACHE}/artifactory/${SCHEMAS_REPOSITORY}"
                                                                               f"/schemas/pe/{namespace}"
                                                                               f"/master/{uuaa_tag}/latest/{uuaa_tag}.output.schema")

            table_dict[table_name]["hammurabi"]["Input"]["options"] = dict()
            table_dict[table_name]["hammurabi"]["Input"]["options"]["overrideSchema"] = True
            table_dict[table_name]["hammurabi"]["Input"]["options"]["includeMetadataAndDeleted"] = True
            table_dict[table_name]["hammurabi"]["Input"]["type"] = "parquet"
        table_dict[table_name]["hammurabi"]["rules"] = list()
    table_dict[table_name]["hammurabi"]["rules"] = hamu_list
    table_list.append(table_name)

    if is_windows:
        dir_hocons_mvp_filename = dir_hocons_mvp_filename.replace("\\", "/")
    os.makedirs(os.path.dirname(dir_hocons_mvp_filename), exist_ok=True)
    txt_string = table_dict[table_name]
    json_file2 = json.dumps(txt_string, indent=4)
    conf2 = ConfigFactory.parse_string(json_file2)
    hocons_file2 = HOCONConverter.convert(conf2, "hocon")
    with open(dir_hocons_mvp_filename, "w") as f:
        f.write(hocons_file2)
    with open(dir_hocons_mvp_filename) as f:
        txt_conf = f.read()
    txt_conf = txt_conf.replace('"${?REPROCESS_DATE}"', "${?REPROCESS_DATE}")
    txt_conf = txt_conf.replace("${?DATE}", '"${?DATE}"')
    txt_conf = txt_conf.replace("${?YEAR_MONTH}", '"${?YEAR_MONTH}"')
    txt_conf = txt_conf.replace("${?PERIOD}", '"${?PERIOD}"')
    txt_conf = txt_conf.replace("/artifactory/", '"/artifactory/"')
    txt_conf = txt_conf.replace('"${ARTIFACTORY_UNIQUE_CACHE}', "${ARTIFACTORY_UNIQUE_CACHE}")
    txt_conf = txt_conf.replace('"${SCHEMAS_REPOSITORY}', '"${SCHEMAS_REPOSITORY}"')
    with open(dir_hocons_mvp_filename, "w") as f:
        f.write(txt_conf)
    print(f"{get_color('HOCON CREATE:')} {get_color_b(dir_hocons_mvp_filename)}")


def dq_convert_url_bitbucket_artifactory(url_conf=None):
    url = url_conf
    url_conf_name = str(str(url).split("/")[-3])
    url_conf_name = f"{url_conf_name}"
    url_conf_zone = str(str(url).split("/")[-2])
    uuaa_name = str(str(url).split("/")[-4])
    url_conf = f"http://artifactory-gdt.central-02.nextgen.igrupobbva/" \
               f"artifactory/gl-datio-generic-local/" \
               f"kirby/" \
               f"pe/" \
               f"{uuaa_name.lower()}/" \
               f"{url_conf_zone.lower()}/" \
               f"{url_conf_name.lower()}/" \
               f"0.1.0/" \
               f"{url_conf_name.lower()}.conf"
    return url_conf


def dq_creating_directory_sandbox(path=None):
    from spark_generated_rules_tools import get_color, get_color_b
    import os

    if path in ("", None):
        raise Exception(f'required variable path')
    if not os.path.exists(f'{path}'):
        os.makedirs(f'{path}')
        print(f"{get_color('Directory Created:')} {get_color_b(path)}")
    else:
        print(f"{get_color('Directory Exists:')} {get_color_b(path)}")


def dq_path_workspace(user_sandbox=None):
    import os
    import sys

    if user_sandbox is None:
        user_sandbox = os.getenv('JPY_USER')
        print(f"user_sandbox = {user_sandbox}")
        if user_sandbox in ("", None):
            raise Exception(f'required variable user_sandbox')
    is_windows = sys.platform.startswith('win')
    pj_dir_workspace = ""

    pj_dq_dir_name = "data_quality_rules"
    pj_dq_dir_name = os.path.join(pj_dir_workspace, pj_dq_dir_name)
    pj_dq_dir_confs_name = os.path.join(pj_dir_workspace, pj_dq_dir_name, "data_confs")
    pj_dq_dir_hocons_name = os.path.join(pj_dir_workspace, pj_dq_dir_name, "data_hocons")
    pj_dq_dir_mvp_name = os.path.join(pj_dir_workspace, pj_dq_dir_name, "data_mvp")
    pj_dq_dir_schema_name = os.path.join(pj_dir_workspace, pj_dq_dir_name, "data_schema")

    if is_windows:
        pj_dq_dir_name = pj_dq_dir_name.replace("\\", "/")
        pj_dq_dir_confs_name = pj_dq_dir_confs_name.replace("\\", "/")
        pj_dq_dir_hocons_name = pj_dq_dir_hocons_name.replace("\\", "/")
        pj_dq_dir_mvp_name = pj_dq_dir_mvp_name.replace("\\", "/")
        pj_dq_dir_schema_name = pj_dq_dir_schema_name.replace("\\", "/")

    dq_creating_directory_sandbox(path=pj_dq_dir_name)
    dq_creating_directory_sandbox(path=pj_dq_dir_confs_name)
    dq_creating_directory_sandbox(path=pj_dq_dir_hocons_name)
    dq_creating_directory_sandbox(path=pj_dq_dir_mvp_name)
    dq_creating_directory_sandbox(path=pj_dq_dir_schema_name)
    os.environ['pj_dq_dir_name'] = pj_dq_dir_name
    os.environ['pj_dq_dir_confs_name'] = pj_dq_dir_confs_name
    os.environ['pj_dq_dir_hocons_name'] = pj_dq_dir_hocons_name
    os.environ['pj_dq_dir_mvp_name'] = pj_dq_dir_mvp_name
    os.environ['pj_dq_dir_schema_name'] = pj_dq_dir_schema_name
    os.environ['pj_dir_workspace'] = pj_dir_workspace


def dq_get_rules_list():
    import os
    import json
    import sys
    from prettytable import PrettyTable
    from spark_generated_rules_tools.utils.color import get_color_b
    from spark_generated_rules_tools.utils import BASE_DIR

    is_windows = sys.platform.startswith('win')
    json_resource_rules = os.path.join(BASE_DIR, "utils", "resource", "rules.json")

    if is_windows:
        json_resource_rules = json_resource_rules.replace("\\", "/")

    with open(json_resource_rules) as f:
        default_rules = json.load(f)
    rules_config = default_rules.get("rules_config", None)

    t = PrettyTable()
    t.field_names = [get_color_b("DQ NAME"), get_color_b("VERSION")]
    for k, v in rules_config.items():
        for key_name, value_name in v.items():
            t.add_row([key_name, value_name[0].get("rules_version")])
    print(t)


def dq_generated_rules(rule_id=None,
                       table_name=None,
                       category_rule="MVP"):
    import os
    import sys
    import json
    from pyhocon import ConfigFactory
    from pyhocon.converter import HOCONConverter
    from spark_generated_rules_tools.utils.color import get_color_b, get_color
    from prettytable import PrettyTable

    is_windows = sys.platform.startswith('win')
    dir_hocons_name = os.getenv('pj_dq_dir_hocons_name')
    uuaa_name = str(table_name.split("_")[1]).upper()
    dir_hocons_filename = os.path.join(dir_hocons_name, uuaa_name, f"{table_name}_{rule_id}_generated.conf")

    if is_windows:
        dir_hocons_filename = dir_hocons_filename.replace("\\", "/")
    os.makedirs(os.path.dirname(dir_hocons_filename), exist_ok=True)

    rs_list = list()
    hamu_dict, id_key_dict = dq_searching_rules(category_rule=category_rule, table_name=table_name,
                                                rule_id=rule_id, static_id=None, sequence="001")
    rs_list.append(hamu_dict)
    json_file2 = json.dumps(rs_list, indent=4)
    conf2 = ConfigFactory.parse_string(json_file2)
    hocons_file2 = HOCONConverter.convert(conf2, "hocon")
    with open(dir_hocons_filename, "w") as f:
        f.write(hocons_file2)

    print(f"{get_color(f'========CREATE RULE============')} ")
    with open(dir_hocons_filename) as f:
        res = f.read()
    print(f"{get_color_b(f'{res}')}")

    print(f"{get_color(f'========MANDATORY============')} ")
    t = PrettyTable()
    t.field_names = [get_color_b("DQ NAME"), get_color_b("TYPE")]
    for key_name, value_name in id_key_dict.items():
        t.add_row([key_name, value_name])
    print(t)


def dq_generated_mvp(table_name=None,
                     periodicity="Daily",
                     target_staging_path=None,
                     is_uuaa_tag=True):
    import os
    import requests
    import json
    from spark_generated_rules_tools.utils.utilitty import extract_only_column_text
    from spark_generated_rules_tools.utils.utilitty import extract_only_parenthesis

    dir_schema_name = os.getenv('pj_dq_dir_schema_name')
    uuaa_name = str(table_name.split("_")[1]).lower()
    uuaa_tag = "".join(table_name.split("_")[2:])
    table_name_extract = "_".join(table_name.split("_")[2:])
    physical_target_name_extension = str(target_staging_path.split(".")[-1])
    uuaa_tag_table = table_name
    if is_uuaa_tag:
        uuaa_tag_table = uuaa_tag

    url_raw = "http://artifactory-gdt.central-02.nextgen.igrupobbva/" \
              "artifactory/gl-datio-da-generic-local/" \
              f"schemas/pe/{uuaa_name}/raw/" \
              f"{uuaa_tag_table}/latest/" \
              f"{uuaa_tag_table}.input.schema"
    url_master = "http://artifactory-gdt.central-02.nextgen.igrupobbva/" \
                 "artifactory/gl-datio-da-generic-local/" \
                 f"schemas/pe/{uuaa_name}/master/" \
                 f"{uuaa_tag_table}/latest/" \
                 f"{uuaa_tag_table}.output.schema"
    url_raw_filename = str(url_raw.split("/")[-1])
    dir_raw_schema_filename = os.path.join(dir_schema_name, f"{table_name}", f"{url_raw_filename}")
    url_master_filename = str(url_master.split("/")[-1])
    dir_master_schema_filename = os.path.join(dir_schema_name, f"{table_name}", f"{url_master_filename}")
    os.makedirs(os.path.dirname(dir_raw_schema_filename), exist_ok=True)
    os.makedirs(os.path.dirname(dir_master_schema_filename), exist_ok=True)

    path = requests.get(url_raw)
    with open(dir_raw_schema_filename, 'wb') as f:
        f.write(path.content)

    path = requests.get(url_master)
    with open(dir_master_schema_filename, 'wb') as f:
        f.write(path.content)

    with open(dir_raw_schema_filename) as f:
        artifactory_json = json.load(f)

    table_name = artifactory_json.get("name")
    namespace = artifactory_json.get("namespace")
    table_name_path = artifactory_json.get("physicalPath")

    key_columns_list = list()
    for row in artifactory_json["fields"]:
        _naming = str(row['name']).lower().strip()
        _type = row['type']
        _logical_format = row['logicalFormat']
        _format_dtype = str(extract_only_column_text(_logical_format)).upper()
        _format_value = str(extract_only_parenthesis(_logical_format)).upper()
        key_columns_dict = dict()
        if isinstance(_type, str) and _naming not in ("cutoff_date", "gf_cutoff_date", "audtiminsert_date"):
            key_columns_dict[_naming] = [_format_dtype, _format_value]
            key_columns_list.append(key_columns_dict)

    rule_ids_staging = ["2.1", "3.1", "3.2", "4.2"]
    rule_ids_ctl = ["2.4"]
    rule_ids_raw = ["2.2-1"]
    rule_ids_master = ["2.3-1"]
    category_rule = "MVP"

    hamu_staging_list = list()
    hamu_raw_list = list()
    hamu_master_list = list()
    sequence = 0
    index2 = 0
    for i, field_name in enumerate(key_columns_list):
        field_name_str = str(list(field_name.keys())[0])
        field_value = int(list(field_name.values())[0][1])
        format_regex = f"^[0-9a-bA-Z]{{1,{field_value}}}$"

        for index, rule_id in enumerate(rule_ids_staging):
            sequence += 1
            index2 = str(sequence).zfill(3)
            hamu_dict, id_key_dict = dq_searching_rules(category_rule=category_rule, table_name=table_name,
                                                        rule_id=rule_id, sequence=index2)
            if 'columns' in hamu_dict["config"].keys():
                hamu_dict["config"]["columns"] = [field_name_str]
            if 'column' in hamu_dict["config"].keys():
                hamu_dict["config"]["columns"] = field_name_str
            if 'format' in hamu_dict["config"].keys():
                hamu_dict["config"]["format"] = format_regex
            if 'drillDown' in hamu_dict["config"].keys():
                del hamu_dict["config"]['drillDown']
            if 'subset' in hamu_dict["config"].keys():
                del hamu_dict["config"]['subset']
            if 'balanceIds' in hamu_dict["config"].keys():
                del hamu_dict["config"]['balanceIds']
            if 'withRefusals' in hamu_dict["config"].keys():
                hamu_dict["config"]['withRefusals'] = True
            hamu_staging_list.append(hamu_dict)
        sequence = int(index2)

    if physical_target_name_extension == "dat":
        sequence = 0
        for index, rule_id in enumerate(rule_ids_ctl):
            sequence += 1
            index2 = str(sequence).zfill(3)
            hamu_dict, id_key_dict = dq_searching_rules(category_rule=category_rule, table_name=table_name,
                                                        rule_id=rule_id, sequence=index2)
            hamu_dict["config"]["dataValues"] = dict(metadataType="", position="", length="", path="")
            if 'drillDown' in hamu_dict["config"].keys():
                del hamu_dict["config"]['drillDown']
            if 'subset' in hamu_dict["config"].keys():
                del hamu_dict["config"]['subset']
            if 'balanceIds' in hamu_dict["config"].keys():
                del hamu_dict["config"]['balanceIds']

            hamu_dict["config"]["dataValues"]["metadataType"] = "ctl"
            hamu_dict["config"]["dataValues"]["position"] = 59
            hamu_dict["config"]["dataValues"]["length"] = 9
            hamu_dict["config"]["dataValues"]["path"] = target_staging_path.replace(".dat", ".ctl")
            hamu_staging_list.append(hamu_dict)

    sequence = 0
    for index, rule_id in enumerate(rule_ids_raw):
        sequence += 1
        index2 = str(sequence).zfill(3)
        hamu_dict, id_key_dict = dq_searching_rules(category_rule=category_rule, table_name=table_name,
                                                    rule_id=rule_id, sequence=index2)
        hamu_dict["config"]["dataValues"] = dict(options=dict(), paths="", schema=dict(), type="")
        if 'drillDown' in hamu_dict["config"].keys():
            del hamu_dict["config"]['drillDown']
        if 'subset' in hamu_dict["config"].keys():
            del hamu_dict["config"]['subset']
        if 'balanceIds' in hamu_dict["config"].keys():
            del hamu_dict["config"]['balanceIds']
        if 'withRefusals' in hamu_dict["config"].keys():
            hamu_dict["config"]['withRefusals'] = False
        if 'isCritical' in hamu_dict["config"].keys():
            hamu_dict["config"]['isCritical'] = True
        hamu_dict["config"]["dataValues"]["options"]["delimiter"] = "|"
        hamu_dict["config"]["dataValues"]["options"]["castMode"] = "notPermissive"
        hamu_dict["config"]["dataValues"]["options"]["charset"] = "UTF-8"
        hamu_dict["config"]["dataValues"]["paths"] = [target_staging_path]
        hamu_dict["config"]["dataValues"]["schema"]["path"] = "${ARTIFACTORY_UNIQUE_CACHE}/artifactory/${SCHEMAS_REPOSITORY}" \
                                                              f"/schemas/pe/{uuaa_name}" \
                                                              f"/raw/{uuaa_tag_table}/latest/{uuaa_tag_table}.input.schema"
        if physical_target_name_extension == "dat":
            hamu_dict["config"]["dataValues"]["type"] = "fixed"
        if physical_target_name_extension == "csv":
            hamu_dict["config"]["dataValues"]["type"] = "csv"
        hamu_raw_list.append(hamu_dict)

    sequence = 0
    for index, rule_id in enumerate(rule_ids_master):
        sequence += 1
        index2 = str(sequence).zfill(3)
        hamu_dict, id_key_dict = dq_searching_rules(category_rule=category_rule, table_name=table_name, rule_id=rule_id, sequence=index2)
        hamu_dict["config"]["dataValues"] = dict(applyConversions="", paths="", schema=dict(), type="")
        if 'drillDown' in hamu_dict["config"].keys():
            del hamu_dict["config"]['drillDown']
        if 'subset' in hamu_dict["config"].keys():
            del hamu_dict["config"]['subset']
        if 'balanceIds' in hamu_dict["config"].keys():
            del hamu_dict["config"]['balanceIds']
        if 'withRefusals' in hamu_dict["config"].keys():
            hamu_dict["config"]['withRefusals'] = True
        hamu_dict["config"]["dataValues"]["applyConversions"] = False
        hamu_dict["config"]["dataValues"]["paths"] = [table_name_path]
        hamu_dict["config"]["dataValues"]["schema"]["path"] = "${ARTIFACTORY_UNIQUE_CACHE}/artifactory/${SCHEMAS_REPOSITORY}" \
                                                              f"/schemas/pe/{uuaa_name}" \
                                                              f"/raw/{uuaa_tag_table}/latest/{uuaa_tag_table}.output.schema"
        hamu_dict["config"]["dataValues"]["type"] = "avro"
        hamu_dict["config"]["condition"] = "1=1"
        hamu_master_list.append(hamu_dict)

    for hamu_type in ("staging", "raw", "master"):
        if hamu_type == "staging":
            target_path_name = target_staging_path
            dq_generated_dataframe_info(namespace=namespace,
                                        table_name=table_name,
                                        periodicity=periodicity,
                                        target_path_name=target_path_name,
                                        hamu_list=hamu_staging_list,
                                        hamu_type=hamu_type)

        if hamu_type == "raw":
            target_path_name = table_name_path
            dq_generated_dataframe_info(namespace=namespace,
                                        table_name=table_name,
                                        periodicity=periodicity,
                                        target_path_name=target_path_name,
                                        hamu_list=hamu_raw_list,
                                        hamu_type=hamu_type)

        if hamu_type == "master":
            target_path_name = f"/data/master/{namespace}/data/t_{namespace}_{table_name_extract}"
            dq_generated_dataframe_info(namespace=namespace,
                                        table_name=table_name,
                                        periodicity=periodicity,
                                        target_path_name=target_path_name,
                                        hamu_list=hamu_master_list,
                                        hamu_type=hamu_type)

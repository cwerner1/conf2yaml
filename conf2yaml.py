#!/usr/bin/env python3

from os import walk, makedirs, listdir
from os.path import isfile, join, splitext, exists
import re, yaml, sys, pprint

from uciparse import uci

# Explicitly specify entry point for clarity's sake
import uciparse


def main():
    # Permit limited configuration via command-line args
    debug = False  # Debug YAML to console defaults to off: enable with --debug
    root_path = 'configurations/'  # Root dir is 'configurations': modify with --root="mydir"
    if (len(sys.argv) > 1):
        for arg in sys.argv:
            if arg == '--debug':
                debug = True
            if arg[:6] == '--root':
                head, sep, directory_value = arg.partition('=')
                if directory_value != '':
                    root_path = directory_value.replace('"', '') + '/'

    subdirs = [x[1] for x in walk(root_path)]  # obtain all subdirectories
    subdirs.append('.')  # add root directory

    # Parse all files in all subdirectories
    for subdir, dirs, files in walk(root_path):
        for filename in files:
            if filename != '.gitignore':  # Do not parse .gitignores
                # input = CiscoConfParse(subdir + '/' + filename)             # Get our CiscoConfParse-formatted input

                try:
                    input = uci.UciFile.from_file(subdir + '/' + filename)

                    output_yaml = convert_to_yaml(input, filename)  # Parse input config into output YAML
                except:
                    print("An exception occurred" )
                    print("skipping " + subdir + '/' + filename)
                    continue


                output_path = 'yaml/' + subdir + '/'
                print('Outputting ' + output_path + splitext(filename)[0] + '.yaml YAML')
                write_output_yaml_to_file(output_yaml, output_path, filename)  # Write our YAML to disk
                if (debug):  # If debug mode specified output YAML to console
                    print(output_path + splitext(filename)[0] + '.yaml YAML Output:')
                    print(output_yaml)


# The workhorse function that reads the Cisco config and returns our output config object
def convert_to_yaml(input_config, last_package=""):
    output_config = {}  # Create master dict for output data

    last_config = ""
    # last_package=""
    if last_package != "":
        if last_package not in output_config:
            output_config[last_package] = {}
    last_option = ""
    last_list = ""
    last_config_obj = {}
    last_list_obj = []

    for line in input_config.lines:
        type_of_line = type(line)
        if str(type_of_line) == "<class 'uciparse.uci.UciPackageLine'>":
            last_package = line.name
            if last_package not in output_config:
                output_config[last_package] = {}

            if last_list_obj != []:
                last_config_obj[last_list] = last_list_obj
                last_list_obj = []

            if last_config_obj != {}:
                output_config[last_package][last_config].append(last_config_obj)
                last_config_obj = {}
        #  output_config[last_package]["package"] = line.normalized()

        elif str(type_of_line) == "<class 'uciparse.uci.UciConfigLine'>":
            ##flush old entrys
            ## append last object

            if last_list_obj != []:
                last_config_obj[last_list] = last_list_obj
                last_list_obj = []

            if last_config_obj != {}:
                output_config[last_package][last_config].append(last_config_obj)
                last_config_obj = {}

            last_config = line.section
            if last_config not in output_config[last_package]:
                output_config[last_package][last_config] = []

            if line.name != None:
                last_config_obj[line.section] = line.name
            # output_config[last_package][last_config].append(line.name)

        elif str(type_of_line) == "<class 'uciparse.uci.UciOptionLine'>":
            last_option = line.name
            # if last_option not in output_config[last_package][last_config]:
            #    output_config[last_package][last_config][last_option] = []
            if last_list_obj != []:
                last_config_obj[last_list] = last_list_obj
                last_list_obj = []

            last_config_obj[line.name] = line.value

        elif str(type_of_line) == "<class 'uciparse.uci.UciListLine'>":

            last_list = line.name
            # if last_list not in output_config[last_package][last_config]:
            # last_list_obj = []
            # name_field = _serialize_identifier(_INDENT + "list ", self.name)
            # value_field = _serialize_value(" ", self.value)
            # comment_field = _serialize_comment("  ", self.comment)
            if last_list not in last_config_obj:
                last_config_obj[last_list] = []

            last_config_obj[last_list].append(line.value)
        else:
            print(type_of_line)
            exit(6)

        ####

    ### add the last entrys

    if last_list_obj != []:
        last_config_obj[last_list] = last_list_obj
        last_list_obj = []

    if last_config_obj != {}:
        output_config[last_package][last_config].append(last_config_obj)
        last_config_obj = {}

    # DemoConfig
    # output_config[last_package]["aa"]= [{"aa1":"bb","cc":"ddd"},{"aa2":"bb","cc":"ddd"}]

    # return "".join([line.normalized() for line in self.lines]).splitlines(keepends=True)

    # Alle zeilen von oben durchgehen und yml aufbauen.
    # beginnent mit Packages
    # dann config weiße
    # darin option und lists durchgehen

    return yaml.dump(output_config, sort_keys=False, default_flow_style=0, explicit_start=1)


def write_output_yaml_to_file(output_yaml, output_path, filename):
    # Make sure the directory we're trying to write to exists. Create it if it doesn't
    if not exists(output_path):
        makedirs(output_path)

    # Write foo.yml to the subdir in yaml/root_path that corresponds to where we got the input file
    with open(output_path + splitext(filename)[0] + '.yaml', 'w') as outfile:
        outfile.write(output_yaml)


if __name__ == '__main__':
    main()

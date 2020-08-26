# This script parses the XML file, converts to JSON format.
# Search for the specific eventID via CLI.
# Author : Dung Ho


import argparse
import json
import re
from xml.etree import ElementTree


def remove_namespace(string):
    """
    This function removes the namespace from a string

    :param string: A string used to remove.

    :return a string
    """
    return re.sub(r"\s*{.*}\s*", "", string)


def xml_parser(xml_file):
    """
    This function parses the XML file and return the results as JSON format.

    :param xml_file: the XML file used to parse.

    :return the list of events in JSON format.
    """

    # Get the root of the xml file
    root = ElementTree.parse(xml_file).getroot()

    # Initialize empty list to store childs
    list_of_events = list()

    for event in list(root):
        # Initialize empty dictionary to hold child's attributions
        dict_of_event = dict()

        # Get event's attributes
        for child in event:
            child_tag = remove_namespace(child.tag)
            if child_tag == "System":
                system = dict()
                for element in child:
                    element_tag = remove_namespace(element.tag)
                    if element_tag == "Provider":
                        system["Provider"] = element.attrib

                    if element_tag == "EventID":
                        system["EventID"] = element.text

                    if element_tag == "Level":
                        system["Level"] = element.text

                    if element_tag == "Task":
                        system["Task"] = element.text

                    if element_tag == "Opcode":
                        system["Opcode"] = element.text

                    if element_tag == "TimeCreated":
                        system["TimeCreated"] = element.attrib

                    if element_tag == "EventRecordID":
                        system["EventRecordID"] = element.text

                    if element_tag == "Execution":
                        system["Execution"] = element.attrib

                    if element_tag == "Channel":
                        system["Channel"] = element.text

                    if element_tag == "Computer":
                        system["Computer"] = element.text

                    if element_tag == "Security":
                        system["Security"] = element.attrib

                dict_of_event["System"] = system

            if child_tag == "EventData":
                event_data = dict()
                for element in child:
                    element_tag = remove_namespace(element.tag)
                    if element_tag == "Data":
                        if element.attrib["Name"] == "RuleName":
                            event_data["RuleName"] = element.text

                        if element.attrib["Name"] == "EventType":
                            event_data["EventType"] = element.text

                        if element.attrib["Name"] == "UtcTime":
                            event_data["UtcTime"] = element.text

                        if element.attrib["Name"] == "Operation":
                            event_data["Operation"] = element.text

                        if element.attrib["Name"] == "ProcessGuid":
                            event_data["ProcessGuid"] = element.text

                        if element.attrib["Name"] == "ProcessId":
                            event_data["ProcessId"] = element.text

                        if element.attrib["Name"] == "Image":
                            event_data["Image"] = element.text

                        if element.attrib["Name"] == "TargetFilename":
                            event_data["TargetFilename"] = element.text

                        if element.attrib["Name"] == "CreationUtcTime":
                            event_data["CreationUtcTime"] = element.text

                        if element.attrib["Name"] == "Hash":
                            event_data["Hash"] = element.text

                        if element.attrib["Name"] == "User":
                            event_data["User"] = element.text

                        if element.attrib["Name"] == "Name":
                            event_data["Name"] = element.text

                        if element.attrib["Name"] == "Type":
                            event_data["Type"] = element.text

                        if element.attrib["Name"] == "Destination":
                            event_data["Destination"] = element.text

                        if element.attrib["Name"] == "Protocol":
                            event_data["Protocol"] = element.text

                        if element.attrib["Name"] == "Initiated":
                            event_data["Initiated"] = element.text

                        if element.attrib["Name"] == "SourceIsIpv6":
                            event_data["SourceIsIpv6"] = element.text

                        if element.attrib["Name"] == "SourceIp":
                            event_data["SourceIp"] = element.text

                        if element.attrib["Name"] == "SourceHostname":
                            event_data["SourceHostname"] = element.text

                        if element.attrib["Name"] == "SourcePort":
                            event_data["SourcePort"] = element.text

                        if element.attrib["Name"] == "SourcePortName":
                            event_data["SourcePortName"] = element.text

                        if element.attrib["Name"] == "DestinationIsIpv6":
                            event_data["DestinationIsIpv6"] = element.text

                        if element.attrib["Name"] == "DestinationIp":
                            event_data["DestinationIp"] = element.text

                        if element.attrib["Name"] == "DestinationHostname":
                            event_data["DestinationHostname"] = element.text

                        if element.attrib["Name"] == "DestinationPort":
                            event_data["DestinationPort"] = element.text

                        if element.attrib["Name"] == "DestinationPortName":
                            event_data["DestinationPortName"] = element.text

                        if element.attrib["Name"] == "ImageLoaded":
                            event_data["ImageLoaded"] = element.text

                        if element.attrib["Name"] == "FileVersion":
                            event_data["FileVersion"] = element.text

                        if element.attrib["Name"] == "Description":
                            event_data["Description"] = element.text

                        if element.attrib["Name"] == "Product":
                            event_data["Product"] = element.text

                        if element.attrib["Name"] == "Company":
                            event_data["Company"] = element.text

                        if element.attrib["Name"] == "OriginalFileName":
                            event_data["OriginalFileName"] = element.text

                        if element.attrib["Name"] == "CommandLine":
                            event_data["CommandLine"] = element.text

                        if element.attrib["Name"] == "CurrentDirectory":
                            event_data["CurrentDirectory"] = element.text

                        if element.attrib["Name"] == "User":
                            event_data["User"] = element.text

                        if element.attrib["Name"] == "LogonGuid":
                            event_data["LogonGuid"] = element.text

                        if element.attrib["Name"] == "LogonGuid":
                            event_data["LogonGuid"] = element.text

                        if element.attrib["Name"] == "LogonId":
                            event_data["LogonId"] = element.text

                        if element.attrib["Name"] == "TerminalSessionId":
                            event_data["TerminalSessionId"] = element.text

                        if element.attrib["Name"] == "IntegrityLevel":
                            event_data["IntegrityLevel"] = element.text

                        if element.attrib["Name"] == "Hashes":
                            event_data["Hashes"] = element.text

                        if element.attrib["Name"] == "ParentProcessGuid":
                            event_data["ParentProcessGuid"] = element.text

                        if element.attrib["Name"] == "ParentProcessId":
                            event_data["ParentProcessId"] = element.text

                        if element.attrib["Name"] == "ParentImage":
                            event_data["ParentImage"] = element.text

                        if element.attrib["Name"] == "ParentCommandLine":
                            event_data["ParentCommandLine"] = element.text

                        if element.attrib["Name"] == "Signed":
                            event_data["Signed"] = element.text

                        if element.attrib["Name"] == "Signature":
                            event_data["Signature"] = element.text

                        if element.attrib["Name"] == "SignatureStatus":
                            event_data["SignatureStatus"] = element.text

                    dict_of_event["EventData"] = event_data

        list_of_events.append(dict_of_event)

    return list_of_events


def check_event_id(events, event_id):
    """
    This function checks if the EventID found from the XML file or not.

    :param events: The list of all events from the XML file.
    :param event_id: The EventID use to check from the XML file.

    :return a list of events that found from the XML file.
    """

    if event_id == "all":

        return events

    else:
        list_events_found = [
                event for event in events if (
                    event["System"]["EventID"] == event_id
                )
            ]

        return list_events_found


def main():
    parser = argparse.ArgumentParser(
        description="""
        This tool uses for detecting supicious events that found on
        the Windows Event Log file.
        How to use:
            python3 detections.py <Path of XML file> <--EventID 123 (all)>.
        """
    )

    parser.add_argument(
        "xml",
        type=str,
        help="The path of Windows Event Log XML file. E.g. C:/logs.xml"
    )

    parser.add_argument(
        "--EventID", type=str,
        help="""
        Input the specific EventID or 'all' for displaying all the events.
        """
    )

    # Arguments
    args = parser.parse_args()
    xml_file = args.xml
    event_id = args.EventID

    # Parse the XML file
    events = xml_parser(xml_file)

    events_found = check_event_id(events, event_id)

    if events_found:
        print('-' * 150)
        print(f"Searching for event: {event_id}")
        print(f"Total events found: {len(events_found)}")
        print('-' * 150)
        print(json.dumps(events_found, indent=4))

    else:
        print({"error": f"EventID {event_id} not found!"})


if __name__ == "__main__":
    main()

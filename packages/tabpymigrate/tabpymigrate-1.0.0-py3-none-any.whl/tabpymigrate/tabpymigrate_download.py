"""
TabPyMigrate Download Script

This script helps in downloading tagged objects 
(flows, datasources, and workbooks) from Tableau Server
based on a given tag name. The downloaded objects are stored in the specified file system path.

Requirements:
- Python 3.x
- tableauserverclient library (install using 'pip install tableauserverclient')

"""

import csv
import os
import tableauserverclient as TSC


# Function to get Tableau Server and Authentication
def gettableauauth(server_address, username=None, password=None,
                   site_id=None, is_personal_access_token=False):
    """
    Create Tableau Server and authentication objects.

    Args:
        server_url (str): The URL of the Tableau Server.
        username (str): Tableau Server username. Not required if using Personal Access Token.
        password (str): Tableau Server password. Not required if using Personal Access Token.
        tag_name (str): The tag name to filter objects during download.
        site_id (str): ID of the Tableau site. Not required if using Personal Access Token.
        is_personal_access_token (bool): Flag indicating whether Personal Access Token is being used.

    Returns:
        Tuple[TSC.Server, TSC.Auth]: The Tableau Server and authentication objects.
    """
    server = TSC.Server(server_address, use_server_version=True, http_options={'verify': False})

    if is_personal_access_token:
        tableau_auth = TSC.PersonalAccessTokenAuth(username, password, site_id)
    else:
        tableau_auth = TSC.TableauAuth(username, password, site_id)

    return server, tableau_auth


# Common Parameters and function for download
def write_download_csv(csv_filename):
    """
    Create and return a CSV writer for downloading data.

    Args:
        csv_filename (str): The filename of the CSV to be created.

    Returns:
        csv.DictWriter: A CSV writer object.
    """
    fieldnames = ['Sno', 'Type', 'ProjectName', 'Name', 'Path', 'Show_Tabs', 'Views', 'Response', 'Details']
    csvfile = open(csv_filename, 'w', newline='', encoding='UTF-8')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    return writer


# Download flows by tagname
def download_flows(server, filesystem_path, tag_name, response_details=list):
    """
    Download flows from Tableau Server based on a given tag name.

    Args:
        server (TSC.Server): Authenticated Tableau Server object.
        filesystem_path (str): The path to the file system where the flows will be downloaded.
        tag_name (str): The tag name to filter flows for download.
        response_details (list, optional): A list to store details of the download response.

    Returns:
        list: A list containing details of the download response.
    """
    flows_path = os.path.join(filesystem_path, 'flow')
    csvwriter = write_download_csv(os.path.join(filesystem_path, 'flows.csv'))

    count = 0
    for flow in TSC.Pager(server.flows):
        if tag_name in flow.tags:
            if flow.project_name is None:
                response = "Error"
                details = f"Could not retrieve project name for Flow '{flow.name}'. Skipping download."
                filepath = ''
            else:
                # Create the download path if it doesn't exist
                download_path = os.path.join(flows_path, flow.project_name)
                os.makedirs(download_path, exist_ok=True)

                # Download the flow
                try:
                    filepath = server.flows.download(flow.id, filepath=download_path)
                    response = "Success"
                    details = f"Flow '{flow.name}' downloaded successfully in '{filepath}'!"
                except Exception as error:
                    response = "Error"
                    details = f"Error in download: {error}"

            count += 1
            flow_details = {'Sno': count,
                            'Type': 'Flow',
                            'Name': flow.name,
                            'ProjectName': flow.project_name,
                            'Path': filepath,
                            'Response': response,
                            'Details': details}
            csvwriter.writerow(flow_details)
            response_details.append(flow_details)
    return response_details


# Download datasource by tagname
def download_datasources(server, filesystem_path, tag_name, response_details=list):
    """
    Download datasources from Tableau Server based on a given tag name.

    Args:
        server (TSC.Server): Authenticated Tableau Server object.
        filesystem_path (str): The path to the file system where the flows will be downloaded.
        tag_name (str): The tag name to filter flows for download.
        response_details (list, optional): A list to store details of the download response.

    Returns:
        list: A list containing details of the download response.
    """
    datasources_path = os.path.join(filesystem_path, 'datasource')
    csvwriter = write_download_csv(os.path.join(filesystem_path, 'datasources.csv'))

    count = 0
    for datasource in TSC.Pager(server.datasources):
        if tag_name in datasource.tags:
            if datasource.project_name is None:
                response = "Error"
                details = f"Could not retrieve project name for Datasource '{datasource.name}'. Skipping download."
                filepath = ''
            else:
                # Create the download path if it doesn't exist
                download_path = os.path.join(datasources_path, datasource.project_name)
                os.makedirs(download_path, exist_ok=True)

                # Download the Datasource
                try:
                    filepath = server.datasources.download(datasource.id, filepath=download_path)
                    response = "Success"
                    details = f"Datasource '{datasource.name}' downloaded successfully in '{filepath}'!"
                except Exception as error:
                    response = "Error"
                    details = f"Error in download: {error}"

            count += 1
            datasource_details = {'Sno': count,
                                  'Type': 'Datasource',
                                  'Name': datasource.name,
                                  'ProjectName': datasource.project_name,
                                  'Path': filepath,
                                  'Response': response,
                                  'Details': details}
            csvwriter.writerow(datasource_details)
            response_details.append(datasource_details)
    return response_details


# Download workbook by tagname
def download_workbooks(server, filesystem_path, tag_name, response_details=list):
    """
    Download workbooks from Tableau Server based on a given tag name.

    Args:
        server (TSC.Server): Authenticated Tableau Server object.
        filesystem_path (str): The path to the file system where the flows will be downloaded.
        tag_name (str): The tag name to filter flows for download.
        response_details (list, optional): A list to store details of the download response.

    Returns:
        list: A list containing details of the download response.
    """
    workbooks_path = os.path.join(filesystem_path, 'workbook')
    csvwriter = write_download_csv(os.path.join(filesystem_path, 'workbooks.csv'))

    count = 0
    for workbook in TSC.Pager(server.workbooks):
        if tag_name in workbook.tags:
            if workbook.project_name is None:
                response = "Error"
                details = f"Could not retrieve project name for Workbook '{workbook.name}'. Skipping download."
                filepath = ''
            else:
                # Create the download path if it doesn't exist
                download_path = os.path.join(workbooks_path, workbook.project_name)
                os.makedirs(download_path, exist_ok=True)

                # Download the workbook
                try:
                    filepath = server.workbooks.download(workbook.id, filepath=download_path)
                    response = "Success"
                    details = f"Workbook '{workbook.name}' downloaded successfully in '{filepath}'!"
                except Exception as error:
                    response = "Error"
                    details = f"Error in download: {error}"

            server.workbooks.populate_views(workbook)
            view_list = [view.name for view in workbook.views]
            count += 1
            workbook_details = {'Sno': count,
                                'Type': 'Workbook',
                                'Name': workbook.name,
                                'ProjectName': workbook.project_name,
                                'Show_Tabs': workbook.show_tabs,
                                'Views': view_list,
                                'Path': filepath,
                                'Response': response,
                                'Details': details}
            csvwriter.writerow(workbook_details)
            response_details.append(workbook_details)
    return response_details


def tabpymigrate_download(server_address='', username=None, password=None, 
                          filesystem_path=None, tag_name=None, 
                          site_id=None, 
                          is_personal_access_token=False):
    """
    Main function to execute download for tagged objects from Tableau Server.

    Args:
        server_address (str): The URL of the Tableau Server.
        username (str): Tableau Server username. Not required if using Personal Access Token.
        password (str): Tableau Server password. Not required if using Personal Access Token.
        filesystem_path (str): The path to the file system where the objects will be downloaded.
        tag_name (str): The tag name to filter objects during download.
        site_id (str): ID of the Tableau site. Not required if using Personal Access Token.
        is_personal_access_token (bool): Flag indicating Personal Access Token is being used.

    Returns:
        Tuple[str, list]: str status ('Success' or 'Error') and a list with detailed response.
    """
    response_details = []
    try:
        # Create server and tableau_auth object
        server, tableau_auth = gettableauauth(server_address,
                                              username=username,
                                              password=password,
                                              site_id=site_id,
                                              is_personal_access_token=is_personal_access_token
                                              )

        # Authenticate to Tableau Server
        with server.auth.sign_in(tableau_auth):
            print(f"Starting download for tag_name: {tag_name}")
            # download objects from server to the filesystem for given tag_name
            response_details = download_flows(server, filesystem_path, tag_name, response_details)
            response_details = download_datasources(server, filesystem_path, tag_name, response_details)
            response_details = download_workbooks(server, filesystem_path, tag_name, response_details)
        return "Success", response_details

    except Exception as error:
        response_details = f"Error in TabPyMigrate Export Execution: {str(error)}"
        print(response_details)
        return "Error", response_details

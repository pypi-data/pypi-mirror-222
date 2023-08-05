import time
import configparser
from datetime import timedelta, date, datetime
from wfsx.apivalidation import *
from wfsx.plite import *
from wfsx.common import *
import random, json
import re

mypath = Path.cwd()  # .parent
config = configparser.ConfigParser()
config.read(mypath / "config.ini")
config.read(mypath / 'utils' / 'endpointapi.ini')


def pattern(extnurl, exValue):
    global rpurl
    pattern = r'\{[^{}]+\}'
    matching_variables = re.findall(pattern, extnurl)
    xid = []
    for variable in matching_variables:
        xid.append(variable)
    keys, values = xid, exValue
    replacements = dict(zip(keys, values))
    for pattern, replacement in replacements.items():
        rpurl = extnurl.replace(str(pattern), str(replacement))
        extnurl = rpurl
    return extnurl


def get_test_data(params, tdata, epoint):
    get_extracted_data = extractedValue(tdata, epoint)
    getPattern = pattern(extnurl=params, exValue=get_extracted_data)
    return getPattern


def saved_response_Data(start_time, vroles, callapis, tdata):
    global status_code

    try:
        status_code = callapis.status_code
        getalljson = json.loads(callapis.content)
        elapsed_time_secs = time.time() - start_time
        time_elapsed = timedelta(seconds=round(elapsed_time_secs))
        log.info(time_elapsed)
        if tdata != '!' and '!' not in tdata:
            if 'rMix' in tdata:
                dp_res_file = mypath / 'test_data' / 'json_data' / 'mixdata'
            else:
                dp_res_file = mypath / 'test_data' / 'json_data' / 'resdata'
            if 'vIdx' in tdata:
                vroles = 'vIdx.json'
            resp_file = dp_res_file / vroles
            dumpData(apiselect=resp_file, getalljson=getalljson)

            # Create Splited Tables with Index
            # dbname = str(vroles).split('.')[0]
            # cgetCreateTables(jsonDatax=getalljson, dbname=dbname, reqres='response')
            # time.sleep(1)
            # Create Splited Tables without Index
            # respdata(jsdata=getalljson, dbname=dbname)

        return status_code, getalljson
    except Exception as e:
        return status_code, 'httpstatus'


def saved_request_Data(payload, vroles, tdata):
    if tdata != '!' and '!' not in tdata:
        if payload != 'None' or payload == '!' and tdata != 'None':
            try:
                gettet = json.loads(payload)
            except json.JSONDecodeError:
                gettet = payload
            dp_req_file = mypath / 'test_data' / 'json_data' / 'reqdata' / vroles
            dumpData(apiselect=dp_req_file, getalljson=gettet)

            # Create Splited Tables with Index
            # dbname = str(vroles).split('.')[0]
            # getCreateTables(jsonDatax=gettet, dbname=dbname, reqres='request')
            # time.sleep(1)
            # Create Splited Tables without Index
            # requdata(jsdata=gettet, dbname=dbname)


def get_nested_multiple_values(data, keys="attributeRequests.attributeId"):
    if isinstance(keys, str):
        keys = keys.split(",")
    if len(keys) == 0:
        return None
    values = [[] for _ in range(len(keys))]  # Create a list to store values for each key
    for i, key in enumerate(keys):
        nested_keys = key.split(".")
        temp_data = data
        for nested_key in nested_keys:
            if isinstance(temp_data, list):
                temp_values = []
                for item in temp_data:
                    if nested_key in item:
                        temp_values.append(item[nested_key])
                    else:
                        temp_values.append(None)
                temp_data = temp_values
            elif nested_key in temp_data:
                temp_data = temp_data[nested_key]
            else:
                temp_data = None
                break
        values[i] = temp_data
    return tuple(values)


def extractedValue(tdata, apipoint, ePoint=None, eValue=None, dictdata=None, gnx=0):
    global random_value, value
    getx, gnx, gxa = None, 0, None
    if ePoint is None and dictdata is None:
        if tdata != 'None' and tdata != '':
            eHome, ePoint, apxpoint, eValue = str(tdata).split('|')
            print(eHome, ePoint, apxpoint, eValue)
            if eValue == '': eValue = None
            if eHome not in ['filterdata', 'mixdata'] and apxpoint == '':
                xroles = config.get('apiEndpoint', apipoint)
                xroles, cxUrl = xroles.split(',')
            elif eHome not in ['filterdata', 'mixdata'] and apxpoint != '':
                xroles = config.get('apiEndpoint', apxpoint)
                xroles, cxUrl = xroles.split(',')
            else:
                if 'mixdata' in eHome or eHome == 'mixdata':
                    xroles = apxpoint
                else:
                    xroles = apipoint
            vroles = str(xroles) + '.json'
            xrolesjson = mypath / 'test_data' / 'json_data' / eHome / vroles
            dictdata = data_required(xrolesjson)
    if dictdata:
        ePoint = get_nested_multiple_values(data=dictdata, keys=ePoint)
        getx = []
        for getresp in ePoint:
            if type(getresp) is str or type(getresp) is int:
                random_value = str(getresp)
                getx = random_value
                gxa = 'S1'
            elif eValue is None and type(getresp) == list:
                filtered_data = [x for x in getresp if x is not None]
                first_element = filtered_data[0]
                count = filtered_data.index(first_element) + 1
                if count > 0 and gnx == 0:
                    gnx = random.randint(0, len(filtered_data) - 1)
                getx = filtered_data[gnx]
                gxa = 'S2'
            else:
                filtered_data = [x for x in getresp if x is not None]
                if filtered_data:
                    random_value = filtered_data
                    # getx.append(random_value)
                    getx = random_value
                    gxa = 'S3'
    return getx, gnx, gxa


def get_data_expected(ddata, apipoint):
    # Use regular expressions to find the string inside the braces
    try:
        if '$' in ddata:
            xid = []
            match = re.findall(r'\$(.*?)\$', ddata)
            gnx = 0
            for variable in match:
                exresults, gnx, gxa = extractedValue(tdata=variable, apipoint=apipoint, gnx=gnx)
                xid.append(exresults)
                gnx = gnx
            keys, values = xid, match
            for pattern, replacements in zip(values, keys):
                rpurl = ddata.replace('$' + pattern + '$', str(replacements))
                ddata = rpurl
            return ddata
        else:
            if '{}' in ddata:
                return ddata
            else:
                match = re.search(r'{(.*?)}', ddata)
                pattern = r'\{[^{}]+\}'
                matching_variables = re.findall(pattern, ddata)
                if match:
                    # Extract the string inside the braces
                    extracted_string = match.group(1)
                    # exresults = get_nested_value(data=payload, keys=extracted_string)
                    exresults, gnx, gxa = extractedValue(tdata=extracted_string, apipoint=str(apipoint).split(':')[1])
                    # replaced_string = re.sub(r'{(.*?)}', extracted_string, exresults)
                    replaced_string = ddata.replace(str('{' + extracted_string + '}'), str(exresults))
                    return replaced_string
                else:
                    return ddata
    except Exception as e:
        return str(e)


def get_defined_data(apipoint, ddata):
    # Use regular expressions to find the string inside the braces
    try:
        global dResults, extnurl
        if '$' in ddata:
            xid = []
            match = re.findall(r'\$(.*?)\$', ddata)
            # print(match)
            gnx = 0
            for variable in match:
                exresults, gnx, gxa = extractedValue(tdata=variable, apipoint=apipoint, gnx=gnx)
                xid.append(exresults)
                gnx = gnx
            keys, values = xid, match
            for pattern, replacements in zip(values, keys):
                rpurl = ddata.replace('$' + pattern + '$', str(replacements))
                ddata = rpurl
            return ddata
        else:
            match = re.search(r'{(.*?)}', ddata)
            if match:
                extracted_string = match.group(1)
                exresults, gnx, gxa = extractedValue(tdata=extracted_string, apipoint=apipoint)
                if gxa in ['S1', 'S2']:
                    dResults = exresults
                else:
                    if type(exresults[0]) == list:
                        dResults = []
                        for xresults in exresults[0]:
                            dResults.append(str(xresults))
                        dResults = '-'.join(dResults)
                    else:
                        dResults = exresults[0]
                replaced_string = ddata.replace('{' + extracted_string + '}', str(dResults))
                return replaced_string
            else:
                return ddata
    except Exception as e:
        return ddata

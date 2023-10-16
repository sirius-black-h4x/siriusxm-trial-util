#!/usr/bin/env python3

import sys

import requests

SESSION = requests.Session()


def appconfig():
    response = SESSION.post(
        url="https://mcare.siriusxm.ca/authService/100000002/appconfig",
        headers={
            "X-HTTP-Method-Override": "GET",
            "Accept": "*/*",
            "X-Kony-App-Secret": "e3048b73f2f7a6c069f7d8abf5864115",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "X-Kony-App-Key": "85ee60a3c8f011baaeba01ff3a5ae2c9",
            "User-Agent": "SXM Dealer/3 CFNetwork/1399 Darwin/22.1.0",
        },
    )

    return response.json()


def login():
    response = SESSION.post(
        url="https://mcare.siriusxm.ca/authService/100000002/login",
        headers={
            "X-Kony-Platform-Type": "ios",
            "Accept": "application/json",
            "X-Kony-App-Secret": "e3048b73f2f7a6c069f7d8abf5864115",
            "Accept-Language": "en-US,en;q=0.9",
            "X-Kony-SDK-Type": "js",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "SXM Dealer/3 CFNetwork/1399 Darwin/22.1.0",
            "X-Kony-SDK-Version": "8.4.134",
            "X-Kony-App-Key": "85ee60a3c8f011baaeba01ff3a5ae2c9",
        },
    )

    return response.json().get("claims_token").get("value")


def version_control(token: str):
    response = SESSION.post(
        url="https://mcare.siriusxm.ca/services/DealerAppService7/VersionControl",
        headers={
            "Accept": "*/*",
            "X-Kony-ReportingParams": '{"os":"16.1.1","dm":"unknown","did":"8FF62332-71B1-4699-B11B-7D32F9C12999",'
            '"ua":"iPhone","aid":"DealerApp","aname":"SXM Dealer","chnl":"mobile",'
            '"plat":"ios","aver":"2.4.0","atype":"native","stype":"b2c","kuid":"",'
            '"mfaid":"3de259b8-e39b-4f60-b2ba-ae3d4a2655bf",'
            '"mfbaseid":"5fa7a77c-aa7e-423f-b9bd-4fe67e91bb71","mfaname":"DealerApp",'
            '"sdkversion":"8.4.134","sdktype":"js","fid":"frmHome","sessiontype":"I",'
            '"rsid":"1668318090440-ac27-f025-7685","svcid":"VersionControl"}',
            "X-Kony-API-Version": "1.0",
            "X-Kony-DeviceId": "8FF62332-71B1-4699-B11B-7D32F9C12999",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "SXM Dealer/3 CFNetwork/1399 Darwin/22.1.0",
            "X-Kony-Authorization": token,
        },
        data={
            "deviceCategory": "iPhone",
            "appver": "2.4.0",
            "deviceLocale": "en_US",
            "deviceModel": "unknown",
            "deviceVersion": "16.1.1",
            "deviceType": "",
        },
    )

    return response.json()


def get_properties(token: str):
    response = SESSION.post(
        url="https://mcare.siriusxm.ca/services/DealerAppService7/getProperties",
        headers={
            "Accept": "*/*",
            "X-Kony-ReportingParams": '{"os":"16.1.1","dm":"unknown","did":"8FF62332-71B1-4699-B11B-7D32F9C12999",'
            '"ua":"iPhone","aid":"DealerApp","aname":"SXM Dealer","chnl":"mobile",'
            '"plat":"ios","aver":"2.4.0","atype":"native","stype":"b2c","kuid":"",'
            '"mfaid":"3de259b8-e39b-4f60-b2ba-ae3d4a2655bf",'
            '"mfbaseid":"5fa7a77c-aa7e-423f-b9bd-4fe67e91bb71",'
            '"mfaname":"DealerApp","sdkversion":"8.4.134","sdktype":"js","fid":"frmHome",'
            '"sessiontype":"I","rsid":"1668318090440-ac27-f025-7685",'
            '"svcid":"getProperties"}',
            "X-Kony-API-Version": "1.0",
            "X-Kony-DeviceId": "8FF62332-71B1-4699-B11B-7D32F9C12999",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "SXM Dealer/3 CFNetwork/1399 Darwin/22.1.0",
            "X-Kony-Authorization": token,
        },
        data={},
    )

    return response.json()


def update_device_sat_refresh_with_priority(device_id: str, token: str):
    response = SESSION.post(
        url="https://mcare.siriusxm.ca/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority",
        headers={
            "Accept": "*/*",
            "X-Kony-ReportingParams": '{"os":"16.1.1","dm":"unknown","did":"8FF62332-71B1-4699-B11B-7D32F9C12999",'
            '"ua":"iPhone","aid":"DealerApp","aname":"SXM Dealer","chnl":"mobile",'
            '"plat":"ios","aver":"2.4.0","atype":"native","stype":"b2c","kuid":"",'
            '"mfaid":"3de259b8-e39b-4f60-b2ba-ae3d4a2655bf",'
            '"mfbaseid":"5fa7a77c-aa7e-423f-b9bd-4fe67e91bb71","mfaname":"DealerApp",'
            '"sdkversion":"8.4.134","sdktype":"js","fid":"frmRefresh","sessiontype":"I",'
            '"rsid":"1668318090440-ac27-f025-7685",'
            '"svcid":"updateDeviceSATRefreshWithPriority"}',
            "X-Kony-API-Version": "1.0",
            "X-Kony-DeviceId": "8FF62332-71B1-4699-B11B-7D32F9C12999",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "SXM Dealer/3 CFNetwork/1399 Darwin/22.1.0",
            "X-Kony-Authorization": token,
        },
        data={
            "deviceId": device_id,
            "appVersion": "2.4.0",
            "lng": "-86.210274696",
            "provisionPackageName": "",
            "vin": "",
            "deviceID": "8FF62332-71B1-4699-B11B-7D32F9C12999",
            "flow_name": "Enter Radio ID",
            "provisionPriority": "2",
            "provisionType": "activate",
            "phone": "",
            "device_Type": "iPhone unknown",
            "note": "1",
            "AuthName": "",
            "os_Version": "iPhone 16.1.1",
            "AuthPwd": "",
            "lat": "32.374343677",
            "provisionDate": "",
            "dmCode": "",
            "vehicle_active_flag": "",
            "base64": "X06FDae2079Ge5H9PYW5sg==",
        },
    )

    return response.json()


def get_crm_account_plan_information(device_id: str, token: str, seq_value):
    response = SESSION.post(
        url="https://mcare.siriusxm.ca/services/DemoConsumptionRules/GetCRMAccountPlanInformation",
        headers={
            "Accept": "*/*",
            "X-Kony-ReportingParams": '{"os":"16.1.1","dm":"unknown","did":"8FF62332-71B1-4699-B11B-7D32F9C12999",'
            '"ua":"iPhone","aid":"DealerApp","aname":"SXM Dealer","chnl":"mobile",'
            '"plat":"ios","aver":"2.4.0","atype":"native","stype":"b2c","kuid":"",'
            '"mfaid":"3de259b8-e39b-4f60-b2ba-ae3d4a2655bf",'
            '"mfbaseid":"5fa7a77c-aa7e-423f-b9bd-4fe67e91bb71","mfaname":"DealerApp",'
            '"sdkversion":"8.4.134","sdktype":"js","fid":"frmRefresh","sessiontype":"I",'
            '"rsid":"1668318090440-ac27-f025-7685","svcid":"GetCRMAccountPlanInformation"}',
            "X-Kony-API-Version": "1.0",
            "X-Kony-DeviceId": "8FF62332-71B1-4699-B11B-7D32F9C12999",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "SXM Dealer/3 CFNetwork/1399 Darwin/22.1.0",
            "X-Kony-Authorization": token,
        },
        data={
            "seqVal": seq_value,
            "deviceId": device_id,
        },
    )

    return response.json()


def db_update_for_google():
    response = SESSION.post(
        url="https://mcare.siriusxm.ca/services/DBSuccessUpdate/DBUpdateForGoogle"
    )

    return response.json()


def block_list_device(token: str):
    response = SESSION.post(
        url="https://mcare.siriusxm.ca/services/USBlockListDevice/BlockListDevice",
        headers={
            "Accept": "*/*",
            "X-Kony-ReportingParams": '{"os":"16.1.1","dm":"unknown","did":"8FF62332-71B1-4699-B11B-7D32F9C12999",'
            '"ua":"iPhone","aid":"DealerApp","aname":"SXM Dealer","chnl":"mobile",'
            '"plat":"ios","aver":"2.4.0","atype":"native","stype":"b2c","kuid":"",'
            '"mfaid":"3de259b8-e39b-4f60-b2ba-ae3d4a2655bf",'
            '"mfbaseid":"5fa7a77c-aa7e-423f-b9bd-4fe67e91bb71","mfaname":"DealerApp",'
            '"sdkversion":"8.4.134","sdktype":"js","fid":"frmRefresh","sessiontype":"I",'
            '"rsid":"1668318090440-ac27-f025-7685","svcid":"BlockListDevice"}',
            "X-Kony-API-Version": "1.0",
            "X-Kony-DeviceId": "8FF62332-71B1-4699-B11B-7D32F9C12999",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "SXM Dealer/3 CFNetwork/1399 Darwin/22.1.0",
            "X-Kony-Authorization": token,
        },
        data={
            "deviceId": "8FF62332-71B1-4699-B11B-7D32F9C12999",
        },
    )

    return response.json()


def create_account(device_id: str, token: str, seq_value):
    response = SESSION.post(
        url="https://mcare.siriusxm.ca/services/DealerAppService3/CreateAccount",
        headers={
            "Connection": "close",
            "Accept": "*/*",
            "X-Kony-ReportingParams": '{"os":"16.1.1","dm":"unknown","did":"8FF62332-71B1-4699-B11B-7D32F9C12999",'
            '"ua":"iPhone","aid":"DealerApp","aname":"SXM Dealer","chnl":"mobile",'
            '"plat":"ios","aver":"2.4.0","atype":"native","stype":"b2c","kuid":"",'
            '"mfaid":"3de259b8-e39b-4f60-b2ba-ae3d4a2655bf",'
            '"mfbaseid":"5fa7a77c-aa7e-423f-b9bd-4fe67e91bb71","mfaname":"DealerApp",'
            '"sdkversion":"8.4.134","sdktype":"js","fid":"frmRefresh","sessiontype":"I",'
            '"rsid":"1668318090440-ac27-f025-7685","svcid":"CreateAccount"}',
            "X-Kony-API-Version": "1.0",
            "X-Kony-DeviceId": "8FF62332-71B1-4699-B11B-7D32F9C12999",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "SXM Dealer/3 CFNetwork/1399 Darwin/22.1.0",
            "X-Kony-Authorization": token,
        },
        data={
            "seqVal": seq_value,
            "deviceId": device_id,
            "oracleCXFailed": "1",
            "appVersion": "2.4.0",
        },
    )

    return response.json()


def update_device_sat_refresh_with_priority_cc(device_id: str, token: str):
    response = SESSION.post(
        url="https://mcare.siriusxm.ca/services/USUpdateDeviceRefreshForCC/updateDeviceSATRefreshWithPriority",
        headers={
            "Accept": "*/*",
            "X-Kony-ReportingParams": '{"os":"16.1.1","dm":"unknown","did":"8FF62332-71B1-4699-B11B-7D32F9C12999",'
            '"ua":"iPhone","aid":"DealerApp","aname":"SXM Dealer","chnl":"mobile",'
            '"plat":"ios","aver":"2.4.0","atype":"native","stype":"b2c","kuid":"",'
            '"mfaid":"3de259b8-e39b-4f60-b2ba-ae3d4a2655bf",'
            '"mfbaseid":"5fa7a77c-aa7e-423f-b9bd-4fe67e91bb71","mfaname":"DealerApp",'
            '"sdkversion":"8.4.134","sdktype":"js","fid":"frmRefresh","sessiontype":"I",'
            '"rsid":"1668318090440-ac27-f025-7685",'
            '"svcid":"updateDeviceSATRefreshWithPriority"}',
            "X-Kony-API-Version": "1.0",
            "X-Kony-DeviceId": "8FF62332-71B1-4699-B11B-7D32F9C12999",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "SXM Dealer/3 CFNetwork/1399 Darwin/22.1.0",
            "X-Kony-Authorization": token,
        },
        data={
            "deviceId": device_id,
            "provisionPriority": "2",
            "appVersion": "2.4.0",
            "note": "1",
            "provisionPackageName": "",
            "dmCode": "",
            "device_Type": "iPhone unknown",
            "deviceID": "8FF62332-71B1-4699-B11B-7D32F9C12999",
            "os_Version": "iPhone 16.1.1",
            "provisionType": "activate",
            "provisionDate": "",
        },
    )

    return response.json()


def process(device_id: str):
    print(f"{type(device_id)}: {device_id}")
    print(f"appconfig")
    appconfig()
    print("auth")
    auth_token = login()
    print(f"auth_token.len: {len(auth_token)}")
    print("version_control")
    version_control(auth_token)
    print("get_properties")
    get_properties(auth_token)
    response = update_device_sat_refresh_with_priority(device_id, auth_token)
    print(f"update_1: {response}")
    seq = int(response.get("seqValue"))
    print(f"seq: {seq}")
    print(f"get_crm: {get_crm_account_plan_information(device_id, auth_token, seq)}")
    print(f"db_1: {db_update_for_google()}")
    print(f"block: {block_list_device(auth_token)}")
    print(f"create: {create_account(device_id, auth_token, seq)}")
    print(f"update_2: {update_device_sat_refresh_with_priority_cc(device_id, auth_token)}")
    print(f"db_2: {db_update_for_google()}")


def main() -> int:
    try:
        radio_id_input = input("Enter Radio ID: ")
        process(radio_id_input)
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())

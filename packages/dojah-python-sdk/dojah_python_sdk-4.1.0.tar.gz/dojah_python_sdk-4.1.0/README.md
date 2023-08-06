# dojah-python-sdk@4.1.0
Use Dojah to verify, onboard and manage user identity across Africa!


## Requirements

Python >=3.7

## Installing

```sh
pip install dojah-python-sdk==4.1.0
```

## Getting Started

```python
from pprint import pprint
from dojah_client import Dojah, ApiException

dojah = Dojah(
    # Defining the host is optional and defaults to https://api.dojah.io
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.dojah.io",
    # Configure API key authorization: apikeyAuth
    authorization="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
    # Configure API key authorization: appIdAuth
    app_id="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'appIdAuth': 'Bearer'},
)

try:
    # Get AML Info
    get_screening_info_response = dojah.aml.get_screening_info(
        profile_id="WC7117469",  # optional
    )
    pprint(get_screening_info_response.headers)
    pprint(get_screening_info_response.status)
    pprint(get_screening_info_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AMLApi.get_screening_info: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from dojah_client import Dojah, ApiException

dojah = Dojah(
    # Defining the host is optional and defaults to https://api.dojah.io
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.dojah.io",
    # Configure API key authorization: apikeyAuth
    authorization="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
    # Configure API key authorization: appIdAuth
    app_id="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'appIdAuth': 'Bearer'},
)


async def main():
    try:
        # Get AML Info
        get_screening_info_response = await dojah.aml.aget_screening_info(
            profile_id="WC7117469",  # optional
        )
        pprint(get_screening_info_response.headers)
        pprint(get_screening_info_response.status)
        pprint(get_screening_info_response.round_trip_time)
    except ApiException as e:
        print("Exception when calling AMLApi.get_screening_info: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```


## Documentation for API Endpoints

All URIs are relative to *https://api.dojah.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AMLApi* | [**get_screening_info**](docs/apis/tags/AMLApi.md#get_screening_info) | **GET** /api/v1/aml/screening/info | Get AML Info
*AMLApi* | [**screen_aml**](docs/apis/tags/AMLApi.md#screen_aml) | **POST** /api/v1/aml/screening/platform | AML Screening
*AuthenticationApi* | [**get_sender_id**](docs/apis/tags/AuthenticationApi.md#get_sender_id) | **GET** /api/v1/messaging/sender_ids | Messaging - Get Sender IDs
*AuthenticationApi* | [**get_sms_status**](docs/apis/tags/AuthenticationApi.md#get_sms_status) | **GET** /v1/messaging/sms/get_status | Messaging - Get SMS Status
*AuthenticationApi* | [**request_sender_id**](docs/apis/tags/AuthenticationApi.md#request_sender_id) | **POST** /api/v1/messaging/sender_id | Messaging - Request Sender ID
*AuthenticationApi* | [**send_otp**](docs/apis/tags/AuthenticationApi.md#send_otp) | **POST** /api/v1/messaging/otp | Messaging - Send OTP
*AuthenticationApi* | [**send_sms**](docs/apis/tags/AuthenticationApi.md#send_sms) | **POST** /api/v1/messaging/sms | Messaging - Send SMS
*AuthenticationApi* | [**validate_otp**](docs/apis/tags/AuthenticationApi.md#validate_otp) | **GET** /api/v1/messaging/otp/validate | Messaging - Validate OTP
*DocumentAnalysisApi* | [**analyze_document**](docs/apis/tags/DocumentAnalysisApi.md#analyze_document) | **POST** /api/v1/document/analysis | KYC - Document Analysis
*FraudApi* | [**get_email_reputation**](docs/apis/tags/FraudApi.md#get_email_reputation) | **GET** /api/v1/kyc/email | Email Reputation
*FraudApi* | [**get_ip_reputation**](docs/apis/tags/FraudApi.md#get_ip_reputation) | **GET** /api/v1/fraud/ip | IP Reputation
*FraudApi* | [**screen_phone**](docs/apis/tags/FraudApi.md#screen_phone) | **GET** /api/v1/fraud/phone | Phone Screening
*FraudApi* | [**screen_user**](docs/apis/tags/FraudApi.md#screen_user) | **GET** /api/v1/fraud/user | User Screening
*GHKYCApi* | [**get_drivers_license**](docs/apis/tags/GHKYCApi.md#get_drivers_license) | **GET** /api/v1/gh/kyc/dl | Driver&#x27;s License
*GHKYCApi* | [**get_passport**](docs/apis/tags/GHKYCApi.md#get_passport) | **GET** /api/v1/gh/kyc/passport | Passport
*GHKYCApi* | [**get_ssnit**](docs/apis/tags/GHKYCApi.md#get_ssnit) | **GET** /api/v1/gh/kyc/ssnit | SSNIT
*GHKYCApi* | [**get_voter**](docs/apis/tags/GHKYCApi.md#get_voter) | **GET** /api/v1/gh/kyc/voter | Voter ID Lookup
*GeneralApi* | [**get_banks**](docs/apis/tags/GeneralApi.md#get_banks) | **GET** /v1/general/banks | General - Get Banks
*GeneralApi* | [**get_bin**](docs/apis/tags/GeneralApi.md#get_bin) | **GET** /v1/general/bin | General Resolve BIN
*GeneralApi* | [**get_nuban**](docs/apis/tags/GeneralApi.md#get_nuban) | **GET** /api/v1/general/account | General Resolve NUBAN
*GlobalKYCApi* | [**ca_ekyc**](docs/apis/tags/GlobalKYCApi.md#ca_ekyc) | **GET** /api/v1/ca/kyc | Canada Ekyc
*GlobalKYCApi* | [**get_us_ssn**](docs/apis/tags/GlobalKYCApi.md#get_us_ssn) | **GET** /api/v1/us/kyc | US SSN
*GlobalKYCApi* | [**uk_two_plus_two**](docs/apis/tags/GlobalKYCApi.md#uk_two_plus_two) | **GET** /api/v1/uk/kyc | UK 2+2
*KEKYCApi* | [**get_national_id**](docs/apis/tags/KEKYCApi.md#get_national_id) | **GET** /api/v1/ke/kyc/id | KYC - National ID
*KEKYCApi* | [**get_passport**](docs/apis/tags/KEKYCApi.md#get_passport) | **GET** /api/v1/ke/kyc/passport | KYC - Passport
*KYBApi* | [**business_detail**](docs/apis/tags/KYBApi.md#business_detail) | **GET** /api/v1/kyb/business/detail | Business Detail
*KYBApi* | [**business_search**](docs/apis/tags/KYBApi.md#business_search) | **GET** /api/v1/kyb/business/search | Business Search
*KYBApi* | [**get_cac**](docs/apis/tags/KYBApi.md#get_cac) | **GET** /api/v1/kyc/cac | KYC - Get CAC 
*KYBApi* | [**get_tin**](docs/apis/tags/KYBApi.md#get_tin) | **GET** /api/v1/kyc/tin | KYC - Fetch Tin
*KYCApi* | [**check_liveness**](docs/apis/tags/KYCApi.md#check_liveness) | **POST** /api/v1/ml/liveness | Liveness Check
*KYCApi* | [**get_accounts**](docs/apis/tags/KYCApi.md#get_accounts) | **GET** /api/v1/kyc/accounts | KYC - Fetch Accounts 
*KYCApi* | [**get_address_verification**](docs/apis/tags/KYCApi.md#get_address_verification) | **GET** /api/v1/kyc/address | Fetch Address Verification Data
*KYCApi* | [**get_bvn_from_nuban**](docs/apis/tags/KYCApi.md#get_bvn_from_nuban) | **GET** /api/v1/kyc/nuban/bvn | Lookup BVN from NUBAN
*KYCApi* | [**get_vin**](docs/apis/tags/KYCApi.md#get_vin) | **GET** /api/v1/kyc/vin | KYC - Get VIN
*KYCApi* | [**submit_address**](docs/apis/tags/KYCApi.md#submit_address) | **POST** /api/v1/kyc/address | Submit Address
*MLApi* | [**verify_photo_id_with_selfie**](docs/apis/tags/MLApi.md#verify_photo_id_with_selfie) | **POST** /api/v1/kyc/photoid/verify | KYC - Selfie Photo ID Verification
*NigeriaKYCApi* | [**get_basic_bvn**](docs/apis/tags/NigeriaKYCApi.md#get_basic_bvn) | **GET** /api/v1/kyc/bvn | KYC - Get Basic BVN Info
*NigeriaKYCApi* | [**get_basic_bvn1**](docs/apis/tags/NigeriaKYCApi.md#get_basic_bvn1) | **GET** /api/v1/kyc/bvn/basic | KYC - Lookup BVN Basic 1
*NigeriaKYCApi* | [**get_basic_phone_number**](docs/apis/tags/NigeriaKYCApi.md#get_basic_phone_number) | **GET** /api/v1/kyc/phone_number/basic | KYC Lookup Phone Number Basic
*NigeriaKYCApi* | [**get_drivers_license**](docs/apis/tags/NigeriaKYCApi.md#get_drivers_license) | **GET** /api/v1/kyc/dl | KYC - Get Drivers License Info
*NigeriaKYCApi* | [**get_nin**](docs/apis/tags/NigeriaKYCApi.md#get_nin) | **GET** /api/v1/kyc/nin | KYC - Get NIN Info
*NigeriaKYCApi* | [**get_normal_bvn**](docs/apis/tags/NigeriaKYCApi.md#get_normal_bvn) | **GET** /api/v1/kyc/bvn/full | KYC - Lookup BVN Normal
*NigeriaKYCApi* | [**get_nuban**](docs/apis/tags/NigeriaKYCApi.md#get_nuban) | **GET** /api/v1/kyc/nuban | KYC - Get NUBAN Information
*NigeriaKYCApi* | [**get_passport**](docs/apis/tags/NigeriaKYCApi.md#get_passport) | **GET** /api/v1/kyc/passport | KYC - Passport
*NigeriaKYCApi* | [**get_phone_number**](docs/apis/tags/NigeriaKYCApi.md#get_phone_number) | **GET** /api/v1/kyc/phone_number | KYC - Lookup Phone Number
*NigeriaKYCApi* | [**get_premium_bvn**](docs/apis/tags/NigeriaKYCApi.md#get_premium_bvn) | **GET** /api/v1/kyc/bvn/advance | KYC - Lookup BVN Premium
*NigeriaKYCApi* | [**get_vnin**](docs/apis/tags/NigeriaKYCApi.md#get_vnin) | **GET** /api/v1/kyc/vnin | Lookup VNIN
*PurchaseApi* | [**send_airtime**](docs/apis/tags/PurchaseApi.md#send_airtime) | **POST** /v1/purchase/airtime | Purchase - Send Airtime
*ServicesApi* | [**get_wallet_balance**](docs/apis/tags/ServicesApi.md#get_wallet_balance) | **GET** /api/v1/balance | Get Dojah Wallet Balance
*TZKYCApi* | [**get_nin**](docs/apis/tags/TZKYCApi.md#get_nin) | **GET** /api/v1/tz/kyc/nin | Lookup TZ NIN
*UGKYCApi* | [**get_voter**](docs/apis/tags/UGKYCApi.md#get_voter) | **GET** /api/v1/ug/kyc/voter | Voters ID
*VerificationsApi* | [**validate_bvn**](docs/apis/tags/VerificationsApi.md#validate_bvn) | **GET** /v1/kyc/bvn | KYC - Validate BVN
*VerificationsApi* | [**verify_age**](docs/apis/tags/VerificationsApi.md#verify_age) | **GET** /v1/kyc/age_verification | KYC - Age Verification
*VerificationsApi* | [**verify_selfie_bvn**](docs/apis/tags/VerificationsApi.md#verify_selfie_bvn) | **POST** /v1/kyc/bvn/verify | KYV - Selfie BVN Verificatoin
*VerificationsApi* | [**verify_selfie_nin**](docs/apis/tags/VerificationsApi.md#verify_selfie_nin) | **POST** /api/v1/kyc/nin/verify | KYC - Selfie NIN Verification
*VerificationsApi* | [**verify_selfie_vnin**](docs/apis/tags/VerificationsApi.md#verify_selfie_vnin) | **POST** /api/v1/kyc/vnin/verify | KYC - Selfie vNIN verification
*WebHooksApi* | [**delete_webhook**](docs/apis/tags/WebHooksApi.md#delete_webhook) | **DELETE** /api/v1/webhook/delete | Delete Webhook
*WebHooksApi* | [**get_webhooks**](docs/apis/tags/WebHooksApi.md#get_webhooks) | **GET** /api/v1/webhook/fetch | Fetch All Webhooks
*WebHooksApi* | [**notify_webhook**](docs/apis/tags/WebHooksApi.md#notify_webhook) | **POST** /api/v1/webhook/notify | Post Hook
*WebHooksApi* | [**subscribe_service**](docs/apis/tags/WebHooksApi.md#subscribe_service) | **POST** /api/v1/webhook/subscribe | Subscribe to service
*ZAFKYCApi* | [**get_id**](docs/apis/tags/ZAFKYCApi.md#get_id) | **GET** /api/v1/za/kyc/id | KYC - Lookup ID
*ZWKYCApi* | [**check_credit**](docs/apis/tags/ZWKYCApi.md#check_credit) | **GET** /api/v1/zw/kyc/fcb | Credit Check
*ZWKYCApi* | [**verify_id**](docs/apis/tags/ZWKYCApi.md#verify_id) | **GET** /api/v1/zw/kyc/nin | National ID Verification

## Documentation For Models

 - [AmlScreenAmlRequest](docs/models/AmlScreenAmlRequest.md)
 - [AmlScreenAmlResponse](docs/models/AmlScreenAmlResponse.md)
 - [AmlScreenAmlResponseEntity](docs/models/AmlScreenAmlResponseEntity.md)
 - [AnalyzeDocumentResponse](docs/models/AnalyzeDocumentResponse.md)
 - [AnalyzeDocumentResponseEntity](docs/models/AnalyzeDocumentResponseEntity.md)
 - [AnalyzeDocumentResponseEntityDocumentImages](docs/models/AnalyzeDocumentResponseEntityDocumentImages.md)
 - [AnalyzeDocumentResponseEntityDocumentType](docs/models/AnalyzeDocumentResponseEntityDocumentType.md)
 - [AnalyzeDocumentResponseEntityStatus](docs/models/AnalyzeDocumentResponseEntityStatus.md)
 - [AnalyzeDocumentResponseEntityTextData](docs/models/AnalyzeDocumentResponseEntityTextData.md)
 - [AnalyzeDocumentResponseEntityTextDataItem](docs/models/AnalyzeDocumentResponseEntityTextDataItem.md)
 - [AuthenticationSendOtpRequest](docs/models/AuthenticationSendOtpRequest.md)
 - [AuthenticationSendOtpResponse](docs/models/AuthenticationSendOtpResponse.md)
 - [AuthenticationSendOtpResponseEntity](docs/models/AuthenticationSendOtpResponseEntity.md)
 - [AuthenticationSendOtpResponseEntityItem](docs/models/AuthenticationSendOtpResponseEntityItem.md)
 - [AuthenticationValidateOtpResponse](docs/models/AuthenticationValidateOtpResponse.md)
 - [AuthenticationValidateOtpResponseEntity](docs/models/AuthenticationValidateOtpResponseEntity.md)
 - [DeleteWebhookResponse](docs/models/DeleteWebhookResponse.md)
 - [FraudGetEmailReputationResponse](docs/models/FraudGetEmailReputationResponse.md)
 - [FraudGetEmailReputationResponseEntity](docs/models/FraudGetEmailReputationResponseEntity.md)
 - [FraudGetEmailReputationResponseEntityAccountDetailsRegistered](docs/models/FraudGetEmailReputationResponseEntityAccountDetailsRegistered.md)
 - [FraudGetEmailReputationResponseEntityBreachDetails](docs/models/FraudGetEmailReputationResponseEntityBreachDetails.md)
 - [FraudGetEmailReputationResponseEntityBreachDetailsBreaches](docs/models/FraudGetEmailReputationResponseEntityBreachDetailsBreaches.md)
 - [FraudGetEmailReputationResponseEntityDetails](docs/models/FraudGetEmailReputationResponseEntityDetails.md)
 - [FraudGetEmailReputationResponseEntityDetailsProfiles](docs/models/FraudGetEmailReputationResponseEntityDetailsProfiles.md)
 - [FraudGetEmailReputationResponseEntityDomainDetails](docs/models/FraudGetEmailReputationResponseEntityDomainDetails.md)
 - [FraudGetIpReputationResponse](docs/models/FraudGetIpReputationResponse.md)
 - [FraudGetIpReputationResponseEntity](docs/models/FraudGetIpReputationResponseEntity.md)
 - [FraudGetIpReputationResponseEntityReport](docs/models/FraudGetIpReputationResponseEntityReport.md)
 - [FraudGetIpReputationResponseEntityReportAnonymity](docs/models/FraudGetIpReputationResponseEntityReportAnonymity.md)
 - [FraudGetIpReputationResponseEntityReportBlacklists](docs/models/FraudGetIpReputationResponseEntityReportBlacklists.md)
 - [FraudGetIpReputationResponseEntityReportInformation](docs/models/FraudGetIpReputationResponseEntityReportInformation.md)
 - [FraudGetIpReputationResponseEntityReportRiskScore](docs/models/FraudGetIpReputationResponseEntityReportRiskScore.md)
 - [FraudScreenPhoneResponse](docs/models/FraudScreenPhoneResponse.md)
 - [FraudScreenPhoneResponseEntity](docs/models/FraudScreenPhoneResponseEntity.md)
 - [FraudScreenPhoneResponseEntityAccountDetailsRegistered](docs/models/FraudScreenPhoneResponseEntityAccountDetailsRegistered.md)
 - [FraudScreenUserResponse](docs/models/FraudScreenUserResponse.md)
 - [FraudScreenUserResponseEntity](docs/models/FraudScreenUserResponseEntity.md)
 - [FraudScreenUserResponseEntityEmailCheckResult](docs/models/FraudScreenUserResponseEntityEmailCheckResult.md)
 - [FraudScreenUserResponseEntityEmailCheckResultAccountDetailsRegistered](docs/models/FraudScreenUserResponseEntityEmailCheckResultAccountDetailsRegistered.md)
 - [FraudScreenUserResponseEntityEmailCheckResultBreachDetails](docs/models/FraudScreenUserResponseEntityEmailCheckResultBreachDetails.md)
 - [FraudScreenUserResponseEntityEmailCheckResultBreachDetailsBreaches](docs/models/FraudScreenUserResponseEntityEmailCheckResultBreachDetailsBreaches.md)
 - [FraudScreenUserResponseEntityEmailCheckResultBreachDetailsBreachesItem](docs/models/FraudScreenUserResponseEntityEmailCheckResultBreachDetailsBreachesItem.md)
 - [FraudScreenUserResponseEntityEmailCheckResultDomainDetails](docs/models/FraudScreenUserResponseEntityEmailCheckResultDomainDetails.md)
 - [FraudScreenUserResponseEntityIpCheckResult](docs/models/FraudScreenUserResponseEntityIpCheckResult.md)
 - [FraudScreenUserResponseEntityIpCheckResultAnonymity](docs/models/FraudScreenUserResponseEntityIpCheckResultAnonymity.md)
 - [FraudScreenUserResponseEntityIpCheckResultBlacklists](docs/models/FraudScreenUserResponseEntityIpCheckResultBlacklists.md)
 - [FraudScreenUserResponseEntityIpCheckResultIpDetails](docs/models/FraudScreenUserResponseEntityIpCheckResultIpDetails.md)
 - [FraudScreenUserResponseEntityIpCheckResultRiskScore](docs/models/FraudScreenUserResponseEntityIpCheckResultRiskScore.md)
 - [FraudScreenUserResponseEntityPhoneCheckResult](docs/models/FraudScreenUserResponseEntityPhoneCheckResult.md)
 - [FraudScreenUserResponseEntityPhoneCheckResultAccountDetailsRegistered](docs/models/FraudScreenUserResponseEntityPhoneCheckResultAccountDetailsRegistered.md)
 - [GeneralGetNubanResponse](docs/models/GeneralGetNubanResponse.md)
 - [GeneralGetNubanResponseEntity](docs/models/GeneralGetNubanResponseEntity.md)
 - [GetBanksResponse](docs/models/GetBanksResponse.md)
 - [GetBanksResponseEntity](docs/models/GetBanksResponseEntity.md)
 - [GetBanksResponseEntityItem](docs/models/GetBanksResponseEntityItem.md)
 - [GetBasicBvnResponse](docs/models/GetBasicBvnResponse.md)
 - [GetBasicBvnResponseEntity](docs/models/GetBasicBvnResponseEntity.md)
 - [GetBinResponse](docs/models/GetBinResponse.md)
 - [GetBinResponseEntity](docs/models/GetBinResponseEntity.md)
 - [GetDriversLicenseResponse](docs/models/GetDriversLicenseResponse.md)
 - [GetDriversLicenseResponseEntity](docs/models/GetDriversLicenseResponseEntity.md)
 - [GetFullBvnResponse](docs/models/GetFullBvnResponse.md)
 - [GetFullBvnResponseEntity](docs/models/GetFullBvnResponseEntity.md)
 - [GetKycDriversLicenseResponse](docs/models/GetKycDriversLicenseResponse.md)
 - [GetKycDriversLicenseResponseEntity](docs/models/GetKycDriversLicenseResponseEntity.md)
 - [GetKycDriversLicenseResponseEntityPersonalDetails](docs/models/GetKycDriversLicenseResponseEntityPersonalDetails.md)
 - [GetKycPassportResponse](docs/models/GetKycPassportResponse.md)
 - [GetKycPassportResponseEntity](docs/models/GetKycPassportResponseEntity.md)
 - [GetNationalIdResponse](docs/models/GetNationalIdResponse.md)
 - [GetNationalIdResponseEntity](docs/models/GetNationalIdResponseEntity.md)
 - [GetNubanResponse](docs/models/GetNubanResponse.md)
 - [GetNubanResponseEntity](docs/models/GetNubanResponseEntity.md)
 - [GetPassportResponse](docs/models/GetPassportResponse.md)
 - [GetPassportResponseEntity](docs/models/GetPassportResponseEntity.md)
 - [GetPhoneNumber404Response](docs/models/GetPhoneNumber404Response.md)
 - [GetPhoneNumber404ResponseEntity](docs/models/GetPhoneNumber404ResponseEntity.md)
 - [GetPhoneNumberResponse](docs/models/GetPhoneNumberResponse.md)
 - [GetPhoneNumberResponseEntity](docs/models/GetPhoneNumberResponseEntity.md)
 - [GetPremiumBvnResponse](docs/models/GetPremiumBvnResponse.md)
 - [GetPremiumBvnResponseEntity](docs/models/GetPremiumBvnResponseEntity.md)
 - [GetSenderIdResponse](docs/models/GetSenderIdResponse.md)
 - [GetSenderIdResponseEntity](docs/models/GetSenderIdResponseEntity.md)
 - [GetSenderIdResponseEntityItem](docs/models/GetSenderIdResponseEntityItem.md)
 - [GetSmsStatusResponse](docs/models/GetSmsStatusResponse.md)
 - [GetSmsStatusResponseEntity](docs/models/GetSmsStatusResponseEntity.md)
 - [GetSsnitResponse](docs/models/GetSsnitResponse.md)
 - [GetSsnitResponseEntity](docs/models/GetSsnitResponseEntity.md)
 - [GetVinResponse](docs/models/GetVinResponse.md)
 - [GetVinResponseEntity](docs/models/GetVinResponseEntity.md)
 - [GetVninResponse](docs/models/GetVninResponse.md)
 - [GetVninResponseEntity](docs/models/GetVninResponseEntity.md)
 - [GetWalletBalanceResponse](docs/models/GetWalletBalanceResponse.md)
 - [GetWalletBalanceResponseEntity](docs/models/GetWalletBalanceResponseEntity.md)
 - [GetWebhooksResponse](docs/models/GetWebhooksResponse.md)
 - [GetWebhooksResponseEntity](docs/models/GetWebhooksResponseEntity.md)
 - [GetWebhooksResponseEntityItem](docs/models/GetWebhooksResponseEntityItem.md)
 - [KybGetCacResponse](docs/models/KybGetCacResponse.md)
 - [KybGetCacResponseEntity](docs/models/KybGetCacResponseEntity.md)
 - [KybGetTinResponse](docs/models/KybGetTinResponse.md)
 - [KybGetTinResponseEntity](docs/models/KybGetTinResponseEntity.md)
 - [KycCheckLivenessRequest](docs/models/KycCheckLivenessRequest.md)
 - [KycSubmitAddressRequest](docs/models/KycSubmitAddressRequest.md)
 - [KycSubmitAddressResponse](docs/models/KycSubmitAddressResponse.md)
 - [KycSubmitAddressResponseEntity](docs/models/KycSubmitAddressResponseEntity.md)
 - [KycSubmitAddressResponseEntityData](docs/models/KycSubmitAddressResponseEntityData.md)
 - [KycSubmitAddressResponseEntityDataApplicant](docs/models/KycSubmitAddressResponseEntityDataApplicant.md)
 - [KycSubmitAddressResponseEntityDataNeighbor](docs/models/KycSubmitAddressResponseEntityDataNeighbor.md)
 - [KycSubmitAddressResponseEntityDataPhotos](docs/models/KycSubmitAddressResponseEntityDataPhotos.md)
 - [MlVerifyPhotoIdWithSelfieRequest](docs/models/MlVerifyPhotoIdWithSelfieRequest.md)
 - [NigeriaKycGetNinResponse](docs/models/NigeriaKycGetNinResponse.md)
 - [NigeriaKycGetNinResponseEntity](docs/models/NigeriaKycGetNinResponseEntity.md)
 - [NigeriaKycGetNinResponseEntityNokAddress2](docs/models/NigeriaKycGetNinResponseEntityNokAddress2.md)
 - [NotifyWebhookRequest](docs/models/NotifyWebhookRequest.md)
 - [NotifyWebhookRequestData](docs/models/NotifyWebhookRequestData.md)
 - [NotifyWebhookResponse](docs/models/NotifyWebhookResponse.md)
 - [PurchaseAirtimeRequest](docs/models/PurchaseAirtimeRequest.md)
 - [PurchaseAirtimeResponse](docs/models/PurchaseAirtimeResponse.md)
 - [PurchaseAirtimeResponseEntity](docs/models/PurchaseAirtimeResponseEntity.md)
 - [PurchaseAirtimeResponseEntityData](docs/models/PurchaseAirtimeResponseEntityData.md)
 - [PurchaseAirtimeResponseEntityDataItem](docs/models/PurchaseAirtimeResponseEntityDataItem.md)
 - [RequestSenderIdRequest](docs/models/RequestSenderIdRequest.md)
 - [RequestSenderIdResponse](docs/models/RequestSenderIdResponse.md)
 - [RequestSenderIdResponseEntity](docs/models/RequestSenderIdResponseEntity.md)
 - [RequestSenderIdResponseEntityItem](docs/models/RequestSenderIdResponseEntityItem.md)
 - [SendSmsRequest](docs/models/SendSmsRequest.md)
 - [SendSmsResponse](docs/models/SendSmsResponse.md)
 - [SendSmsResponseEntity](docs/models/SendSmsResponseEntity.md)
 - [SubscribeServiceRequest](docs/models/SubscribeServiceRequest.md)
 - [SubscribeServiceResponse](docs/models/SubscribeServiceResponse.md)
 - [ValidateBvnResponse](docs/models/ValidateBvnResponse.md)
 - [ValidateBvnResponseEntity](docs/models/ValidateBvnResponseEntity.md)
 - [ValidateBvnResponseEntityBvn](docs/models/ValidateBvnResponseEntityBvn.md)
 - [ValidateBvnResponseEntityFirstName](docs/models/ValidateBvnResponseEntityFirstName.md)
 - [VerificationsVerifySelfieNinRequest](docs/models/VerificationsVerifySelfieNinRequest.md)
 - [VerificationsVerifySelfieVninRequest](docs/models/VerificationsVerifySelfieVninRequest.md)
 - [VerifyAgeResponse](docs/models/VerifyAgeResponse.md)
 - [VerifyAgeResponseEntity](docs/models/VerifyAgeResponseEntity.md)
 - [VerifySelfieBvnRequest](docs/models/VerifySelfieBvnRequest.md)
 - [VerifySelfieBvnResponse](docs/models/VerifySelfieBvnResponse.md)
 - [VerifySelfieBvnResponseEntity](docs/models/VerifySelfieBvnResponseEntity.md)
 - [VerifySelfieBvnResponseEntitySelfieVerification](docs/models/VerifySelfieBvnResponseEntitySelfieVerification.md)
 - [ZafKycGetIdResponse](docs/models/ZafKycGetIdResponse.md)
 - [ZafKycGetIdResponseEntity](docs/models/ZafKycGetIdResponseEntity.md)
 - [ZwKycCheckCreditResponse](docs/models/ZwKycCheckCreditResponse.md)
 - [ZwKycCheckCreditResponseEntity](docs/models/ZwKycCheckCreditResponseEntity.md)
 - [ZwKycVerifyIdResponse](docs/models/ZwKycVerifyIdResponse.md)
 - [ZwKycVerifyIdResponseEntity](docs/models/ZwKycVerifyIdResponseEntity.md)


## Author
This Python package is automatically generated by [Konfig](https://konfigthis.com)

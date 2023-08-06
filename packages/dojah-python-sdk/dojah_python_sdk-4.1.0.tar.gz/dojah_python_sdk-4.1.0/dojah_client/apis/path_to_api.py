import typing_extensions

from dojah_client.paths import PathValues
from dojah_client.apis.paths.api_v1_kyc_cac import ApiV1KycCac
from dojah_client.apis.paths.api_v1_kyc_tin import ApiV1KycTin
from dojah_client.apis.paths.api_v1_kyb_business_search import ApiV1KybBusinessSearch
from dojah_client.apis.paths.api_v1_kyb_business_detail import ApiV1KybBusinessDetail
from dojah_client.apis.paths.api_v1_gh_kyc_dl import ApiV1GhKycDl
from dojah_client.apis.paths.api_v1_gh_kyc_passport import ApiV1GhKycPassport
from dojah_client.apis.paths.api_v1_gh_kyc_ssnit import ApiV1GhKycSsnit
from dojah_client.apis.paths.api_v1_gh_kyc_voter import ApiV1GhKycVoter
from dojah_client.apis.paths.api_v1_ug_kyc_voter import ApiV1UgKycVoter
from dojah_client.apis.paths.api_v1_ke_kyc_id import ApiV1KeKycId
from dojah_client.apis.paths.api_v1_ke_kyc_passport import ApiV1KeKycPassport
from dojah_client.apis.paths.api_v1_tz_kyc_nin import ApiV1TzKycNin
from dojah_client.apis.paths.api_v1_zw_kyc_nin import ApiV1ZwKycNin
from dojah_client.apis.paths.api_v1_zw_kyc_fcb import ApiV1ZwKycFcb
from dojah_client.apis.paths.api_v1_uk_kyc import ApiV1UkKyc
from dojah_client.apis.paths.api_v1_us_kyc import ApiV1UsKyc
from dojah_client.apis.paths.api_v1_ca_kyc import ApiV1CaKyc
from dojah_client.apis.paths.api_v1_za_kyc_id import ApiV1ZaKycId
from dojah_client.apis.paths.api_v1_kyc_nuban import ApiV1KycNuban
from dojah_client.apis.paths.api_v1_kyc_bvn import ApiV1KycBvn
from dojah_client.apis.paths.api_v1_kyc_bvn_basic import ApiV1KycBvnBasic
from dojah_client.apis.paths.api_v1_kyc_bvn_full import ApiV1KycBvnFull
from dojah_client.apis.paths.api_v1_kyc_nin import ApiV1KycNin
from dojah_client.apis.paths.api_v1_kyc_vnin import ApiV1KycVnin
from dojah_client.apis.paths.api_v1_kyc_bvn_advance import ApiV1KycBvnAdvance
from dojah_client.apis.paths.api_v1_kyc_phone_number_basic import ApiV1KycPhoneNumberBasic
from dojah_client.apis.paths.api_v1_kyc_phone_number import ApiV1KycPhoneNumber
from dojah_client.apis.paths.api_v1_kyc_dl import ApiV1KycDl
from dojah_client.apis.paths.api_v1_kyc_passport import ApiV1KycPassport
from dojah_client.apis.paths.api_v1_kyc_vin import ApiV1KycVin
from dojah_client.apis.paths.api_v1_kyc_nuban_bvn import ApiV1KycNubanBvn
from dojah_client.apis.paths.api_v1_kyc_address import ApiV1KycAddress
from dojah_client.apis.paths.api_v1_kyc_accounts import ApiV1KycAccounts
from dojah_client.apis.paths.api_v1_ml_liveness import ApiV1MlLiveness
from dojah_client.apis.paths.v1_kyc_bvn_verify import V1KycBvnVerify
from dojah_client.apis.paths.api_v1_kyc_nin_verify import ApiV1KycNinVerify
from dojah_client.apis.paths.v1_kyc_age_verification import V1KycAgeVerification
from dojah_client.apis.paths.v1_kyc_bvn import V1KycBvn
from dojah_client.apis.paths.api_v1_kyc_vnin_verify import ApiV1KycVninVerify
from dojah_client.apis.paths.api_v1_document_analysis import ApiV1DocumentAnalysis
from dojah_client.apis.paths.api_v1_messaging_sms import ApiV1MessagingSms
from dojah_client.apis.paths.v1_messaging_sms_get_status import V1MessagingSmsGetStatus
from dojah_client.apis.paths.api_v1_messaging_otp import ApiV1MessagingOtp
from dojah_client.apis.paths.api_v1_messaging_otp_validate import ApiV1MessagingOtpValidate
from dojah_client.apis.paths.api_v1_messaging_sender_ids import ApiV1MessagingSenderIds
from dojah_client.apis.paths.api_v1_messaging_sender_id import ApiV1MessagingSenderId
from dojah_client.apis.paths.api_v1_kyc_photoid_verify import ApiV1KycPhotoidVerify
from dojah_client.apis.paths.api_v1_aml_screening_platform import ApiV1AmlScreeningPlatform
from dojah_client.apis.paths.api_v1_aml_screening_info import ApiV1AmlScreeningInfo
from dojah_client.apis.paths.api_v1_fraud_ip import ApiV1FraudIp
from dojah_client.apis.paths.api_v1_kyc_email import ApiV1KycEmail
from dojah_client.apis.paths.api_v1_fraud_user import ApiV1FraudUser
from dojah_client.apis.paths.api_v1_fraud_phone import ApiV1FraudPhone
from dojah_client.apis.paths.v1_purchase_airtime import V1PurchaseAirtime
from dojah_client.apis.paths.v1_general_banks import V1GeneralBanks
from dojah_client.apis.paths.api_v1_general_account import ApiV1GeneralAccount
from dojah_client.apis.paths.v1_general_bin import V1GeneralBin
from dojah_client.apis.paths.api_v1_balance import ApiV1Balance
from dojah_client.apis.paths.api_v1_webhook_subscribe import ApiV1WebhookSubscribe
from dojah_client.apis.paths.api_v1_webhook_delete import ApiV1WebhookDelete
from dojah_client.apis.paths.api_v1_webhook_fetch import ApiV1WebhookFetch
from dojah_client.apis.paths.api_v1_webhook_notify import ApiV1WebhookNotify

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V1_KYC_CAC: ApiV1KycCac,
        PathValues.API_V1_KYC_TIN: ApiV1KycTin,
        PathValues.API_V1_KYB_BUSINESS_SEARCH: ApiV1KybBusinessSearch,
        PathValues.API_V1_KYB_BUSINESS_DETAIL: ApiV1KybBusinessDetail,
        PathValues.API_V1_GH_KYC_DL: ApiV1GhKycDl,
        PathValues.API_V1_GH_KYC_PASSPORT: ApiV1GhKycPassport,
        PathValues.API_V1_GH_KYC_SSNIT: ApiV1GhKycSsnit,
        PathValues.API_V1_GH_KYC_VOTER: ApiV1GhKycVoter,
        PathValues.API_V1_UG_KYC_VOTER: ApiV1UgKycVoter,
        PathValues.API_V1_KE_KYC_ID: ApiV1KeKycId,
        PathValues.API_V1_KE_KYC_PASSPORT: ApiV1KeKycPassport,
        PathValues.API_V1_TZ_KYC_NIN: ApiV1TzKycNin,
        PathValues.API_V1_ZW_KYC_NIN: ApiV1ZwKycNin,
        PathValues.API_V1_ZW_KYC_FCB: ApiV1ZwKycFcb,
        PathValues.API_V1_UK_KYC: ApiV1UkKyc,
        PathValues.API_V1_US_KYC: ApiV1UsKyc,
        PathValues.API_V1_CA_KYC: ApiV1CaKyc,
        PathValues.API_V1_ZA_KYC_ID: ApiV1ZaKycId,
        PathValues.API_V1_KYC_NUBAN: ApiV1KycNuban,
        PathValues.API_V1_KYC_BVN: ApiV1KycBvn,
        PathValues.API_V1_KYC_BVN_BASIC: ApiV1KycBvnBasic,
        PathValues.API_V1_KYC_BVN_FULL: ApiV1KycBvnFull,
        PathValues.API_V1_KYC_NIN: ApiV1KycNin,
        PathValues.API_V1_KYC_VNIN: ApiV1KycVnin,
        PathValues.API_V1_KYC_BVN_ADVANCE: ApiV1KycBvnAdvance,
        PathValues.API_V1_KYC_PHONE_NUMBER_BASIC: ApiV1KycPhoneNumberBasic,
        PathValues.API_V1_KYC_PHONE_NUMBER: ApiV1KycPhoneNumber,
        PathValues.API_V1_KYC_DL: ApiV1KycDl,
        PathValues.API_V1_KYC_PASSPORT: ApiV1KycPassport,
        PathValues.API_V1_KYC_VIN: ApiV1KycVin,
        PathValues.API_V1_KYC_NUBAN_BVN: ApiV1KycNubanBvn,
        PathValues.API_V1_KYC_ADDRESS: ApiV1KycAddress,
        PathValues.API_V1_KYC_ACCOUNTS: ApiV1KycAccounts,
        PathValues.API_V1_ML_LIVENESS: ApiV1MlLiveness,
        PathValues.V1_KYC_BVN_VERIFY: V1KycBvnVerify,
        PathValues.API_V1_KYC_NIN_VERIFY: ApiV1KycNinVerify,
        PathValues.V1_KYC_AGE_VERIFICATION: V1KycAgeVerification,
        PathValues.V1_KYC_BVN: V1KycBvn,
        PathValues.API_V1_KYC_VNIN_VERIFY: ApiV1KycVninVerify,
        PathValues.API_V1_DOCUMENT_ANALYSIS: ApiV1DocumentAnalysis,
        PathValues.API_V1_MESSAGING_SMS: ApiV1MessagingSms,
        PathValues.V1_MESSAGING_SMS_GET_STATUS: V1MessagingSmsGetStatus,
        PathValues.API_V1_MESSAGING_OTP: ApiV1MessagingOtp,
        PathValues.API_V1_MESSAGING_OTP_VALIDATE: ApiV1MessagingOtpValidate,
        PathValues.API_V1_MESSAGING_SENDER_IDS: ApiV1MessagingSenderIds,
        PathValues.API_V1_MESSAGING_SENDER_ID: ApiV1MessagingSenderId,
        PathValues.API_V1_KYC_PHOTOID_VERIFY: ApiV1KycPhotoidVerify,
        PathValues.API_V1_AML_SCREENING_PLATFORM: ApiV1AmlScreeningPlatform,
        PathValues.API_V1_AML_SCREENING_INFO: ApiV1AmlScreeningInfo,
        PathValues.API_V1_FRAUD_IP: ApiV1FraudIp,
        PathValues.API_V1_KYC_EMAIL: ApiV1KycEmail,
        PathValues.API_V1_FRAUD_USER: ApiV1FraudUser,
        PathValues.API_V1_FRAUD_PHONE: ApiV1FraudPhone,
        PathValues.V1_PURCHASE_AIRTIME: V1PurchaseAirtime,
        PathValues.V1_GENERAL_BANKS: V1GeneralBanks,
        PathValues.API_V1_GENERAL_ACCOUNT: ApiV1GeneralAccount,
        PathValues.V1_GENERAL_BIN: V1GeneralBin,
        PathValues.API_V1_BALANCE: ApiV1Balance,
        PathValues.API_V1_WEBHOOK_SUBSCRIBE: ApiV1WebhookSubscribe,
        PathValues.API_V1_WEBHOOK_DELETE: ApiV1WebhookDelete,
        PathValues.API_V1_WEBHOOK_FETCH: ApiV1WebhookFetch,
        PathValues.API_V1_WEBHOOK_NOTIFY: ApiV1WebhookNotify,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V1_KYC_CAC: ApiV1KycCac,
        PathValues.API_V1_KYC_TIN: ApiV1KycTin,
        PathValues.API_V1_KYB_BUSINESS_SEARCH: ApiV1KybBusinessSearch,
        PathValues.API_V1_KYB_BUSINESS_DETAIL: ApiV1KybBusinessDetail,
        PathValues.API_V1_GH_KYC_DL: ApiV1GhKycDl,
        PathValues.API_V1_GH_KYC_PASSPORT: ApiV1GhKycPassport,
        PathValues.API_V1_GH_KYC_SSNIT: ApiV1GhKycSsnit,
        PathValues.API_V1_GH_KYC_VOTER: ApiV1GhKycVoter,
        PathValues.API_V1_UG_KYC_VOTER: ApiV1UgKycVoter,
        PathValues.API_V1_KE_KYC_ID: ApiV1KeKycId,
        PathValues.API_V1_KE_KYC_PASSPORT: ApiV1KeKycPassport,
        PathValues.API_V1_TZ_KYC_NIN: ApiV1TzKycNin,
        PathValues.API_V1_ZW_KYC_NIN: ApiV1ZwKycNin,
        PathValues.API_V1_ZW_KYC_FCB: ApiV1ZwKycFcb,
        PathValues.API_V1_UK_KYC: ApiV1UkKyc,
        PathValues.API_V1_US_KYC: ApiV1UsKyc,
        PathValues.API_V1_CA_KYC: ApiV1CaKyc,
        PathValues.API_V1_ZA_KYC_ID: ApiV1ZaKycId,
        PathValues.API_V1_KYC_NUBAN: ApiV1KycNuban,
        PathValues.API_V1_KYC_BVN: ApiV1KycBvn,
        PathValues.API_V1_KYC_BVN_BASIC: ApiV1KycBvnBasic,
        PathValues.API_V1_KYC_BVN_FULL: ApiV1KycBvnFull,
        PathValues.API_V1_KYC_NIN: ApiV1KycNin,
        PathValues.API_V1_KYC_VNIN: ApiV1KycVnin,
        PathValues.API_V1_KYC_BVN_ADVANCE: ApiV1KycBvnAdvance,
        PathValues.API_V1_KYC_PHONE_NUMBER_BASIC: ApiV1KycPhoneNumberBasic,
        PathValues.API_V1_KYC_PHONE_NUMBER: ApiV1KycPhoneNumber,
        PathValues.API_V1_KYC_DL: ApiV1KycDl,
        PathValues.API_V1_KYC_PASSPORT: ApiV1KycPassport,
        PathValues.API_V1_KYC_VIN: ApiV1KycVin,
        PathValues.API_V1_KYC_NUBAN_BVN: ApiV1KycNubanBvn,
        PathValues.API_V1_KYC_ADDRESS: ApiV1KycAddress,
        PathValues.API_V1_KYC_ACCOUNTS: ApiV1KycAccounts,
        PathValues.API_V1_ML_LIVENESS: ApiV1MlLiveness,
        PathValues.V1_KYC_BVN_VERIFY: V1KycBvnVerify,
        PathValues.API_V1_KYC_NIN_VERIFY: ApiV1KycNinVerify,
        PathValues.V1_KYC_AGE_VERIFICATION: V1KycAgeVerification,
        PathValues.V1_KYC_BVN: V1KycBvn,
        PathValues.API_V1_KYC_VNIN_VERIFY: ApiV1KycVninVerify,
        PathValues.API_V1_DOCUMENT_ANALYSIS: ApiV1DocumentAnalysis,
        PathValues.API_V1_MESSAGING_SMS: ApiV1MessagingSms,
        PathValues.V1_MESSAGING_SMS_GET_STATUS: V1MessagingSmsGetStatus,
        PathValues.API_V1_MESSAGING_OTP: ApiV1MessagingOtp,
        PathValues.API_V1_MESSAGING_OTP_VALIDATE: ApiV1MessagingOtpValidate,
        PathValues.API_V1_MESSAGING_SENDER_IDS: ApiV1MessagingSenderIds,
        PathValues.API_V1_MESSAGING_SENDER_ID: ApiV1MessagingSenderId,
        PathValues.API_V1_KYC_PHOTOID_VERIFY: ApiV1KycPhotoidVerify,
        PathValues.API_V1_AML_SCREENING_PLATFORM: ApiV1AmlScreeningPlatform,
        PathValues.API_V1_AML_SCREENING_INFO: ApiV1AmlScreeningInfo,
        PathValues.API_V1_FRAUD_IP: ApiV1FraudIp,
        PathValues.API_V1_KYC_EMAIL: ApiV1KycEmail,
        PathValues.API_V1_FRAUD_USER: ApiV1FraudUser,
        PathValues.API_V1_FRAUD_PHONE: ApiV1FraudPhone,
        PathValues.V1_PURCHASE_AIRTIME: V1PurchaseAirtime,
        PathValues.V1_GENERAL_BANKS: V1GeneralBanks,
        PathValues.API_V1_GENERAL_ACCOUNT: ApiV1GeneralAccount,
        PathValues.V1_GENERAL_BIN: V1GeneralBin,
        PathValues.API_V1_BALANCE: ApiV1Balance,
        PathValues.API_V1_WEBHOOK_SUBSCRIBE: ApiV1WebhookSubscribe,
        PathValues.API_V1_WEBHOOK_DELETE: ApiV1WebhookDelete,
        PathValues.API_V1_WEBHOOK_FETCH: ApiV1WebhookFetch,
        PathValues.API_V1_WEBHOOK_NOTIFY: ApiV1WebhookNotify,
    }
)

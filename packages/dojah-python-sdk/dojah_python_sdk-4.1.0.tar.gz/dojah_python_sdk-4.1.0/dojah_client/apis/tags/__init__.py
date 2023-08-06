# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from dojah_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    NIGERIA_KYC = "Nigeria KYC"
    KYC = "KYC"
    AUTHENTICATION = "Authentication"
    VERIFICATIONS = "Verifications"
    KYB = "KYB"
    GH_KYC = "GH KYC"
    FRAUD = "Fraud"
    WEB_HOOKS = "WebHooks"
    GLOBAL_KYC = "Global KYC"
    GENERAL = "General"
    KE_KYC = "KE KYC"
    ZW_KYC = "ZW KYC"
    AML = "AML"
    SERVICES = "Services"
    UG_KYC = "UG KYC"
    TZ_KYC = "TZ KYC"
    ZAF_KYC = "ZAF KYC"
    DOCUMENT_ANALYSIS = "Document Analysis"
    ML = "ML"
    PURCHASE = "Purchase"

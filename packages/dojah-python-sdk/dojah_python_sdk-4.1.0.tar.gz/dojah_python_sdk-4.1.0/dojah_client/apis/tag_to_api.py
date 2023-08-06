import typing_extensions

from dojah_client.apis.tags import TagValues
from dojah_client.apis.tags.nigeria_kyc_api import NigeriaKYCApi
from dojah_client.apis.tags.kyc_api import KYCApi
from dojah_client.apis.tags.authentication_api import AuthenticationApi
from dojah_client.apis.tags.verifications_api import VerificationsApi
from dojah_client.apis.tags.kyb_api import KYBApi
from dojah_client.apis.tags.ghkyc_api import GHKYCApi
from dojah_client.apis.tags.fraud_api import FraudApi
from dojah_client.apis.tags.web_hooks_api import WebHooksApi
from dojah_client.apis.tags.global_kyc_api import GlobalKYCApi
from dojah_client.apis.tags.general_api import GeneralApi
from dojah_client.apis.tags.kekyc_api import KEKYCApi
from dojah_client.apis.tags.zwkyc_api import ZWKYCApi
from dojah_client.apis.tags.aml_api import AMLApi
from dojah_client.apis.tags.services_api import ServicesApi
from dojah_client.apis.tags.ugkyc_api import UGKYCApi
from dojah_client.apis.tags.tzkyc_api import TZKYCApi
from dojah_client.apis.tags.zafkyc_api import ZAFKYCApi
from dojah_client.apis.tags.document_analysis_api import DocumentAnalysisApi
from dojah_client.apis.tags.ml_api import MLApi
from dojah_client.apis.tags.purchase_api import PurchaseApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.NIGERIA_KYC: NigeriaKYCApi,
        TagValues.KYC: KYCApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.VERIFICATIONS: VerificationsApi,
        TagValues.KYB: KYBApi,
        TagValues.GH_KYC: GHKYCApi,
        TagValues.FRAUD: FraudApi,
        TagValues.WEB_HOOKS: WebHooksApi,
        TagValues.GLOBAL_KYC: GlobalKYCApi,
        TagValues.GENERAL: GeneralApi,
        TagValues.KE_KYC: KEKYCApi,
        TagValues.ZW_KYC: ZWKYCApi,
        TagValues.AML: AMLApi,
        TagValues.SERVICES: ServicesApi,
        TagValues.UG_KYC: UGKYCApi,
        TagValues.TZ_KYC: TZKYCApi,
        TagValues.ZAF_KYC: ZAFKYCApi,
        TagValues.DOCUMENT_ANALYSIS: DocumentAnalysisApi,
        TagValues.ML: MLApi,
        TagValues.PURCHASE: PurchaseApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.NIGERIA_KYC: NigeriaKYCApi,
        TagValues.KYC: KYCApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.VERIFICATIONS: VerificationsApi,
        TagValues.KYB: KYBApi,
        TagValues.GH_KYC: GHKYCApi,
        TagValues.FRAUD: FraudApi,
        TagValues.WEB_HOOKS: WebHooksApi,
        TagValues.GLOBAL_KYC: GlobalKYCApi,
        TagValues.GENERAL: GeneralApi,
        TagValues.KE_KYC: KEKYCApi,
        TagValues.ZW_KYC: ZWKYCApi,
        TagValues.AML: AMLApi,
        TagValues.SERVICES: ServicesApi,
        TagValues.UG_KYC: UGKYCApi,
        TagValues.TZ_KYC: TZKYCApi,
        TagValues.ZAF_KYC: ZAFKYCApi,
        TagValues.DOCUMENT_ANALYSIS: DocumentAnalysisApi,
        TagValues.ML: MLApi,
        TagValues.PURCHASE: PurchaseApi,
    }
)

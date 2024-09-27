from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, Field


class HeaderModel(BaseModel):
    method: Annotated[str | None, Field(alias=':method')]
    authority: Annotated[str | None, Field(alias=':authority')]
    scheme: Annotated[str | None, Field(alias=':scheme')]
    path: Annotated[str | None, Field(alias=':path')]
    sec_ch_ua: Annotated[str | None, Field(alias='sec-ch-ua')]
    sec_ch_ua_mobile: Annotated[str | None, Field(alias='sec-ch-ua-mobile')]
    sec_ch_ua_platform: Annotated[str | None, Field(alias='sec-ch-ua-platform')]
    upgrade_insecure_requests: Annotated[str | None, Field(alias='upgrade-insecure-requests')]
    user_agent: Annotated[str | None, Field(alias='user-agent')]
    accept: str | None
    sec_fetch_site: Annotated[str | None, Field(alias='sec-fetch-site')]
    sec_fetch_mode: Annotated[str | None, Field(alias='sec-fetch-mode')]
    sec_fetch_dest: Annotated[str | None, Field(alias='sec-fetch-dest')]
    referer: str | None
    accept_encoding: Annotated[str | None, Field(alias='accept-encoding')]
    accept_language: Annotated[str | None, Field(alias='accept-language')]
    cookie: str | None


class RequestFingerprintModel(BaseModel):
    headers: HeaderModel
    http_version: Annotated[str | None, Field(alias='httpVersion')]
    tls_version: Annotated[str | None, Field(alias='tlsVersion')]
    tls_name: Annotated[str | None, Field(alias='tlsName')]
    tls_standard_name: Annotated[str | None, Field(alias='tlsStandardName')]


class BrandModel(BaseModel):
    brand: str
    version: str


class UserAgentDataModel(BaseModel):
    brands: list[BrandModel]
    mobile: bool
    platform: str | None
    architecture: str | None
    bitness: str | None
    model: str | None
    platform_version: Annotated[str | None, Field(alias='platformVersion')]
    ua_full_version: Annotated[str | None, Field(alias='uaFullVersion')]


class ExtraPropertiesModel(BaseModel):
    vendor_flavors: Annotated[list[str] | None, Field(alias='vendorFlavors')]
    is_bluetooth_supported: Annotated[bool | None, Field(alias='isBluetoothSupported')]
    global_privacy_control: Annotated[bool | None, Field(alias='globalPrivacyControl')]
    pdf_viewer_enabled: Annotated[bool | None, Field(alias='pdfViewerEnabled')]
    installed_apps: Annotated[list[str] | None, Field(alias='installedApps')]


class SpeakerModel(BaseModel):
    device_id: Annotated[str | None, Field(alias='deviceId')]
    kind: str | None
    label: str | None
    group_id: Annotated[str | None, Field(alias='groupId')]


class MicModel(BaseModel):
    device_id: Annotated[str | None, Field(alias='deviceId')]
    kind: str | None
    label: str | None
    group_id: Annotated[str | None, Field(alias='groupId')]


class WebcamModel(BaseModel):
    device_id: Annotated[str | None, Field(alias='deviceId')]
    kind: str | None
    label: str | None
    group_id: Annotated[str | None, Field(alias='groupId')]


class MultimediaDevicesModel(BaseModel):
    speakers: list[SpeakerModel] | None
    micros: list[MicModel] | None
    webcams: list[WebcamModel] | None


class BatteryModel(BaseModel):
    charging: bool | None
    charging_time: Annotated[float | None, Field(alias='chargingTime')]
    discharging_time: Annotated[float | None, Field(alias='dischargingTime')]
    level: float | None


class AudioCodecsModel(BaseModel):
    ogg: str | None
    mp3: str | None
    wav: str | None
    m4a: str | None
    aac: str | None


class VideoCodecsModel(BaseModel):
    ogg: str | None
    h264: str | None
    webm: str | None


class ScreenModel(BaseModel):
    avail_height: Annotated[int | None, Field(alias='availHeight')]
    avail_width: Annotated[int | None, Field(alias='availWidth')]
    pixel_depth: Annotated[int | None, Field(alias='pixelDepth')]
    height: int | None
    width: int | None
    avail_top: Annotated[int | None, Field(alias='availTop')]
    avail_left: Annotated[int | None, Field(alias='availLeft')]
    color_depth: Annotated[int | None, Field(alias='colorDepth')]
    inner_height: Annotated[int | None, Field(alias='innerHeight')]
    outer_height: Annotated[int | None, Field(alias='outerHeight')]
    outer_width: Annotated[int | None, Field(alias='outerWidth')]
    inner_width: Annotated[int | None, Field(alias='innerWidth')]
    screen_x: Annotated[int | None, Field(alias='screenX')]
    page_x_offset: Annotated[int | None, Field(alias='pageXOffset')]
    page_y_offset: Annotated[int | None, Field(alias='pageYOffset')]
    device_pixel_ratio: Annotated[float | None, Field(alias='devicePixelRatio')]
    client_width: Annotated[int | None, Field(alias='clientWidth')]
    client_height: Annotated[int | None, Field(alias='clientHeight')]
    has_hdr: Annotated[bool | None, Field(alias='hasHDR')]


class PluginMimeTypeModel(BaseModel):
    type: str
    suffixes: str


class PluginModel(BaseModel):
    name: str
    description: str
    mime_types: Annotated[list[PluginMimeTypeModel], Field(alias='mimeTypes')]


class VideoCardModel(BaseModel):
    vendor: str | None
    renderer: str | None


class BrowserFingerprintModel(BaseModel):
    language: str | None
    oscpu: str | None
    do_not_track: Annotated[str | None, Field(alias='doNotTrack')]
    product: str | None
    vendor_sub: Annotated[str | None, Field(alias='vendorSub')]
    app_code_name: Annotated[str | None, Field(alias='appCodeName')]
    app_name: Annotated[str | None, Field(alias='appName')]
    app_version: Annotated[str | None, Field(alias='appVersion')]
    webdriver: bool | None
    max_touch_points: Annotated[int | None, Field(alias='maxTouchPoints')]
    user_agent_data: Annotated[UserAgentDataModel, Field(alias='userAgentData')]
    extra_properties: Annotated[ExtraPropertiesModel, Field(alias='extraProperties')]
    user_agent: str | None
    platform: str | None
    languages: list[str] | None
    video_card: Annotated[VideoCardModel, Field(alias='videoCard')]
    multimedia_devices: Annotated[MultimediaDevicesModel, Field(alias='multimediaDevices')]
    product_sub: Annotated[str | None, Field(alias='productSub')]
    battery: BatteryModel
    device_memory: Annotated[int | None, Field(alias='deviceMemory')]
    audio_codecs: Annotated[AudioCodecsModel, Field(alias='audioCodecs')]
    video_codecs: Annotated[VideoCodecsModel, Field(alias='videoCodecs')]
    screen: ScreenModel
    hardware_concurrency: Annotated[int | None, Field(alias='hardwareConcurrency')]
    plugins: list[PluginModel]
    mime_types: Annotated[list[str], Field(alias='mimeTypes')]
    fonts: list[str] | None
    vendor: str | None


class FingerprintModel(BaseModel):
    id: str
    collected_at: Annotated[str, Field(alias='collectedAt')]
    request_fingerprint: Annotated[RequestFingerprintModel, Field(alias='requestFingerprint')]
    browser_fingerprint: Annotated[BrowserFingerprintModel, Field(alias='browserFingerprint')]

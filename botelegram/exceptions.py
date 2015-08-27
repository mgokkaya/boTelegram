# -*- coding: utf-8 -*-
class BaseError(Exception):
    """Bu sınıf tüm hatalara aittir"""
    def __init__(self, *args, **kwargs):
        super(BaseError, self).__init__(*args, **kwargs)


class TokenError(BaseError):
    """TokenError"""
    def __init__(self):
        super(TokenError, self).__init__("Token değeri kullanılamıyor")


class OfsetError(BaseError):
    """OfsetError"""
    def __init__(self):
        super(OfsetError, self).__init__("Verdiğiniz tip uygun değildir")


class LimitError(BaseError):
    """LimitError"""
    def __init__(self):
        super(LimitError, self).__init__("Verdiğiniz tip uygun değildir")


class TimeOutError(BaseError):
    """TimeOutError"""
    def __init__(self):
        super(TimeOutError, self).__init__("Verdiğiniz tip uygun değildir")


class ChatIdError(BaseError):
    """ChatIdError"""
    def __init__(self):
        super(ChatIdError, self).__init__("Verdiğiniz tip uygun değildir")


class TextError(BaseError):
    """TextError"""
    def __init__(self):
        super(TextError, self).__init__("Verdiğiniz tip uygun değildir")


class ReplyMarkupError(BaseError):
    """ReplyMarkupError"""
    def __init__(self):
        super(ReplyMarkupError, self).__init__("Verdiğiniz tip uygun değildir")


class DisableWebPagePreviewError(BaseError):
    """DisableWebPagePreviewError"""
    def __init__(self):
        super(DisableWebPagePreviewError, self).__init__("Verdiğiniz tip uygun değildir")


class ReplyMarkupError(BaseError):
    """ReplyMarkupError"""
    def __init__(self):
        super(ReplyMarkupError, self).__init__("Verdiğiniz tip uygun değildir")


class FromChatIdError(BaseError):
    """FromChatIdError"""
    def __init__(self):
        super(FromChatIdError, self).__init__("Verdiğiniz tip uygun değildir")


class MessageIdError(BaseError):
    """MessageIdError"""
    def __init__(self):
        super(MessageIdError, self).__init__("Verdiğiniz tip uygun değildir")


class CaptionError(BaseError):
    """CaptionError"""
    def __init__(self):
        super(CaptionError, self).__init__("Verdiğiniz tip uygun değildir")


class FileLocationError(BaseError):
    """FileLocationError"""
    def __init__(self):
        super(FileLocationError, self).__init__("Dosya bulunamadı")


class UserIdError(BaseError):
    """UserIdError"""
    def __init__(self):
        super(UserIdError, self).__init__("Verdiğiniz tip uygun değildir")


class ActionError(BaseError):
    """ActionError"""
    def __init__(self):
        super(ActionError, self).__init__("Verdiğiniz tip uygun değildir")


class LatitudeError(BaseError):
    """LatitudeError"""
    def __init__(self):
        super(LatitudeError, self).__init__("Verdiğiniz tip uygun değildir")


class LongitudeError(BaseError):
    """LongitudeError"""
    def __init__(self):
        super(LongitudeError, self).__init__("Verdiğiniz tip uygun değildir")


class VideoError(BaseError):
    """VideoError"""
    def __init__(self):
        super(VideoError, self).__init__("Video Bulunamadı")


class StickerError(BaseError):
    """StickerError"""
    def __init__(self):
        super(StickerError, self).__init__("Sticker dosyası bulunamadı")


class DocumentError(BaseError):
    """DocumentError"""
    def __init__(self):
        super(DocumentError, self).__init__("Döküman bulunamadı")


class AudioError(BaseError):
    """AudioError"""
    def __init__(self):
        super(AudioError, self).__init__("Ses dosyası bulunamadı")


class PhotoError(BaseError):
    """PhotoError"""
    def __init__(self):
        super(PhotoError, self).__init__("Resim dosyası bulunamadı")


class LatitudeBettwenError(BaseError):
    """LatitudeBettwenError"""
    def __init__(self):
        super(LatitudeBettwenError, self).__init__("Verdiğiniz değer 1-3 aralığında değildir")


class LongitudeBettwenError(BaseError):
    """LongitudeBettwenError"""
    def __init__(self):
        super(LongitudeBettwenError, self).__init__("Verdiğiniz değer 1-3 aralığında değildir")

class RequestsConnectionError(object):
    """RequestsConnectionError"""
    def __init__(self):
        super(RequestsConnectionError, self).__init__("İntert bağlantınızı kontrol ediniz")

class UnauthorizedAccessError(object):
    """RequestsConnectionError"""
    def __init__(self):
        super(UnauthorizedAccessError, self).__init__("Hata")

class UnknownError(object):
    """RequestsConnectionError"""
    def __init__(self):
        super(UnknownError, self).__init__("Hata")

class RequestsHTTPError(object):
    """RequestsHTTPError"""
    def __init__(self):
        super(RequestsHTTPError, self).__init__("RequestsHTTPError")

class RequestsURLRequiredError(object):
    """RequestsHTTPError"""
    def __init__(self):
        super(RequestsURLRequiredError, self).__init__("RequestsURLRequiredError")

class RequestsTooManyRedirectsError(object):
    """RequestsTooManyRedirectsError"""
    def __init__(self):
        super(RequestsTooManyRedirectsError, self).__init__("RequestsTooManyRedirectsError")

class RequestsConnectTimeoutError(object):
    """RequestsConnectTimeoutError"""
    def __init__(self):
        super(RequestsConnectTimeoutError, self).__init__("RequestsConnectTimeoutError")

class RequestsReadTimeoutError(object):
    """RequestsReadTimeoutError"""
    def __init__(self):
        super(RequestsReadTimeoutError, self).__init__("RequestsReadTimeoutError")

class RequestsTimeoutError(object):
    """RequestsTimeoutError"""
    def __init__(self):
        super(RequestsTimeoutError, self).__init__("RequestsTimeoutError")

class RequestsExceptionError(object):
    """RequestsHTTPError"""
    def __init__(self):
        super(RequestsHTTPError, self).__init__("RequestsHTTPError")
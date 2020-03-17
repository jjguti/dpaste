from django.conf import settings
from django.conf.urls import include, url

url_prefix = getattr(settings, "URL_PREFIX", "")

urlpatterns = [
    url(r"^%s" % url_prefix, include("dpaste.urls.dpaste_api")),
    url(r"^%s" % url_prefix, include("dpaste.urls.dpaste")),
    url(r"^%si18n/" % url_prefix, include("django.conf.urls.i18n")),
]

# Custom error handlers which load `dpaste/<code>.html` instead of `<code>.html`
handler404 = "dpaste.views.page_not_found"
handler500 = "dpaste.views.server_error"

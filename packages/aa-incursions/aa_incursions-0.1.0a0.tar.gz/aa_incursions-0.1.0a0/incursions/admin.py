from django.contrib import admin

from allianceauth.services.hooks import get_extension_logger

from .models import Incursion, IncursionsConfig, Webhook

logger = get_extension_logger(__name__)


@admin.register(IncursionsConfig)
class IncursionsConfigAdmin(admin.ModelAdmin):
    filter_horizontal = ["status_webhooks", ]


@admin.register(Incursion)
class IncursionAdmin(admin.ModelAdmin):
    list_display = ["constellation", "state"]
    list_filter = ["state", ]


@admin.register(Webhook)
class WebhookAdmin(admin.ModelAdmin):
    list_display = ("url", )

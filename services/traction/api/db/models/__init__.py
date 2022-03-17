# Import all the models, so that Base has them before being imported by Alembic

from api.db.models.base import BaseTable  # noqa: F401
from api.db.models.tenant import Tenant  # noqa: F401
from api.db.models.tenant_webhook import TenantWebhook  # noqa: F401
from api.db.models.tenant_webhook_msg import TenantWebhookMsg  # noqa: F401
from api.db.models.catalog import Operation  # noqa: F401

__all__ = ["BaseTable", "Operation", "Tenant", "TenantWebhook", "TenantWebhookMsg"]

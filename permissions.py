"""Explicit permission gate; unknown roles cannot export."""
def can_export(role, tenant_matches):
    return tenant_matches is True and role in {"owner", "analyst"}

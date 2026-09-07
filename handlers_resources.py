"""Resource handlers for Tealium Connector."""
from __future__ import annotations
from typing import Any
from imperal_sdk import ActionResult
from app import chat
from schemas import (
    ListAudienceParams, GetAudienceParams,
    AudienceRecord, AudienceList, AuditHealthReport, ConnectionIdParams
)
from handlers_connection import resolve_client

@chat.function("list_audiences", "List audiences in Tealium.", action_type="read", chain_callable=True, event="tealium-connector.list_audiences", effects=["read:audiences"], data_model=AudienceList)
async def list_audiences(params: ListAudienceParams, ctx) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        raw_items = await client.list_audiences(limit=params.limit)
        items = []
        for r in raw_items:
            rid = str(r.get("id") or r.get("key") or r.get("uuid") or "unknown")
            rname = r.get("name") or r.get("title") or r.get("label") or rid
            items.append({"id": rid, "name": rname, "status": r.get("status"), "created_at": r.get("createdAt") or r.get("created_at"), "raw": r})
        return ActionResult.success({"audiences": items, "total": len(items)}, summary=f"Found {len(items)} audiences.")
    except Exception as e:
        return ActionResult.error(f"Error listing audiences: {e}")

@chat.function("get_audience", "Get details of one Audience in Tealium.", action_type="read", chain_callable=True, event="tealium-connector.get_audience", effects=["read:audience"], data_model=AudienceRecord)
async def get_audience(params: GetAudienceParams, ctx) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        r = await client.get_audience(params.audience_id)
        rid = str(r.get("id") or params.audience_id)
        rname = r.get("name") or r.get("title") or rid
        return ActionResult.success({"id": rid, "name": rname, "status": r.get("status"), "created_at": r.get("createdAt") or r.get("created_at"), "raw": r}, summary=f"Retrieved Audience {rid}.")
    except Exception as e:
        return ActionResult.error(f"Error retrieving Audience: {e}")

@chat.function("audit_audience_health", "Audit health of Tealium audiences and connectivity.", action_type="read", chain_callable=True, event="tealium-connector.audit_audience_health", effects=["read:audit"], data_model=AuditHealthReport)
async def audit_audience_health(params: ConnectionIdParams, ctx) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        items = await client.list_audiences(limit=50)
        return ActionResult.success({
            "healthy": True,
            "total_audiences": len(items),
            "details": {"sample_count": len(items)},
            "summary": f"Tealium healthy. Sampled {len(items)} audiences."
        }, summary=f"Tealium health check passed with {len(items)} audiences.")
    except Exception as e:
        return ActionResult.error(f"Error auditing Tealium health: {e}")

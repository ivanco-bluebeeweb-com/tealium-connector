"""Pydantic schemas for Tealium Connector."""
from __future__ import annotations
from typing import Any, Optional, List, Dict
from pydantic import BaseModel, Field

class NoParams(BaseModel):
    """Empty parameters model."""
    pass

class ConnectParams(BaseModel):
    label: str = Field(default="", description="Friendly connection label, e.g. Primary Tealium.")
    api_token: str = Field(description="Access Token / API Key")
    base_url: str = Field(default="https://api.tealiumiq.com/v2", description="Tealium API base URL.")

class ConnectionIdParams(BaseModel):
    connection_id: str = Field(default="", description="Connection identifier (empty uses active connection).")

class ConnectionRecord(BaseModel):
    id: str
    label: str
    masked_key: str
    base_url: str
    is_active: bool

class ConnectionList(BaseModel):
    connections: list[ConnectionRecord]
    total: int

class DeleteResult(BaseModel):
    success: bool
    message: str

class AudienceRecord(BaseModel):
    id: str
    name: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None
    raw: Dict[str, Any] = Field(default_factory=dict)

class AudienceList(BaseModel):
    audiences: list[AudienceRecord]
    total: int

class ListAudienceParams(BaseModel):
    connection_id: str = Field(default="", description="Optional connection ID.")
    limit: int = Field(default=20, ge=1, le=100, description="Max records to return.")

class GetAudienceParams(BaseModel):
    connection_id: str = Field(default="", description="Optional connection ID.")
    audience_id: str = Field(description="Tealium Audience ID.")

class AuditHealthReport(BaseModel):
    healthy: bool
    total_audiences: int
    details: Dict[str, Any] = Field(default_factory=dict)
    summary: str

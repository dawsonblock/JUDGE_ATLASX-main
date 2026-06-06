"""add review action log unique constraint

Add a unique constraint on review_action_logs(review_item_id, actor, action)
to prevent duplicate audit-log entries for the same actor + action on a
review item while still supporting legitimate re-reviews by different actors.

Revision ID: 20260604_0002
Revises: 20260604_0001
Create Date: 2026-06-04
"""

from __future__ import annotations

from alembic import op


revision = "20260604_0002"
down_revision = "20260604_0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint(
        "uq_review_action_log_item_actor_action",
        "review_action_logs",
        ["review_item_id", "actor", "action"],
    )


def downgrade() -> None:
    op.drop_constraint(
        "uq_review_action_log_item_actor_action",
        "review_action_logs",
        type_="unique",
    )

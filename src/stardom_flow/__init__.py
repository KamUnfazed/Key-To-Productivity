# Stardom Flow Module
# This module will handle the AI-driven daily routine optimizer.

from .ai_coach import AICoach


def initialize_stardom_flow():
    """Initialize the Stardom Flow AI module."""
    coach = AICoach()
    return coach


__all__ = ['AICoach', 'initialize_stardom_flow']
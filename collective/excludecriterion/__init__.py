# -*- extra stuff goes here -*-
import logging
from zope.i18nmessageid import MessageFactory
excludeCriterionMessageFactory = MessageFactory('collective.excludecriterion')
logger = logging.getLogger("collective.periodcriterion")


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

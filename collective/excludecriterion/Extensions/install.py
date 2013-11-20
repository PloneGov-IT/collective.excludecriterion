from collective.excludecriterion import logger


def uninstall(portal, reinstall=False):
    setup_tool = portal.portal_setup
    setup_tool.runAllImportStepsFromProfile('profile-collective.excludecriterion:uninstall')
    logger.info("collective.excludecriterion has been removed")

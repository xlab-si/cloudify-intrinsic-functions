from cloudify import ctx

ctx.logger.info("Creating node of type B")

props = ctx.node.properties
ctx.logger.info("property_b1 = {}".format(props["property_b1"]))
ctx.logger.info("property_b2 = {}".format(props["property_b2"]))

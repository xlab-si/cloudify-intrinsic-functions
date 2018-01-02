from cloudify import ctx
from cloudify.state import ctx_parameters as inputs

ctx.logger.info("Creating node of type B")

props = ctx.node.properties
ctx.logger.info("property_b1 = {}".format(props["property_b1"]))
ctx.logger.info("input_b2 = {}".format(inputs["input_b2"]))

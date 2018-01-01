from cloudify import ctx

ctx.logger.info("Creating node of type A")
ctx.instance.runtime_properties["attribute_a"] = "attribute_a_value"

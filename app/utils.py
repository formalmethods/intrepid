def typename_to_type(ctx, typename):
    if typename == 'bool':
        return ctx.mk_boolean_type()
    elif typename == 'int8':
        return ctx.mk_int8_type()
    elif typename == 'int16':
        return ctx.mk_int16_type()
    elif typename == 'int32':
        return ctx.mk_int32_type()
    elif typename == 'uint8':
        return ctx.mk_uint8_type()
    elif typename == 'uint16':
        return ctx.mk_uint16_type()
    elif typename == 'uint32':
        return ctx.mk_uint32_type()
    elif typename == 'real':
        return ctx.mk_real_type()
    elif typename == 'float16':
        return ctx.mk_float16_type()
    elif typename == 'float32':
        return ctx.mk_float32_type()
    elif typename == 'float64':
        return ctx.mk_float64_type()
    raise RuntimeError('Unhandled type {}'.format(typename))

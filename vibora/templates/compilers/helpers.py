from inspect import isasyncgen, isasyncgenfunction


async def smart_iter(element):
    if isasyncgen(element) or isasyncgenfunction(element):
        async for x in element:
            yield x
    else:
        for x in element:
            yield x

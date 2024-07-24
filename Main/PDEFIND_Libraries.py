def fnc_PDEFIND_Libraries(PolyPower):


    if PolyPower == 3:

        library_functions = [
            lambda x: x,
            lambda x: x * x * x,
            lambda x, y: x * x * y,
            lambda x, y: x * y * y,
        ]

        library_function_names = [
            lambda x: x,
            lambda x: x + x + x,
            lambda x, y: x + x + y,
            lambda x, y: x + y + y,
        ]


    if PolyPower == 5:

        library_functions = [
            lambda x: x,
            lambda x: x * x * x,
            lambda x, y: x * x * y,
            lambda x, y: x * y * y,
            lambda x: x * x * x * x * x,
            lambda x, y: x * x * x * x * y,
            lambda x, y: x * x * x * y * y,
            lambda x, y: x * x * y * y * y,
            lambda x, y: x * y * y * y * y,
        ]

        library_function_names = [
            lambda x: x,
            lambda x: x + x + x,
            lambda x, y: x + y + y,
            lambda x, y: x + x + y,
            lambda x: x + x + x + x + x,
            lambda x, y: x + x + x + x + y,
            lambda x, y: x + x + x + y + y,
            lambda x, y: x + x + y + y + y,
            lambda x, y: x + y + y + y + y,
        ]


    if PolyPower == 23:

        library_functions = [
            lambda x: x,
            lambda x: x * x,
            lambda x, y: x * y,
            lambda x: x * x * x,
            lambda x, y: x * x * y,
            lambda x, y: x * y * y,
        ]

        library_function_names = [
            lambda x: x,
            lambda x: x + x,
            lambda x, y: x + y,
            lambda x: x + x + x,
            lambda x, y: x + x + y,
            lambda x, y: x + y + y,
        ]

        
    if PolyPower == 2345:

        library_functions = [
            lambda x: x,
            lambda x: x * x,
            lambda x, y: x * y,
            lambda x: x * x * x,
            lambda x, y: x * x * y,
            lambda x, y: x * y * y,
            lambda x: x * x * x * x,
            lambda x, y: x * x * x * y,
            lambda x, y: x * x * y * y,
            lambda x, y: x * y * y * y,
            lambda x: x * x * x * x * x,
            lambda x, y: x * x * x * x * y,
            lambda x, y: x * x * x * y * y,
            lambda x, y: x * x * y * y * y,
            lambda x, y: x * y * y * y * y,
        ]

        library_function_names = [
            lambda x: x,
            lambda x: x + x,
            lambda x, y: x + y,
            lambda x: x + x + x,
            lambda x, y: x + x + y,
            lambda x, y: x + y + y,
            lambda x: x + x + x + x,
            lambda x, y: x + x + x + y,
            lambda x, y: x + x + y + y,
            lambda x, y: x + y + y + y,
            lambda x: x + x + x + x + x,
            lambda x, y: x + x + x + x + y,
            lambda x, y: x + x + x + y + y,
            lambda x, y: x + x + y + y + y,
            lambda x, y: x + y + y + y + y,
        ]


    return library_functions, library_function_names




    
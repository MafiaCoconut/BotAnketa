import logging


def set_func(function, tag, status="info"):
    match status:
        case "info":    logging.info(f"[%s] Вызвана функция: {function}", tag)
        case "debug":   logging.debug(f"[%s] Вызвана функция: {function}", tag)


def set_func_and_person(function, tag, message, status="info"):
    match status:
        case "info":      logging.info(f"[%s] Вызвана функция: ({function}) пользователем: @{message.from_user.username}", tag)
        case "debug":     logging.debug(f"[%s] Вызвана функция: ({function}) пользователем: @{message.from_user.username}", tag)


def set_inside_func(data, function, tag, status="info"):
    match status:
        case "info":  logging.info(f"[%s] [%s]: {data}", tag, function)
        case "debug": logging.debug(f"[%s] [%s]: {data}", tag, function)



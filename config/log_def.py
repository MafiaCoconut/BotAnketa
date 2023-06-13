import logging


def set_func(function, tag, status="info"):
    match status:
        case "info":    logging.info(f"[%s] Вызвана функция: {function}", tag)
        case "debug":   logging.debug(f"[%s] Вызвана функция: {function}", tag)


def set_person_text(tag, message, status="info"):
    match status:
        # case "info":      logging.info(f"[%s] Вызвана функция: ({function}) пользователем: {message.from_user.id}",
        # tag) case "debug":     logging.debug(f"[%s] Вызвана функция: ({function}) пользователем: {
        # message.from_user.id}", tag)
        case "info":     logging.info(f"[%s] |Пользователь: {message.chat.id}|, {message.text}", tag)
        case "debug":     logging.debug(f"[%s] |Пользователь: {message.chat.id}|, {message.text}", tag)


def set_inside_func(data, function, tag, status="info"):
    match status:
        case "info":  logging.info(f"[%s] [%s]: {data}", tag, function)
        case "debug": logging.debug(f"[%s] [%s]: {data}", tag, function)
        case "warning": logging.warning(f"[%s] [%s]: {data}", tag, function)



""" from https://github.com/keithito/tacotron """

import inflect
import re
from vietnam_number import n2w, w2n

_time_re = re.compile(
  r"""\b
  ((0?[0-9])|(1[0-1])|(1[2-9])|(2[0-3]))  # hours
  :
  ([0-5][0-9])                            # minutes
  \s*(a\\.m\\.|am|pm|p\\.m\\.|a\\.m|p\\.m)? # am/pm
  \b""",
  re.IGNORECASE | re.X,
)


def expand_num(num: str) -> str:
    return n2w(num)


def expand_time_vi(match: "re.Match") -> str:
    # process hour
    _hour = match.group(1)
    hour = int(_hour)
    past_noon = hour >= 12
    time = []
    if hour > 12:
        hour -= 12
    elif hour == 0:
        hour = 12
        past_noon = True

    time.append(expand_num(_hour))
    time.append("giờ")

    # process minutes
    _minute = match.group(6)
    minute = int(_minute)
    if minute > 0:
        time.append(expand_num(_minute))
    am_pm = match.group(7)
    if am_pm is None:
        time.append("p m" if past_noon else "a m")
    else:
        time.extend(list(am_pm.replace(".", "")))
    return " ".join(time)


def normalize_time(text: str) -> str:
    return re.sub(_time_re, expand_time_vi, text)
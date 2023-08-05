import os
import io
import inspect
from datetime import datetime
from .colors import Colors
from time import perf_counter
from pathlib import Path

class StartTime:
    perf_counter: float = perf_counter()

def tlog(tags: str, *args, **kwargs):
    debug_tags = os.environ.get("DEBUG", None)
    if debug_tags is None or not tag_match(debug_tags, tags):
        return
    try:
        debug_tags, debug_options = debug_tags.split(":")   
    except ValueError:
        debug_options = ''
    log_message = print_to_string(*args, **kwargs)
    msg_prefix = prefix(debug_options)
    formatted_msg = f"{msg_prefix}{Colors.LIGHT_CYAN}DEBUG " \
        f"[{Colors.BOLD}{tags}] {Colors.LIGHT_WHITE}{log_message}{Colors.END}"
    print(formatted_msg, end="")

def prefix(debug_optons: str) -> str:
    """Return the prefix string for the log message"""
    PREFIX_MAP = { 
        "l": location , 
        "t": time,
        "e": elapsed_time,
        }
    prefix_list = []
    for option in debug_optons:
        prefix_function = PREFIX_MAP[option]
        prefix_list.append(prefix_function())

    prefix_str = ' '.join(prefix_list)
    # Add a space if there is a prefix
    if prefix_str:
        prefix_str = f"{Colors.BROWN}{prefix_str} "
    return prefix_str

def tag_match(source_tags: str , target_tagets: str) -> bool:
    """ Check if any tag in source tags is in target tags"""
    if source_tags == "all" or target_tagets == "all":
        return True
    source_tags_list = source_tags.split(":")
    target_tags_list = target_tagets.split(":")
    for source_tag in source_tags_list:
        if source_tag in target_tags_list:
            return True
    return False    

def print_to_string(*args, **kwargs):
    """Print to a string instead of stdout"""

    output = io.StringIO()
    print(*args, file=output, **kwargs)
    contents = output.getvalue()
    output.close()
    return contents

def location():
    callerframerecord = inspect.stack()[3]
    cwd = Path.cwd()
    filename = callerframerecord.filename.replace(str(cwd), '.')
    return f"{filename}:{callerframerecord.lineno}"

def time():
    return datetime.now().strftime("%H:%M:%S.%f")

def elapsed_time():
    now = perf_counter()
    return f"{now - StartTime.perf_counter:.3f}s"    
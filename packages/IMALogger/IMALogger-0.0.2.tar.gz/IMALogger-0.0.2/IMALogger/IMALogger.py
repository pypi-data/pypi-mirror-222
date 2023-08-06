import datetime
import re

class logging:
    def __init__(self, log_file_path=None, log_to_console=False, log_date_time=False, time_format_24hr=True):
        self.log_file_path = log_file_path
        self.log_to_console = log_to_console
        self.log_date_time = log_date_time
        self.time_format_24hr = time_format_24hr
        self.log_colors = {
            "DEBUG": "\033[94m",    # Blue
            "INFO": "\033[92m",     # Green
            "WARNING": "\033[93m",  # Yellow
            "ERROR": "\033[91m",    # Red
            "CRITICAL": "\033[95m", # Magenta
            "TAG": "\033[90m",      # Gray
            "RESET": "\033[0m",     # Reset color to default
        }

    def _write_to_log_file(self, message):
        if self.log_file_path:
            cleaned_message = self._remove_ansi_escape_codes(message)
            with open(self.log_file_path, 'a') as log_file:
                log_file.write(cleaned_message + '\n')

    def _remove_ansi_escape_codes(self, text):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

    def _get_current_time(self):
        if self.log_date_time:
            now = datetime.datetime.now()
            if self.time_format_24hr:
                time_str = now.strftime("%Y-%m-%d %H:%M:%S")
            else:
                time_str = now.strftime("%Y-%m-%d %I:%M:%S%p")
            return f"[{time_str}] "
        return ""

    def _log_to_console(self, message):
        if self.log_to_console:
            print(message)

    def _log(self, level, tag, message):
        color = self.log_colors.get(level, "")
        log_message = f"{self._get_current_time()}{self.log_colors['TAG']}[{tag}]{self.log_colors['RESET']} {color}{level}{self.log_colors['RESET']}: {message}"
        self._write_to_log_file(log_message)
        self._log_to_console(log_message)

    def debug(self, tag, message):
        self._log("DEBUG", tag, message)

    def info(self, tag, message):
        self._log("INFO", tag, message)

    def warning(self, tag, message):
        self._log("WARNING", tag, message)

    def error(self, tag, message):
        self._log("ERROR", tag, message)

    def critical(self, tag, message):
        self._log("CRITICAL", tag, message)



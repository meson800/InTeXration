import configparser
import os
from intexration import settings


class Build:
    def __init__(self, name, dir, idx, bib):
        self._name = name
        self._dir = dir
        self._idx = idx
        self._bib = bib

    def get_name(self):
        return self._name

    def get_dir(self):
        return self._dir

    def get_idx(self):
        return self._idx + '.idx'

    def get_bib(self):
        return self._bib

    def get_tex(self):
        return self._name + '.tex'

    def get_pdf(self):
        return self._name + '.pdf'

    def get_log(self):
        return self._name + '.log'


class BuildHelper:
    def __init__(self, path):
        self._path = path

    def get_builds(self):
        """Return all builds from the .intexration file."""
        builds = []
        if os.path.exists(self._path):
            parser = configparser.ConfigParser()
            parser.read(self._path)
            for build_name in parser.sections():
                if parser.has_option(build_name, 'dir'):
                    dir = parser[build_name]['dir']
                else:
                    dir = ''
                if parser.has_option(build_name, 'idx'):
                    idx = parser[build_name]['idx']
                else:
                    idx = build_name
                if parser.has_option(build_name, 'bib'):
                    bib = parser[build_name]['bib']
                else:
                    bib = build_name
                builds.append(Build(build_name, dir, idx, bib))
        return builds


class LogHelper:
    def __init__(self, path):
        self._lines = self._read_lines(path)

    @staticmethod
    def _read_lines(path):
        """Read all lines form log file"""
        if not os.path.isfile(path):
            raise RuntimeError("The logfile does not exist")
        log_file = open(path, "r", encoding='latin-1')
        return log_file.readlines()

    def get_warnings(self):
        """Parse warnings from log file."""
        warnings = []
        multi_line_error = False
        for line in self._lines:
            if multi_line_error and line == settings.LOG_NEW_LINE_CHAR:
                multi_line_error = False
            if settings.LOG_WARNING_STRING in line or multi_line_error:
                warnings.append(line)
                multi_line_error = True
        return warnings

    def get_errors(self):
        """Parse errors from logfile."""
        errors = []
        multi_line_error = False
        for line in self._lines:
            if multi_line_error and line == settings.LOG_NEW_LINE_CHAR:
                multi_line_error = False
            if line.startswith(settings.LOG_ERROR_STRING) or multi_line_error:
                errors.append(line.replace(settings.LOG_ERROR_STRING, ""))
                multi_line_error = True
        return errors

    def get_all(self):
        return self._lines
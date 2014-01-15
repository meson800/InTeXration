import os
import errno
import subprocess
import sys


class InTeXrationTask:

    def __init__(self, url, repository, commit):
        self._url = url
        self._repository = self._convert(repository)
        self._commit = commit
        self._build_dir = self._create_dir('build', commit)
        self._output_dir = self._create_dir('out')

    def _create_dir(self, prefix, suffix=''):
        path = os.path.join(os.getcwdu(), prefix, self._repository, suffix)
        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        return path

    @staticmethod
    def _convert(url):
        if url.startswith('https://'):
            return url + '.git'
        return url

    def _clone(self):
        if subprocess.call(['git', 'clone', self._url, self._build_dir]) != 0:
            raise RuntimeError('git clone failed!')

    def _compile(self, file):
        input_path = os.path.join(self._build_dir, file)
        output_path = self._build_dir
        if subprocess.call(['pdflatex', '-interaction=batchmode', '-aux-directory=' + output_path,
                            '-output-directory=' + output_path, input_path]) != 0:
            raise RuntimeError('pdflatex compilation failed!')

    def run(self):
        self._clone()
        self._compile('main.tex')

def error(*objs):
    print("ERROR: ", *objs, end='\n', file=sys.stderr)

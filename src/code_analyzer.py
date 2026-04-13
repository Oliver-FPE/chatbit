import os
import subprocess
import json

class CodeAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.language = self.detect_language()

    def detect_language(self):
        _, ext = os.path.splitext(self.file_path)
        languages = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.cpp': 'C++',
            '.c': 'C',
            '.lua': 'Lua'
        }
        return languages.get(ext, 'Unknown')

    def syntax_check(self):
        if self.language == 'Python':
            return self.run_python_check()
        elif self.language == 'JavaScript':
            return self.run_js_check()
        elif self.language == 'C++':
            return self.run_cpp_check()
        elif self.language == 'C':
            return self.run_c_check()
        elif self.language == 'Lua':
            return self.run_lua_check()
        else:
            return 'Unsupported language for syntax checking.'

    def run_python_check(self):
        result = subprocess.run(['flake8', self.file_path], capture_output=True, text=True)
        return result.stdout or 'No syntax errors.'

    def run_js_check(self):
        result = subprocess.run(['eslint', self.file_path], capture_output=True, text=True)
        return result.stdout or 'No syntax errors.'

    def run_cpp_check(self):
        result = subprocess.run(['g++', '-fsyntax-only', self.file_path], capture_output=True, text=True)
        return result.stdout or 'No syntax errors.'

    def run_c_check(self):
        result = subprocess.run(['gcc', '-fsyntax-only', self.file_path], capture_output=True, text=True)
        return result.stdout or 'No syntax errors.'

    def run_lua_check(self):
        result = subprocess.run(['luacheck', self.file_path], capture_output=True, text=True)
        return result.stdout or 'No syntax errors.'

# Example usage
# analyzer = CodeAnalyzer('path_to_your_code_file')
# print(analyzer.syntax_check())

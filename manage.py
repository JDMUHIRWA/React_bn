#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


from django.core.management import execute_from_command_line
import os

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_bn.settings')
    try:
        # Rest of the code...
if __name__ == '__main__':
    # Indented block of code
    print("This script is being run directly")

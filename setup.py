from setuptools import setup, find_packages
import os

# Read dependencies from the adapters/mcp requirements if desired, 
# but for a unified package, we explicitly array them here.
install_requires = [
    'pydantic>=2.0.0',
    'pyyaml>=6.0.0',
    'jsonschema>=4.0.0',
    'mcp>=1.0.0',
]

setup(
    name='big4bot',
    version='0.2.0',
    description='Big4Bot Consulting Methodology Runtime for AI Agents',
    author='Big4Bot Open Source',
    # Maps the 'big4bot' namespace to the local 'adapters' directory.
    package_dir={'big4bot': 'adapters'},
    packages=['big4bot', 'big4bot.shared', 'big4bot.mcp', 'big4bot.openai', 'big4bot.anthropic', 'big4bot.gemini', 'big4bot.gemini.example', 'big4bot.openai.example', 'big4bot.anthropic.example'],
    install_requires=install_requires,
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.10',
    ],
)

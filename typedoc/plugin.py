# Author: Jakub Andrýsek
# Email: email@kubaandrysek.cz
# Website: https://kubaandrysek.cz
# License: MIT
# GitHub: https://github.com/JakubAndrysek/mkdocs-typedoc
# PyPI: https://pypi.org/project/mkdocs-typedoc/

import os
import subprocess
import logging

from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
from mkdocs.structure.files import File

log: logging.Logger = logging.getLogger("mkdocs")


class TypeDocPlugin(BasePlugin):

    config_scheme = (
        ('source', config_options.Type(str, required=True)),
        ('output_dir', config_options.Type(str, required=False, default="typedoc")),
        ('tsconfig', config_options.Type(str, required=True)),
        ('options', config_options.Type(str, required=False)),
        ('name', config_options.Type(str, required=False, default="TypeDoc API")),
    )

    def on_files(self, files, config):
        # Path to your TypeScript source code
        src_path = self.config['source']

        # Path to the typedoc.json options file
        typedoc_options = self.config.get('options')

        output_dir = self.config['output_dir']

        # Path to the generated documentation
        doc_path = os.path.join(config["site_dir"], output_dir)

        if not os.path.exists(doc_path):
            os.makedirs(doc_path)

        # Name for the generated documentation
        typedoc_name = self.config['name']

        # Path to the tsconfig file
        tsconfig_path = self.config['tsconfig']

        if not os.path.exists(tsconfig_path):
            log.error("tsconfig.json file does not exist. Please create it or change the path in mkdocs.yml.")
            return files

        # Check if Node.js is installed
        if not self.is_node_installed():
            log.error("Node.js is not installed. Please install it from https://nodejs.org/en/download/.")
            return files

        # Check if TypeDoc is installed
        if not self.is_typedoc_installed():
            log.error("TypeDoc is not installed. Please install it with `npm install typedoc --save-dev`. See https://typedoc.kubaandrysek.cz for more information.")
            return files

        # Build TypeDoc documentation
        try:
            typedoc_config = [
                ("--out", doc_path),
                ("--name", typedoc_name),
                ("--tsconfig", tsconfig_path),
                ("--titleLink", "/"),
            ]

            if typedoc_options:
                typedoc_config.insert(2, ("--options", typedoc_options))

            # Flattening the list of pairs to pass into subprocess.run
            flattened_config = [item for pair in typedoc_config for item in pair]

            command = [self.get_npx_filename(), "typedoc", *flattened_config, src_path]
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            log.error("TypeDoc failed with error code %d" % e.returncode)
            return files
        except Exception as e:
            log.error(f"TypeDoc failed with error: {e}")
            return files

        # Add generated TypeDoc documentation to MkDocs
        for dirpath, dirnames, filenames in os.walk(doc_path):
            for filename in filenames:
                abs_src_path = os.path.join(dirpath, filename)
                doc_rel_path = os.path.relpath(abs_src_path, config["site_dir"])
                files.append(File(doc_rel_path, config["site_dir"], config["site_dir"], config["use_directory_urls"]))

        return files

    def get_npx_filename(self):
        return "npx.cmd" if os.name == "nt" else "npx"

    def is_node_installed(self):
        try:
            result = subprocess.run(["node", "--version"], check=True, capture_output=True, text=True)
            return result.returncode == 0
        except subprocess.CalledProcessError:
            return False
        except Exception as e:
            log.error(f"TypeDoc: Node.js failed with error: {e}")
            return False

    def is_typedoc_installed(self):
        try:
            result = subprocess.run([self.get_npx_filename(), "typedoc", "--version"], check=True,
                                    capture_output=True, text=True)
            return result.returncode == 0
        except subprocess.CalledProcessError:
            return False
        except Exception as e:
            log.error(f"TypeDoc: TypeDoc failed with error: {e}")
            return False

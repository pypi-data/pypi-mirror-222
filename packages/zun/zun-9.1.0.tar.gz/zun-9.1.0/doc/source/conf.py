# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))
# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
    'openstackdocstheme',
    'oslo_config.sphinxconfiggen',
    'oslo_policy.sphinxext',
    'oslo_policy.sphinxpolicygen',
]

# autodoc generation is a bit aggressive and a nuisance when doing heavy
# text edit cycles.
# execute "export SPHINX_DEBUG=1" in your terminal to disable

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# openstackdocstheme options
openstackdocs_repo_name = 'openstack/zun'
openstackdocs_pdf_link = True
openstackdocs_bug_project = 'zun'
openstackdocs_bug_tag = ''

config_generator_config_file = '../../etc/zun/zun-config-generator.conf'
sample_config_basename = '_static/zun'

policy_generator_config_file = '../../etc/zun/zun-policy-generator.conf'
sample_policy_basename = '_static/zun'

# General information about the project.
project = u'zun'
copyright = u'2013, OpenStack Foundation'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'native'

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'openstackdocs'

# Output file base name for HTML help builder.
htmlhelp_basename = '%sdoc' % project

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
    ('index',
     'doc-%s.tex' % project,
     u'Zun Documentation',
     u'Zun development team', 'manual'),
]

# Disable usage of xindy https://bugzilla.redhat.com/show_bug.cgi?id=1643664
latex_use_xindy = False

latex_domain_indices = False

latex_elements = {
    'makeindex': '',
    'printindex': '',
    'preamble': r'\setcounter{tocdepth}{3}',
    'extraclassoptions': 'openany',
}

# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx_mapping = {'http://docs.python.org/': None}

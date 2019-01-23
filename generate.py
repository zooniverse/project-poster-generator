import base64
import sys

import requests

from jinja2 import Template
from panoptes_client import Project


project = Project.find(slug=sys.argv[-1])

poster_info = {
    'image_name': '{}-poster.svg'.format(project.slug.replace('/','-')),
    'avatar_b64': base64.b64encode(
        requests.get(project.avatar['media'][0]['src']).content
    ),
    'avatar_type': project.avatar['media'][0]['content_type'],
}

poster_info.update(project.raw)

with open('template.svg') as template_f:
    template = Template(template_f.read())

with open(poster_info['image_name'], 'w') as out_f:
    out_f.write(template.render(**poster_info))

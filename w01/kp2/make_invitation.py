#!/usr/bin/env python3

import docx
import os

doc = docx.Document()
doc.add_paragraph('Hello!')

os.mkdir('output')
doc.save('output/invitation.docx')

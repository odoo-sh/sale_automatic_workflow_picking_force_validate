# Copyright 2022 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    "name": "Sale Automatic Workflow Picking Force Validate",
    "summary": """
        Force Quantities and validate the pickings.""",
    "version": "13.0.1.0.0",
    "category": "Uncategorized",
    "website": "http://sodexis.com/",
    "author": "Sodexis",
    "license": "OPL-1",
    "installable": True,
    "application": False,
    "depends": [
        "sale_automatic_workflow",
    ],
    "data": [
        "views/sale_workflow_process_views.xml",
    ],
}

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "myerp"
app_title = "myerp"
app_publisher = "suresh thakor"
app_description = "custom app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "smthakor1979@gmail.com"
app_license = "MIT"
app_logo_url = '/assets/erpnext/images/cs_logo.png'



# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/myerp/css/myerp.css"
# app_include_js = "/assets/myerp/js/myerp.js"

# include js, css files in header of web template
# web_include_css = "/assets/myerp/css/myerp.css"
# web_include_js = "/assets/myerp/js/myerp.js"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------
website_context = {
	"favicon": 	"/assets/myerp/images/cs_logo.png",
	"splash_image": "/assets/myerp/images/cs_logo.png"
}




# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "myerp.install.before_install"
# after_install = "myerp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "myerp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"myerp.tasks.all"
# 	],
# 	"daily": [
# 		"myerp.tasks.daily"
# 	],
# 	"hourly": [
# 		"myerp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"myerp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"myerp.tasks.monthly"
# 	]
# }

fixtures = [
    "Custom Script","Custom Field", "Property Setter", "Print Format"
    # add more here
]

# Testing
# -------

# before_tests = "myerp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "myerp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "myerp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


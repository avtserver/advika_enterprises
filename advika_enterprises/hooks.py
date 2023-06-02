from . import __version__ as app_version

app_name = "advika_enterprises"
app_title = "Advika Enterprises"
app_publisher = "MD Faiyaz Ansari"
app_description = "This app will mannaged all Enterprises workflow with supplier or vendor"
app_email = "faiyaz@avtutoring.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/advika_enterprises/css/advika_enterprises.css"
# app_include_js = "/assets/advika_enterprises/js/advika_enterprises.js"

# include js, css files in header of web template
# web_include_css = "/assets/advika_enterprises/css/advika_enterprises.css"
# web_include_js = "/assets/advika_enterprises/js/advika_enterprises.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "advika_enterprises/public/scss/website"

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "advika_enterprises.utils.jinja_methods",
#	"filters": "advika_enterprises.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "advika_enterprises.install.before_install"
# after_install = "advika_enterprises.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "advika_enterprises.uninstall.before_uninstall"
# after_uninstall = "advika_enterprises.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "advika_enterprises.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"advika_enterprises.tasks.all"
#	],
#	"daily": [
#		"advika_enterprises.tasks.daily"
#	],
#	"hourly": [
#		"advika_enterprises.tasks.hourly"
#	],
#	"weekly": [
#		"advika_enterprises.tasks.weekly"
#	],
#	"monthly": [
#		"advika_enterprises.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "advika_enterprises.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "advika_enterprises.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "advika_enterprises.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["advika_enterprises.utils.before_request"]
# after_request = ["advika_enterprises.utils.after_request"]

# Job Events
# ----------
# before_job = ["advika_enterprises.utils.before_job"]
# after_job = ["advika_enterprises.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"advika_enterprises.auth.validate"
# ]

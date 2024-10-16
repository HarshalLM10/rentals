# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters: dict | None = None):
    """Return columns, data, message, and chart for the report.

    This is the main entry point for the report. It accepts the filters as a
    dictionary and should return columns, data, message summary, and chart.
    It is called by the framework every time the report is refreshed or a filter is updated.
    """
    columns = get_columns()
    data = get_data()

    # Message and chart data
    message_summary = "Message Summary"
    chart = get_chart(data)

    return columns, data, message_summary, chart


def get_columns() -> list[dict]:
    """Return columns for the report.

    One field definition per column, just like a DocType field definition.
    """
    return [
        {
            "label": _("Column 1"),
            "fieldname": "column_1",
            "fieldtype": "Data",
        },
        {
            "label": _("Column 2"),
            "fieldname": "column_2",
            "fieldtype": "Int",
        },
        {
            "fieldname": "name1",
            "label": _("Make"),
            "fieldtype": "Data",
        },
        {
            "fieldname": "revenue",
            "label": _("Total Revenue"),
            "fieldtype": "Currency",
            "options": "AED",
        },
    ]


def get_data() -> list[dict]:
    """Return data for the report.

    The report data is fetched using `frappe.get_all`, 
    querying the 'Ride Booking' doctype and grouping by 'name1'.
    """
    return frappe.get_all(
        "Ride Booking",
        fields=["SUM(amount) as revenue", "vehicle.name1"],
        filters={"docstatus": 1},
        group_by="name1"
    )


def get_chart(data: list[dict]) -> dict:
    """Return chart data for the report.

    Generates a pie chart using the vehicle 'name1' as labels and the 'revenue' as values.
    """
    return {
        "data": {
            "labels": [x.get("name1") for x in data],
            "datasets": [
                {
                    "values": [x.get("revenue") for x in data]
                }
            ],
        },
        "type": "pie"
    }

// Copyright (c) 2024, BWH and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    // setup and onload also
	refresh(frm) {
        if (frm.doc.status === "New"){

            frm.add_custom_button("Accept" , () => {
                //status change to acepted 
                frm.set_value("status","Accepted")
                //svae the form
                frm.save()
            } , "Actions")

            frm.add_custom_button("Reject" , () => {
                //status change to acepted 
                frm.set_value("status","Rejected")
                //svae the form
                frm.save()
            }, "Actions")
        }
	},
    status(frm) {
        console.log("Status Changed ");
        
    }
});

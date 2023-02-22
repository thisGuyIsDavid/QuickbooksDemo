from app import api_calls

#   This will fail. Object already exists.
api_calls.create_customer({
        "FullyQualifiedName": "King Groceries",
        "PrimaryEmailAddr": {
            "Address": "jdrew@myemail.com"
        },
        "DisplayName": "King's Groceries",
        "Suffix": "Jr",
        "Title": "Mr",
        "MiddleName": "B",
        "Notes": "Here are other details.",
        "FamilyName": "King",
        "PrimaryPhone": {
            "FreeFormNumber": "(555) 555-5555"
        },
        "CompanyName": "King Groceries",
        "BillAddr": {
            "CountrySubDivisionCode": "CA",
            "City": "Mountain View",
            "PostalCode": "94042",
            "Line1": "123 Main Street",
            "Country": "USA"
        },
        "GivenName": "James"
    })

#   Get a list of all customers.
all_customers = api_calls.query_customers('SELECT * FROM Customer')
print('Found %s customers.' % len(all_customers.get('QueryResponse').get('Customer')))

#   Get the first customer
customer = all_customers.get('QueryResponse').get('Customer')[0]
print('Looking at %s (ID:%s)' % (customer.get('CompanyName'), customer.get('Id')))
#   Charge them for something.
invoice = api_calls.create_invoice(
    {
        "Line": [
            {
                "DetailType": "SalesItemLineDetail",
                "Amount": 100.0,
                "SalesItemLineDetail": {
                    "ItemRef": {
                        "name": "Services",
                        "value": "1"
                    }
                }
            }
        ],
        "CustomerRef": {
            "value": customer.get('Id')
        }
    }
)
print('Invoice %s for $%s has been created.' % (invoice.get('Invoice').get('DocNumber'), invoice.get('Invoice').get('TotalAmt')))

customer_after_invoice = api_calls.get_customer(customer.get('Id'))
print('You are owed $%s from this company.' % (customer_after_invoice.get('Customer').get('Balance')))

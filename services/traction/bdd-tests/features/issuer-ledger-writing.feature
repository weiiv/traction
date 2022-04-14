Feature: issuer ledger write operations
    Scenario: issuer-tenant writes and indy schema
        Given we have authenticated at the innkeeper
        And we have "1" traction tenants
        | name  | role    |
        | alice | issuer |
        And 'alice' is an issuer
        When "alice" creates a new schema labelled "degree"
        Then the schema "degree" will be on the ledger

        Examples:
        | schema_name  | schema_attrs   |
         | "degree"  | "name,degree,date" |
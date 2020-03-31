FORMAT: 1A
HOST: https://api.usaspending.gov

# TAS

These endpoints are used to power USAspending.gov's TAS search component on the advanced search page.
The response is a forest of filter search nodes, which despite having a unified structure represent different
database fields based on depth in the tree.

## Toptier Search [GET /api/v2/references/filter_tree/tas/{?depth}] [GET]

Returns a list of toptier agencies that have at least one TAS affiliated with them
+ Request
    + Parameters
        + `depth`: `0` (optional, enum[number]) How many levels deep the search will populate each tree. 
            + Members
                    + `0`
                    + `1`
                    + `2`
    + Schema
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "string"
        }

+ Response 200 (application/json)
    + Attributes (object)
        + `results` (required, array[TASFilterTreeNode], fixed-type)
    + Body

            {
                "results": [
                    {
                        "id": "1",
                        "description": "Agency of Donald Trump",
                        "ancestors": [],
                        "count": 100,
                        "children": null
                    },
                    {
                        "id": "2",
                        "description": "Agency of Michael Jackson",
                        "ancestors": [],
                        "count": "92",
                        "children": null
                    },
                    {
                        "id": "3",
                        "description": "Agency of Hillary Clinton",
                        "ancestors": [],
                        "count": "500",
                        "children": null
                    },
                    {
                        "id": "4",
                        "description": "Agency of Arnold Schwartzenager",
                        "ancestors": [],
                        "count": "200",
                        "children": null
                    },
                    {
                        "id": "5",
                        "description": "Agency of Jon Hill",
                        "ancestors": [],
                        "count": "23",
                        "children": null
                    },
                    {
                        "id": "6",
                        "description": "Agency of Elton John",
                        "ancestors": [],
                        "count": "11",
                        "children": null
                    },
                    {
                        "id": "7",
                        "description": "Agency of the Pop Group Hanson",
                        "ancestors": [],
                        "count": "55",
                        "children": null
                    },
                    {
                        "id": "8",
                        "description": "Agency of Nickle Back",
                        "ancestors": [],
                        "count": "44",
                        "children": null
                    },
                    {
                        "id": "9",
                        "description": "Agency of Marco Mendoza",
                        "ancestors": [],
                        "count": "22",
                        "children": null
                    },
                    {
                        "id": "10",
                        "description": "Agency of SQRLE",
                        "ancestors": [],
                        "count": "3",
                        "children": null
                    }
                ]
            }

## Search by Agency [GET /api/v2/references/filter_tree/tas/{agency}/{?depth}]

Returns a list of federal accounts associated with the specified agency
+ Request A request with a naics id 
    + Parameters
        + `agency`: `020` (required, string) 
        + `depth`: `0` (optional, enum[number]) How many levels deep the search will populate each tree. 
            + Members
                    + `0`
                    + `1`
                    + `2`        
        0 will return only federal accounts, and 1 will return federal accounts and any TAS under them
    + Schema
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "string"
        }

+ Response 200 (application/json)
    + Attributes (object)
        + `results` (required, array[TASFilterTreeNode], fixed-type)
    + Body

            {
                "results": [
                        {
                            "id": "11",
                            "description": "Federal Account of Donald Trump",
                            "ancestors": ["1"],
                            "count": 100
                        },
                        {
                            "id": "12",
                            "description": "Federal Account of Donald Trump II",
                            "ancestors": ["1"],
                            "count": 100
                        }
                ]
            }

## Search by Federal Account [GET /api/v2/references/filter_tree/tas/{agency}/{federal_account}/{?depth}]

Returns a list of Treasury Account Symbols associated with the specified federal account
+ Request A request with a naics id
    + Parameters
        + `agency`: `020` (required, string) 
        + `federal_account`: `0550`
        + `depth`: `0` (optional, enum[number]) How many levels deep the search will populate each tree.
            + Members
                    + `0`
                    + `1`
                    + `2` 
        With this tree structure, only TAS will be returned, and the tree depth will always be one, reguardless of provided depth.
    + Schema
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "string"
        }

+ Response 200 (application/json)
    + Attributes (object)
        + `results` (required, array[TASFilterTreeNode], fixed-type)
    + Body

            {
                "results": [
                        {
                            "id": "1111",
                            "description": "Treasury Account of Donald Trump",
                            "ancestors": ["1", "12"],
                            "count": 100
                        },
                        {
                            "id": "12211",
                            "description": "Treasury Account of Donald Trump II",
                            "ancestors": ["1", "12"],
                            "count": 100
                        }
                ]
            }

## Data Structures

### TASFilterTreeNode (object)

+ `id` (required, string)
+ `description` (required, string)
+ `ancestors` (required, array[string])
+ `count` (required, number)
+ `children` (required, array[TASFilterTreeNode], nullable)
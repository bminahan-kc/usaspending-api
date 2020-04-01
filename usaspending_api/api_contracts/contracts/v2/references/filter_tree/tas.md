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
                    "id": "012",
                    "ancestors": [],
                    "description": "Department of Agriculture",
                    "count": 139,
                    "children": [
                        {
                        "id": "012-8226",
                        "ancestors": [
                            "012"
                        ],
                        "description": "Miscellaneous Contributed Funds, Animal and Plant Health Inspection Service, Agriculture",
                        "count": 1,
                        "children": [
                            {
                            "id": "012-X-8226-000",
                            "ancestors": [
                                "012",
                                "012-8226"
                            ],
                            "description": "Miscellaneous Contributed Funds, Animal and Plant Health Inspection Service, Agriculture",
                            "count": 0,
                            "children": null
                            }
                        ]
                        },
                        {
                        "id": "012-8214",
                        "ancestors": [
                            "012"
                        ],
                        "description": "Miscellaneous Contributed Funds, Agricultural Research Service, Agriculture",
                        "count": 1,
                        "children": [
                            {
                            "id": "012-X-8214-000",
                            "ancestors": [
                                "012",
                                "012-8214"
                            ],
                            "description": "Miscellaneous Contributed Funds, Agricultural Research Service, Agriculture",
                            "count": 0,
                            "children": null
                            }
                        ]
                        }
                    ]
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
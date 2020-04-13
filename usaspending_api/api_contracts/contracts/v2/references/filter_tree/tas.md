FORMAT: 1A
HOST: https://api.usaspending.gov

# TAS

These endpoints are used to power USAspending.gov's TAS search component on the advanced search page.
The response is a forest of filter search nodes, which despite having a unified structure represent different
database fields based on depth in the tree.

## Toptier Search [GET /api/v2/references/filter_tree/tas/{?depth}]

Returns a list of toptier agencies that have at least one TAS affiliated with them
+ Request A request with a contract id
    + Parameters
        + `depth`: `0` (optional, enum[number]) How many levels deep the search will populate each tree. 
            + Members
                    + `0`
                    + `1`
                    + `2`
        0 will return only agencies, 1 will return agencies and any federal accounts under them, and so on.
        + `filter`: `port` (optional, string) When provided, only results who's id or name matches the provided string (case insensitive) will be returned, along with any ancestors to a matching node. 
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
                        "count": 129,
                        "children": null
                    },
                    {
                        "id": "013",
                        "ancestors": [],
                        "description": "Department of Commerce",
                        "count": 42,
                        "children": null
                    },
                    {
                        "id": "097",
                        "ancestors": [],
                        "description": "Department of Defense",
                        "count": 100,
                        "children": null
                    },
                    {
                        "id": "091",
                        "ancestors": [],
                        "description": "Department of Education",
                        "count": 28,
                        "children": null
                    },
                    {
                        "id": "089",
                        "ancestors": [],
                        "description": "Department of Energy",
                        "count": 43,
                        "children": null
                    },
                    {
                        "id": "075",
                        "ancestors": [],
                        "description": "Department of Health and Human Services",
                        "count": 134,
                        "children": null
                    },
                    {
                        "id": "070",
                        "ancestors": [],
                        "description": "Department of Homeland Security",
                        "count": 94,
                        "children": null
                    },
                    {
                        "id": "086",
                        "ancestors": [],
                        "description": "Department of Housing and Urban Development",
                        "count": 52,
                        "children": null
                    },
                    {
                        "id": "015",
                        "ancestors": [],
                        "description": "Department of Justice",
                        "count": 43,
                        "children": null
                    },
                    {
                        "id": "1601",
                        "ancestors": [],
                        "description": "Department of Labor",
                        "count": 32,
                        "children": null
                    },
                    {
                        "id": "019",
                        "ancestors": [],
                        "description": "Department of State",
                        "count": 38,
                        "children": null
                    },
                    {
                        "id": "014",
                        "ancestors": [],
                        "description": "Department of the Interior",
                        "count": 113,
                        "children": null
                    },
                    {
                        "id": "020",
                        "ancestors": [],
                        "description": "Department of the Treasury",
                        "count": 36,
                        "children": null
                    },
                    {
                        "id": "069",
                        "ancestors": [],
                        "description": "Department of Transportation",
                        "count": 113,
                        "children": null
                    },
                    {
                        "id": "036",
                        "ancestors": [],
                        "description": "Department of Veterans Affairs",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "068",
                        "ancestors": [],
                        "description": "Environmental Protection Agency",
                        "count": 16,
                        "children": null
                    },
                    {
                        "id": "047",
                        "ancestors": [],
                        "description": "General Services Administration",
                        "count": 16,
                        "children": null
                    },
                    {
                        "id": "080",
                        "ancestors": [],
                        "description": "National Aeronautics and Space Administration",
                        "count": 16,
                        "children": null
                    },
                    {
                        "id": "049",
                        "ancestors": [],
                        "description": "National Science Foundation",
                        "count": 8,
                        "children": null
                    },
                    {
                        "id": "031",
                        "ancestors": [],
                        "description": "Nuclear Regulatory Commission",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "024",
                        "ancestors": [],
                        "description": "Office of Personnel Management",
                        "count": 4,
                        "children": null
                    },
                    {
                        "id": "073",
                        "ancestors": [],
                        "description": "Small Business Administration",
                        "count": 7,
                        "children": null
                    },
                    {
                        "id": "028",
                        "ancestors": [],
                        "description": "Social Security Administration",
                        "count": 6,
                        "children": null
                    },
                    {
                        "id": "072",
                        "ancestors": [],
                        "description": "Agency for International Development",
                        "count": 20,
                        "children": null
                    },
                    {
                        "id": "310",
                        "ancestors": [],
                        "description": "Access Board",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "302",
                        "ancestors": [],
                        "description": "Administrative Conference of the U.S.",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "1136",
                        "ancestors": [],
                        "description": "African Development Foundation",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "309",
                        "ancestors": [],
                        "description": "Appalachian Regional Commission",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "084",
                        "ancestors": [],
                        "description": "Armed Forces Retirement Home",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "339",
                        "ancestors": [],
                        "description": "Commodity Futures Trading Commission",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "581",
                        "ancestors": [],
                        "description": "Consumer Financial Protection Bureau",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "061",
                        "ancestors": [],
                        "description": "Consumer Product Safety Commission",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "485",
                        "ancestors": [],
                        "description": "Corporation for National and Community Service",
                        "count": 4,
                        "children": null
                    },
                    {
                        "id": "096",
                        "ancestors": [],
                        "description": "Corps of Engineers - Civil Works",
                        "count": 12,
                        "children": null
                    },
                    {
                        "id": "511",
                        "ancestors": [],
                        "description": "Court Services and Offender Supervision Agency",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "347",
                        "ancestors": [],
                        "description": "Defense Nuclear Facilities Safety Board",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "513",
                        "ancestors": [],
                        "description": "Denali Commission",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "525",
                        "ancestors": [],
                        "description": "Election Assistance Commission",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "045",
                        "ancestors": [],
                        "description": "Equal Employment Opportunity Commission",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "1100",
                        "ancestors": [],
                        "description": "Executive Office of the President",
                        "count": 18,
                        "children": null
                    },
                    {
                        "id": "083",
                        "ancestors": [],
                        "description": "Export-Import Bank of the United States",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "027",
                        "ancestors": [],
                        "description": "Federal Communications Commission",
                        "count": 3,
                        "children": null
                    },
                    {
                        "id": "360",
                        "ancestors": [],
                        "description": "Federal Election Commission",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "054",
                        "ancestors": [],
                        "description": "Federal Labor Relations Authority",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "065",
                        "ancestors": [],
                        "description": "Federal Maritime Commission",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "093",
                        "ancestors": [],
                        "description": "Federal Mediation and Conciliation Service",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "368",
                        "ancestors": [],
                        "description": "Federal Mine Safety and Health Review Commission",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "029",
                        "ancestors": [],
                        "description": "Federal Trade Commission",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "005",
                        "ancestors": [],
                        "description": "Government Accountability Office",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "471",
                        "ancestors": [],
                        "description": "Gulf Coast Ecosystem Restoration Council",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "474",
                        "ancestors": [],
                        "description": "Institute of Museum and Library Services",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "1130",
                        "ancestors": [],
                        "description": "Inter-American Foundation",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "034",
                        "ancestors": [],
                        "description": "International Trade Commission",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "3301",
                        "ancestors": [],
                        "description": "John F. Kennedy Center for the Performing Arts",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "009",
                        "ancestors": [],
                        "description": "Legislative Branch Boards and Commissions",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "387",
                        "ancestors": [],
                        "description": "Marine Mammal Commission",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "389",
                        "ancestors": [],
                        "description": "Merit Systems Protection Board",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "524",
                        "ancestors": [],
                        "description": "Millennium Challenge Corporation",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "088",
                        "ancestors": [],
                        "description": "National Archives and Records Administration",
                        "count": 8,
                        "children": null
                    },
                    {
                        "id": "394",
                        "ancestors": [],
                        "description": "National Capital Planning Commission",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "025",
                        "ancestors": [],
                        "description": "National Credit Union Administration",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "417",
                        "ancestors": [],
                        "description": "National Endowment for the Arts",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "418",
                        "ancestors": [],
                        "description": "National Endowment for the Humanities",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "420",
                        "ancestors": [],
                        "description": "National Labor Relations Board",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "421",
                        "ancestors": [],
                        "description": "National Mediation Board",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "424",
                        "ancestors": [],
                        "description": "National Transportation Safety Board",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "431",
                        "ancestors": [],
                        "description": "Nuclear Waste Technical Review Board",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "432",
                        "ancestors": [],
                        "description": "Occupational Safety and Health Review Commission",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "434",
                        "ancestors": [],
                        "description": "Office of Government Ethics",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "071",
                        "ancestors": [],
                        "description": "Overseas Private Investment Corporation",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "1125",
                        "ancestors": [],
                        "description": "Peace Corps",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "1602",
                        "ancestors": [],
                        "description": "Pension Benefit Guaranty Corporation",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "060",
                        "ancestors": [],
                        "description": "Railroad Retirement Board",
                        "count": 6,
                        "children": null
                    },
                    {
                        "id": "050",
                        "ancestors": [],
                        "description": "Securities and Exchange Commission",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "090",
                        "ancestors": [],
                        "description": "Selective Service System",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "472",
                        "ancestors": [],
                        "description": "Surface Transportation Board",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "542",
                        "ancestors": [],
                        "description": "The Council of the Inspectors General on Integrity and Efficiency",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "010",
                        "ancestors": [],
                        "description": "The Judicial Branch",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "514",
                        "ancestors": [],
                        "description": "U.S. Agency for Global Media",
                        "count": 2,
                        "children": null
                    },
                    {
                        "id": "510",
                        "ancestors": [],
                        "description": "United States Chemical Safety Board",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "1133",
                        "ancestors": [],
                        "description": "United States Trade and Development Agency",
                        "count": 1,
                        "children": null
                    },
                    {
                        "id": "519",
                        "ancestors": [],
                        "description": "Vietnam Education Foundation",
                        "count": 1,
                        "children": null
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
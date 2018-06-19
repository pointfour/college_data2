import csv

filething = "reee.csv"

indexer = ["UNITID", "OPEID", "OPEID6", "SCHOOL", "CITY", "STABBR", "ZIP", "ACCREDAGENCY", "INSTURL", "NPCURL",
           "SCH_DEG", "HCM2", "MAIN", "NUMBRANCH", "PREDDEG", "HIGHDEG", "CONTROL", "ST_FIPS", "REGION", "LOCALE",
           "LOCALE2", "LATITUDE", "LONGITUDE", "CCBASIC", "CCUGPROF", "CCSIZSET", "HBCU", "PBI", "ANNHI", "TRIBAL",
           "AANAPII", "HSI", "NANTI", "MENONLY", "WOMENONLY", "RELAFFIL", "ADM_RATE", "ADM_RATE_ALL", "SATVR25",
           "SATVR75", "SATMT25", "SATMT75", "SATWR25", "SATWR75", "SATVRMID", "SATMTMID", "SATWRMID", "ACTCM25",
           "ACTCM75", "ACTEN25", "ACTEN75", "ACTMT25", "ACTMT75", "ACTWR25", "ACTWR75", "ACTCMMID", "ACTENMID",
           "ACTMTMID", "ACTWRMID", "SAT_AVG", "SAT_AVG_ALL", "PCIP01", "PCIP03", "PCIP04", "PCIP05", "PCIP09",
           "PCIP10", "PCIP11", "PCIP12", "PCIP13", "PCIP14", "PCIP15", "PCIP16", "PCIP19", "PCIP22", "PCIP23", "PCIP24",
           "PCIP25", "PCIP26", "PCIP27"
           ]


def getindex(name):
    """gets the index of the thing"""
    i = 0
    while name != indexer[i]:
        if i > len(indexer):
            break
        i = i + 1
    return i


def getaverage(name):
    with open(filething) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        index = getindex(name)
        count = 0
        total = float(0.0)
        for row in readCSV:
            # print(row[index])
            if (str(row[index]) != "NULL"):
                if count != 0:
                    print(row[index])
                    total = total + float(row[index])
                count = count + 1
    print "The " + name + " average " + str(float(total) / float(count))


def differential(SAT_SCORE, variationationing):
    with open(filething) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        index = getindex("SAT_AVG")
        schoolindex = getindex("SCHOOL")
        count = 0
        success_count = 0
        for row in readCSV:
            if (str(row[index]) != "NULL"):
                if (count != 0):
                    variation = abs(int(row[index]) - SAT_SCORE)
                    if variation < variationationing:
                        print(row[schoolindex] + ":" + row[index])
                        success_count = success_count + 1
                count = count + 1
        print "Thats " + str(success_count) + " places"


# with open(filething) as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     index = getindex("ADM_RATE")
#     count = 0
#     isnull = 0
#     for row in readCSV:
#         print(row[index])
#         count = count + 1
#         if row[index] == "NULL":
#             isnull = isnull + 1
#         print "Percent null is " + str(float(isnull) / float(count) * 100) + "%"
# getaverage("SAT_AVG")

differential(1470, 200)

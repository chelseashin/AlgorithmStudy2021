#start --

def solution(companies, applicants):
    is_change = True
    company_list = dict()
    applicant_list = dict()
    left = dict()
    for company in companies:
        raw_data = company.split(" ")
        company_list[raw_data[0]] = {"prefer":list(raw_data[1]), 
                                     "count":int(raw_data[2]),
                                     "applicant":dict(),
                                     "approve":dict()}
    for applicant in applicants:
        raw_data = applicant.split(" ")
        applicant_list[raw_data[0]] = {"prefer":raw_data[1], 
                                       "left_chance":int(raw_data[2]), 
                                       "count": int(raw_data[2])}
        left[raw_data[0]] = True

    while len(left) > 0:
        complete_appliance = list()
        for applicant in left.keys():
            if  applicant_list[applicant]["left_chance"] <= 0:
                complete_appliance.append(applicant)
                continue
            appliance_order = applicant_list[applicant]["count"] - applicant_list[applicant]["left_chance"]
            company = applicant_list[applicant]["prefer"][appliance_order]
            applicant_list[applicant]["left_chance"] -= 1
            if applicant in company_list[company]["prefer"]:
                company_list[company]["applicant"][applicant] = False

        for applicant in complete_appliance:
            if left.get(applicant) != None:
                left.pop(applicant)

        if len(left.keys()) <= 0: 
            break

        approve_list = list()
        for company in company_list.keys():
            prev_all_approve = set(company_list[company]["applicant"].keys())
            company_list[company]["approve"] = dict()
            for prefer_applicant in company_list[company]["prefer"]:
                if len(company_list[company]["approve"]) >= company_list[company]["count"]:
                    break
                if company_list[company]["applicant"].get(prefer_applicant) != None:
                    company_list[company]["approve"][prefer_applicant] = True
                    approve_list.append(prefer_applicant)

            current_approve = set(company_list[company]["approve"].keys())
            left_applicants = prev_all_approve - current_approve
            while len(left_applicants) > 0:
                left_applicant = left_applicants.pop()
                left[left_applicant] = True
        for approve in approve_list:
            if left.get(approve) != None:
                left.pop(approve)

    result = []
    for company in company_list.keys():
        applicant = sorted(list(company_list[company]["approve"].keys()))
        result.append("{0}_{1}".format(company, ''.join(applicant)))
    return result
  
if __name__ == "__main__":
    print(solution(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"], ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]))
    print(solution(["A abc 2", "B abc 1"], ["a AB 1", "b AB 1", "c AB 1"]))
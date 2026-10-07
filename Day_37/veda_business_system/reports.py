from service_manager import ServiceManager
from program_manager import ProgramManager
from inquiry_manager import InquiryManager

def generate_business_report():
    sm = ServiceManager()
    pm = ProgramManager()
    im = InquiryManager()

    services = sm.list_services()
    programs = pm.list_programs()
    inquiries = im.list_inquiries()

    print("\n================ BUSINESS SUMMARY REPORT ================")
    print(f"Total Digital Services Offered : {len(services)}")
    active_services = [s for s in services if s.get("status") == "Active"]
    print(f"  - Active Services            : {len(active_services)}")

    print(f"\nTotal Training/Intern Programs : {len(programs)}")
    internships = [p for p in programs if p.get("type", "").lower() == "internship"]
    trainings = [p for p in programs if p.get("type", "").lower() == "training"]
    print(f"  - Internships                : {len(internships)}")
    print(f"  - Training Programs          : {len(trainings)}")

    print(f"\nTotal Customer Inquiries       : {len(inquiries)}")
    pending = [i for i in inquiries if i.get("status") == "Pending"]
    resolved = [i for i in inquiries if i.get("status") == "Resolved"]
    print(f"  - Pending                    : {len(pending)}")
    print(f"  - Resolved                   : {len(resolved)}")
    print("========================================================\n")

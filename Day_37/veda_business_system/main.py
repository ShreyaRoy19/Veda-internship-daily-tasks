from service_manager import ServiceManager
from program_manager import ProgramManager
from inquiry_manager import InquiryManager
from reports import generate_business_report

def main():
    sm = ServiceManager()
    pm = ProgramManager()
    im = InquiryManager()

    while True:
        print("\n=============================================")
        print("  VEDA TECHNOLOGY BUSINESS MANAGEMENT SYSTEM ")
        print("=============================================")
        print("1. Add Digital Service")
        print("2. View / Search Services")
        print("3. Add Training / Internship Program")
        print("4. View Programs")
        print("5. Log Customer Inquiry / Request")
        print("6. Update Inquiry Status")
        print("7. View Inquiries")
        print("8. Generate Business Reports")
        print("9. Exit")

        choice = input("Enter choice (1-9): ").strip()

        try:
            if choice == "1":
                sid = input("Service ID (e.g., S101): ").strip()
                name = input("Service Name: ").strip()
                cat = input("Category (e.g., Cloud, Web, AI): ").strip()
                price = float(input("Estimated Cost ($): ").strip())
                sm.add_service(sid, name, cat, price)
                print(" Service added successfully.")

            elif choice == "2":
                cat = input("Filter by Category (leave blank for all): ").strip()
                results = sm.filter_services(category=cat if cat else None)
                print("\n--- Services ---")
                for s in results:
                    print(f"[{s['id']}] {s['name']} | Category: {s['category']} | Status: {s['status']} | ${s['price']}")

            elif choice == "3":
                pid = input("Program ID (e.g., P201): ").strip()
                title = input("Program Title: ").strip()
                ptype = input("Type (Internship/Training): ").strip()
                dur = int(input("Duration (weeks): ").strip())
                seats = int(input("Available Seats: ").strip())
                pm.add_program(pid, title, ptype, dur, seats)
                print(" Program added successfully.")

            elif choice == "4":
                ptype = input("Filter by Type (leave blank for all): ").strip()
                results = pm.filter_programs(program_type=ptype if ptype else None)
                print("\n--- Programs ---")
                for p in results:
                    print(f"[{p['id']}] {p['title']} | Type: {p['type']} | {p['duration_weeks']} wks | Seats: {p['available_seats']}")

            elif choice == "5":
                iid = input("Inquiry ID (e.g., INQ01): ").strip()
                name = input("Client Name: ").strip()
                email = input("Client Email: ").strip()
                target = input("Interested Service/Program: ").strip()
                details = input("Inquiry Details: ").strip()
                im.log_inquiry(iid, name, email, target, details)
                print(" Inquiry registered successfully.")

            elif choice == "6":
                iid = input("Enter Inquiry ID to update: ").strip()
                status = input("New Status (Pending/In Progress/Resolved): ").strip()
                im.update_status(iid, status)
                print(" Inquiry status updated.")

            elif choice == "7":
                status = input("Filter by Status (leave blank for all): ").strip()
                results = im.filter_by_status(status) if status else im.list_inquiries()
                print("\n--- Customer Inquiries ---")
                for i in results:
                    print(f"[{i['id']}] {i['client_name']} ({i['email']}) -> {i['target']} | Status: {i['status']}")

            elif choice == "8":
                generate_business_report()

            elif choice == "9":
                print("Exiting application. Goodbye!")
                break

            else:
                print("Invalid option. Please enter a number between 1 and 9.")

        except ValueError as ve:
            print(f"Input Error: {ve}")
        except KeyError as ke:
            print(f"Lookup Error: {ke}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
